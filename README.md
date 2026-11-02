# Who may read our messages? (Chat Control 2.0)

One HTML file per slide, so several people can work in parallel.

- `slides/NN-name.html` — one slide each (the `<section>` plus its own chart script, if any)
- `shared/head.html` — styles and shared SVG symbols; `shared/foot.html` — slide-position-in-URL script
- `chat-control-2.0.html` — **generated**, do not edit by hand
- `speaker-notes.md` — notes, page numbers match the slides

## Workflow

1. Edit your slide in `slides/`.
2. Run `python3 build.py` and open `chat-control-2.0.html` (`#slide-23` jumps to slide 23, and a reload keeps your place).
3. Commit your slide file. If `chat-control-2.0.html` conflicts after a merge, just run `python3 build.py` again.

Slides are joined in file-name order. To insert or move a slide, renumber the `NN-` prefixes and update the page number inside the slide (`<p class="page">`).
