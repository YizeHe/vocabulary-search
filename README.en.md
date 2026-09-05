# Gaokao Curriculum 3000 Word Lookup

English | [简体中文](README.md)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

Live site: https://voc.forbiddenx.top/

A local web page for looking up words from the Chinese National Gaokao English curriculum list (about 3,000 headwords). Search by English spelling or Chinese gloss. The same page can be opened on a phone or another computer on the LAN.

The current list has about 832 entries: common curriculum words plus in-class additions, merged and de-duplicated.

## Features

- Filter word cards as you type, in English or Chinese
- Clearing the box shows the full list again
- HTTP server binds to `0.0.0.0:8811` so other devices on the same network can open it

## Requirements

- Python 3.8 or later
- No third-party packages

## Usage

From the project directory:

```bash
python serve.py
```

On this machine:

```text
http://127.0.0.1:8811/
```

The process prints LAN URLs, for example:

```text
http://192.168.x.x:8811/
```

Open that address on another phone or computer on the same Wi-Fi. Do not use `localhost` or `127.0.0.1` on those devices.

If another device cannot connect, allow Python through the Windows firewall, or add an inbound rule for TCP port `8811`.

## Rebuild the page

`1.txt` holds the original page and the extra-word notes. After you edit it:

```bash
python build.py
```

This merges the additions into `index.html` and leaves the UI and search behavior unchanged.

## Deploy to Cloudflare

Copy the latest `index.html` into `public/`, then:

```bash
# Pages
wrangler pages deploy public --project-name voc --branch main --commit-dirty=true

# Custom domain voc.forbiddenx.top
wrangler deploy
```

- Custom domain: https://voc.forbiddenx.top/
- Pages: https://voc-bh4.pages.dev/

## Layout

| File | Role |
|------|------|
| `index.html` | Lookup page (word list + UI) |
| `public/` | Cloudflare static assets |
| `wrangler.jsonc` | Cloudflare deploy config |
| `serve.py` | LAN HTTP server on port 8811 |
| `build.py` | Merge `1.txt` into `index.html` |
| `1.txt` | Original HTML and classroom additions |

## License

This project is licensed under the [Apache License 2.0](LICENSE).
