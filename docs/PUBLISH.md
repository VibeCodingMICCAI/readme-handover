# Publish the stand page (GitHub Pages)

Participants open this site → clone the repo → run the activity.
The page generates its own QR code from the live URL.

## 1. Put this demo in its own GitHub repository

From the `ai-handover-demo/` folder:

```bash
git init
git add .
git commit -m "Initial AI handover stand demo"
gh repo create ai-handover-demo --public --source=. --remote=origin --push
```

## 2. Enable GitHub Pages

1. **Settings → Pages**
2. Source: Deploy from a branch
3. Branch: `main`, folder: `/docs`
4. Save

Stand URL:

```text
https://YOUR_USER.github.io/ai-handover-demo/
```

## 3. Share / print

- Share the Pages URL, or open `poster.html` and print it (QR is drawn in the browser).
- Optional: set `githubUser` in `docs/index.html` if auto-detect is not enough.
