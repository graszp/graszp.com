# graszp.com
Source of https://graszp.com, the home of graszp, a solution architecture method for working with AI.

Plain static HTML and CSS, published by GitHub Pages from the `main` branch (root folder). Push to `main` to publish.

- `index.html`: home page
- `template/graszp-san-template.md`: the downloadable SAN template
- `css/`: layout and type copied from the vernacular.cloud stylesheets; `css/graszp.css` holds the graszp colours and loads last
- `CNAME`: the custom domain for GitHub Pages
- `.nojekyll`: serve files as they are (no Jekyll build)
- `publish_template.py`: releases the SAN template from the vault note 94.06.01 (the single source) when its `Template version:` is bumped; `python publish_template.py` to check, `--publish` to copy
- `serve_localhost.py`: local preview before a push: `python serve_localhost.py` opens http://localhost:8001/

## Licences
- Method text and SAN template: CC BY 4.0, see `LICENSE-CONTENT.md`
- Site code (HTML, CSS): MIT, see `LICENSE`

Copyright © 2026 Vernacular Cloud LLC.
