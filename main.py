import time
import uuid

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

# ---------------------------------------------------------------------------
# 1. CHANGE THIS to your real logged-in email before you deploy.
# ---------------------------------------------------------------------------
MY_EMAIL = "22f3001028@ds.study.iitm.ac.in"

# The ONE origin the assignment allows. No wildcards, no extra origins.
ALLOWED_ORIGIN = "https://dash-28pptm.example.com"

app = FastAPI()


# ---------------------------------------------------------------------------
# Custom middleware: stamps every response with a unique request id and
# how long the handler took to run.
# ---------------------------------------------------------------------------
class TimingAndRequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        start = time.perf_counter()

        response = await call_next(request)

        duration = time.perf_counter() - start
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = f"{duration:.6f}"
        return response


# Order matters here: the middleware added LAST wraps everything ELSE,
# so TimingAndRequestIDMiddleware (added second) is the outermost layer.
# That guarantees X-Request-ID / X-Process-Time land on every response,
# including the CORS preflight responses handled below.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],   # only this origin gets ACAO header
    allow_credentials=False,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)
app.add_middleware(TimingAndRequestIDMiddleware)


@app.get("/stats")
def get_stats(values: str = Query(..., description="Comma-separated integers, e.g. 1,2,3")):
    # Parse "1,2,3" -> [1, 2, 3]. Ignore stray blanks like trailing commas.
    numbers = [int(v.strip()) for v in values.split(",") if v.strip() != ""]

    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = total / count

    return {
        "email": MY_EMAIL,
        "count": count,
        "sum": total,
        "min": minimum,
        "max": maximum,
        "mean": mean,
    }
