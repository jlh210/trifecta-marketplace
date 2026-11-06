#!/usr/bin/env python3
"""Preflight check for Marketing OS outputs against output-specs.yaml.

Usage:
  preflight.py --specs output-specs.yaml --format instagram_carousel slide1.jpg slide2.jpg ...
  preflight.py --specs output-specs.yaml --format instagram_reel reel.mp4
  preflight.py --specs output-specs.yaml --list

Exit codes: 0 = all pass, 1 = at least one failure, 2 = setup problem.
Never modifies files. Never upscales. Prints one line per file plus a summary, and a JSON
report on the last line (prefixed with REPORT_JSON:) for agents to parse.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

try:
    import yaml  # PyYAML
except ImportError:
    print("SETUP: PyYAML missing. Run: pip install pyyaml pillow", file=sys.stderr)
    sys.exit(2)

IMAGE_EXT = {"jpg", "jpeg", "png", "webp"}
VIDEO_EXT = {"mp4", "mov", "m4v"}


def ratio_value(r):
    a, b = str(r).split(":")
    return float(a) / float(b)


def ext_of(path):
    e = os.path.splitext(path)[1].lower().lstrip(".")
    return "jpg" if e == "jpeg" else e


def check_dims(w, h, spec, tol_pct):
    """Return list of (level, message). Exact or larger at same ratio passes; smaller fails."""
    out = []
    tw, th = spec.get("width"), spec.get("height")
    if not tw or not th:
        return out
    target = tw / th
    actual = w / h
    dev = abs(actual - target) / target * 100
    if dev > tol_pct:
        out.append(("FAIL", f"ratio {w}x{h} = {actual:.3f}, expected {spec.get('ratio')} ({target:.3f}), off by {dev:.1f}%"))
    if w < tw or h < th:
        out.append(("FAIL", f"too small: {w}x{h}, need at least {tw}x{th} (never upscale; re-export from source)"))
    elif (w, h) != (tw, th):
        out.append(("WARN", f"{w}x{h} is larger than export size {tw}x{th}; platform will downscale. OK, but exact export is preferred"))
    return out


def check_filesize(path, spec):
    out = []
    size = os.path.getsize(path)
    if "max_mb" in spec and size > spec["max_mb"] * 1024 * 1024:
        out.append(("FAIL", f"file {size/1048576:.1f} MB exceeds {spec['max_mb']} MB"))
    if "max_kb" in spec and size > spec["max_kb"] * 1024:
        out.append(("FAIL", f"file {size/1024:.0f} KB exceeds {spec['max_kb']} KB"))
    if "min_kb" in spec and size < spec["min_kb"] * 1024:
        out.append(("FAIL", f"file {size/1024:.0f} KB below minimum {spec['min_kb']} KB"))
    return out


def check_image(path, spec, tol):
    try:
        from PIL import Image
    except ImportError:
        return None, [("SETUP", "Pillow missing. Run: pip install pillow")]
    out = []
    with Image.open(path) as im:
        w, h = im.size
        mode = im.mode
        icc = im.info.get("icc_profile")
    out += check_dims(w, h, spec, tol)
    if mode == "CMYK":
        out.append(("FAIL", "CMYK image; export as sRGB"))
    elif spec.get("color") == "sRGB" and icc and b"sRGB" not in icc[:400] and b"sRGB" not in icc:
        out.append(("WARN", "embedded color profile is not sRGB; colors may shift. Re-export as sRGB"))
    return (w, h), out


def ffprobe(path):
    if not shutil.which("ffprobe"):
        return None
    cmd = ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
           "stream=width,height,codec_name,r_frame_rate:format=duration", "-of", "json", path]
    try:
        data = json.loads(subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout or "{}")
    except Exception:
        return None
    st = (data.get("streams") or [{}])[0]
    return {
        "width": st.get("width"), "height": st.get("height"), "codec": st.get("codec_name"),
        "duration": float((data.get("format") or {}).get("duration") or 0),
    }


def check_video(path, spec, tol):
    out = []
    info = ffprobe(path)
    if not info or not info.get("width"):
        out.append(("UNCHECKED", "ffprobe unavailable or unreadable video; dimensions and duration NOT verified"))
        return None, out
    w, h = info["width"], info["height"]
    out += check_dims(w, h, spec, tol)
    codec = spec.get("codec")
    if codec and codec.lower().replace(".", "") == "h264" and info.get("codec") not in ("h264",):
        out.append(("FAIL", f"codec {info.get('codec')}, expected H.264"))
    dur = spec.get("duration_sec") or {}
    max_sec = dur.get("max") or (spec.get("video") or {}).get("max_sec")
    if max_sec and info["duration"] > max_sec:
        out.append(("FAIL", f"duration {info['duration']:.1f}s exceeds {max_sec}s"))
    if dur.get("min") and info["duration"] < dur["min"]:
        out.append(("FAIL", f"duration {info['duration']:.1f}s below {dur['min']}s"))
    return (w, h), out


def check_pdf(path, spec, tol):
    out = []
    try:
        from pypdf import PdfReader
    except ImportError:
        out.append(("UNCHECKED", "pypdf missing (pip install pypdf); page sizes NOT verified"))
        return out
    reader = PdfReader(path)
    n = len(reader.pages)
    pages = spec.get("pages") or {}
    if pages.get("min") and n < pages["min"]:
        out.append(("FAIL", f"{n} pages, minimum {pages['min']}"))
    if pages.get("hard_max") and n > pages["hard_max"]:
        out.append(("FAIL", f"{n} pages exceeds {pages['hard_max']}"))
    elif pages.get("max") and n > pages["max"]:
        out.append(("WARN", f"{n} pages; recommended max {pages['max']}"))
    target = spec["page_width"] / spec["page_height"]
    sizes = set()
    for i, p in enumerate(reader.pages, 1):
        pw, ph = float(p.mediabox.width), float(p.mediabox.height)
        sizes.add((round(pw), round(ph)))
        dev = abs(pw / ph - target) / target * 100
        if dev > tol:
            out.append(("FAIL", f"page {i} ratio {pw:.0f}x{ph:.0f} off target {spec.get('ratio')} by {dev:.1f}%"))
    if spec.get("same_size_all_pages") and len(sizes) > 1:
        out.append(("FAIL", f"pages have different sizes: {sorted(sizes)}"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--specs", required=True)
    ap.add_argument("--format")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()

    with open(a.specs) as f:
        specs = yaml.safe_load(f)
    formats = specs.get("formats", {})
    if a.list:
        for k, v in formats.items():
            dims = f"{v.get('width', v.get('page_width'))}x{v.get('height', v.get('page_height'))}"
            print(f"{k:24} {dims:11} {v.get('ratio')}")
        return 0
    if a.format not in formats:
        print(f"SETUP: unknown format '{a.format}'. Known: {', '.join(formats)}", file=sys.stderr)
        return 2
    if not a.files:
        print("SETUP: no files given", file=sys.stderr)
        return 2

    spec = formats[a.format]
    tol = float((specs.get("tolerance") or {}).get("ratio_pct", 1.0))
    allowed = {("jpg" if t == "jpeg" else t) for t in spec.get("file_types", [])}
    report, failed, carousel_dims = [], False, []

    slides = spec.get("slides")
    if slides:
        if len(a.files) < slides.get("min", 1) or len(a.files) > slides.get("max", 99):
            report.append({"file": "(set)", "results": [["FAIL", f"{len(a.files)} slides; allowed {slides.get('min')} to {slides.get('max')}"]]})
            failed = True

    for path in a.files:
        res = []
        if not os.path.isfile(path):
            res.append(("FAIL", "file not found"))
        else:
            e = ext_of(path)
            if spec.get("deliverable") == "pdf":
                if e != "pdf":
                    res.append(("FAIL", f"expected a PDF, got .{e}"))
                else:
                    res += check_pdf(path, spec, tol)
            else:
                if allowed and e not in allowed:
                    res.append(("FAIL", f"type .{e} not allowed; use {sorted(allowed)}"))
                if e in IMAGE_EXT:
                    dims, r = check_image(path, spec, tol)
                    res += r
                    if dims:
                        carousel_dims.append(dims)
                elif e in VIDEO_EXT:
                    _, r = check_video(path, spec, tol)
                    res += r
            res += check_filesize(path, spec)
        if any(l in ("FAIL", "SETUP") for l, _ in res):
            failed = True
        status = "FAIL" if any(l in ("FAIL", "SETUP") for l, _ in res) else ("UNCHECKED" if any(l == "UNCHECKED" for l, _ in res) else "PASS")
        print(f"{status:9} {path}")
        for l, m in res:
            print(f"          {l}: {m}")
        report.append({"file": path, "status": status, "results": [list(x) for x in res]})

    if slides and slides.get("same_ratio_all") and len(set(carousel_dims)) > 1:
        print(f"FAIL      (set) slides have different dimensions: {sorted(set(carousel_dims))}")
        report.append({"file": "(set)", "status": "FAIL", "results": [["FAIL", "mixed slide dimensions"]]})
        failed = True

    print(f"\nSUMMARY: {'FAIL' if failed else 'PASS'} ({len(a.files)} file(s), format {a.format})")
    print("REPORT_JSON:" + json.dumps({"format": a.format, "pass": not failed, "files": report}))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
