# NYJC SIG open-house directory

A lightweight mobile-first directory containing the 45 SIGs listed on NYJC's official website on 2 November 2026. No build step, accounts, API keys or runtime libraries are needed. Search and category filters work in the browser, and every SIG has a shareable hash URL that works on GitHub Pages.

## Publish on GitHub Pages

1. Create a repository (suggested name: `nyjc-sigs`). Public repositories support GitHub Pages on GitHub Free.
2. Upload this folder's contents so `index.html` is at the repository root.
3. Open **Settings → Pages → Deploy from a branch**.
4. Choose **main** and **/(root)**, then **Save**.
5. Use the exact published address shown by GitHub Pages. Test it on your phone before printing the QR code.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Preview and editing

Serve the folder with a static HTTP server, for example `python -m http.server 8000`, then open `http://localhost:8000`. Update SIG content in `data.js`. The file is regular JavaScript containing one data object.

Each group contains:
- `name`, `category`, `description`: the directory and profile text.
- `activities`: an array of strings for the activity list.
- `schedule`, `location`: current session and open-house booth details.
- `joinUrl`, `instagram`: full HTTPS links (empty values hide these links).
- `photos`: up to two photo objects; the display always caps this array at two.

Example photo entry (add your own actual image in `assets/`):

```js
"photos": [
  { "src": "assets/club-session.jpg", "alt": "Members working together at a club session", "caption": "A recent club session" },
  { "src": "assets/club-performance.jpg", "alt": "Members performing on stage", "caption": "Our performance" }
]
```

Avoid changing a group's `id` after sharing its link. A profile link looks like `https://YOUR-SITE/#sig/nyarts`.

## QR code

After publication, generate a QR code for the final address, not the GitHub repository:

```sh
python -m pip install 'qrcode[pil]'
python tools/make_qr.py 'https://YOUR-PUBLISHED-SITE/'
```

This produces `open-house-qr.png` and a vector `open-house-qr.svg` suitable for printing. The QR includes a white quiet zone. Test both the main directory and several SIG links on mobile before printing.

## Content and outstanding inputs

Source: https://www.nanyangjc.moe.edu.sg/life-at-nyjc/student-interest-groups/

The eight official category pages supplied the names and short paraphrased descriptions. Each profile links directly to its official school page. Missing schedules and booth locations are clearly marked. This is a student-built directory, not an official school site.

NYSingularity, Nanyang Astronomers’ Club and NYMagic Society use the complete descriptions and EXCO details from the supplied SIG Details document, with exactly two selected photos each. NYMagic’s supplied Instagram account is linked. The remaining 42 profiles use short school-directory summaries. Current session times and open-house booth locations still need to be supplied. The school category summaries contain apparent institution-name mistakes for JFire and Harmonix; these names were not repeated in the paraphrases.

## Validation

JavaScript syntax and automated content/navigation/search checks passed. The preview service was unavailable, so visual browser QA remains outstanding. Check phone layouts, real photo cropping, share controls and external links after deployment.
