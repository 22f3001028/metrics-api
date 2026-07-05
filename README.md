# Metrics API — ELI15 Walkthrough

## 1. What this assignment actually wants (in plain words)

Think of it as building a tiny website-for-robots (an "API") that:

1. Takes a list of numbers from the URL, like `?values=1,2,3`
2. Does simple math on them (count, sum, min, max, average)
3. Hands the answer back as JSON (a structured text format computers read easily)
4. Only lets ONE specific website (`https://dash-28pptm.example.com`) talk to it
   from a browser — this is called **CORS** (Cross-Origin Resource Sharing).
   Browsers block websites from calling APIs on other domains unless the API
   explicitly says "yes, this domain is allowed" via a header.
5. Tags every response with a unique ID and how long it took to process —
   useful for debugging in real systems.

You are NOT hard-coding the answer, because the grader sends random numbers
each time and expects your server to actually compute the result live.

## 2. What's in this folder

- `main.py` — the actual API code (explained below)
- `requirements.txt` — the two libraries it needs (FastAPI + Uvicorn, the
  server that runs FastAPI)

## 3. How `main.py` works, piece by piece

- **`ALLOWED_ORIGIN`** — the one website allowed to call you. FastAPI's
  built-in `CORSMiddleware` automatically:
  - Adds the `Access-Control-Allow-Origin` header ONLY when the request's
    `Origin` matches this value.
  - Automatically handles `OPTIONS` preflight requests (the "asking
    permission" request browsers send before the real request) — you don't
    have to write that logic yourself.
- **`TimingAndRequestIDMiddleware`** — a small custom layer that:
  - Generates a random UUID (`X-Request-ID`) so every request is traceable.
  - Measures how long your code took (`X-Process-Time`) using a stopwatch
    (`time.perf_counter()`), started right before the request is handled and
    stopped right after.
- **`get_stats()`** — the actual endpoint:
  - Splits `"1,2,3"` into `["1", "2", "3"]`, then converts each to an integer.
  - Uses Python's built-in `len`, `sum`, `min`, `max` — no need to write math
    from scratch.
  - `mean = total / count` — a plain float division, which easily satisfies
    the "±0.01 accuracy" requirement.

## 4. Before you deploy — do this one edit

Open `main.py` and change:

```python
MY_EMAIL = "your-email@example.com"
```

to your actual logged-in email address exactly as required by the
assignment.

## 5. Deploying it for free (Render.com — no credit card, no CLI needed)

1. Go to https://render.com and sign up (you can use your GitHub account).
2. Push this folder to a new **public GitHub repository**:
   - Create a repo on GitHub (e.g. `metrics-api`).
   - Upload/push these three files (`main.py`, `requirements.txt`, and
     optionally this `README.md`) to it.
3. In Render, click **New +** → **Web Service**.
4. Connect your GitHub account and pick the repo you just made.
5. Fill in the settings:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click **Create Web Service**. Render will build and deploy it — this
   takes a couple of minutes.
7. When it's done, Render gives you a public URL like:
   `https://metrics-api-xyz.onrender.com`
   That is your **base URL** to paste into the assignment.

### Alternative hosts (same idea, same start command)
- **Railway.app** — similar "connect GitHub repo, auto-deploy" flow.
- **Fly.io** — needs their CLI (`flyctl launch`, `flyctl deploy`), a bit more
  setup but very reliable.
- **Hugging Face Spaces** — choose the "Docker" or "FastAPI" template.

## 6. How to test your live deployment yourself before submitting

Replace `YOUR_URL` below with your real deployed base URL.

```bash
# 1. Does the math work?
curl "https://YOUR_URL/stats?values=4,8,15,16,23,42"

# 2. Does the allowed origin get the CORS header?
curl -i -X OPTIONS "https://YOUR_URL/stats" \
  -H "Origin: https://dash-28pptm.example.com" \
  -H "Access-Control-Request-Method: GET" | grep -i access-control-allow-origin

# 3. Does a random other origin get REJECTED (no header at all)?
curl -i -X OPTIONS "https://YOUR_URL/stats" \
  -H "Origin: https://someone-else.com" \
  -H "Access-Control-Request-Method: GET" | grep -i access-control-allow-origin
# ^ this should print NOTHING if it's working correctly

# 4. Are the custom headers present?
curl -i "https://YOUR_URL/stats?values=1,2,3" | grep -i "x-request-id\|x-process-time"
```

If step 3 prints nothing and the other three print the expected data, you're
done — paste your base URL into the assignment field.
