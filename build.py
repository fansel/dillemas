#!/usr/bin/env python3
"""Build chat-control-2.0.html from shared/head.html, slides/*.html and shared/foot.html.

Edit a slide in slides/NN-name.html (one file per slide), then run:
    python3 build.py
Slides are joined in file-name order, so keep the NN- prefix.
"""
from pathlib import Path

root = Path(__file__).resolve().parent
parts = [(root / "shared" / "head.html").read_text(encoding="utf-8")]
slides = sorted((root / "slides").glob("*.html"))
parts += [s.read_text(encoding="utf-8").rstrip() + "\n\n" for s in slides]
parts.append((root / "shared" / "foot.html").read_text(encoding="utf-8"))
(root / "chat-control-2.0.html").write_text("".join(parts), encoding="utf-8")
print(f"built chat-control-2.0.html from {len(slides)} slides")
