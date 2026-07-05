# ==========================================
# MASTER CONFIGURATION CHEAT SHEET
# Fill these in with your unique assigned values from the Exam Portal!
# ==========================================

# 1. Your IITM Email
EMAIL = "22f3001028@ds.study.iitm.ac.in"

# 2. Q1: CORS Allowed Origin
Q1_ALLOWED_ORIGIN = "https://dash-28pptm.example.com"

# 3. Q2: OAuth JWKS (Issuer, Audience, and Public Key)
ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-rdholgc8.apps.exam.local"
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""

# 4. Q3: 12-Factor Config (Manually merge the variables)
Q3_PORT = 8000
Q3_WORKERS = 1
Q3_DEBUG = False
Q3_LOG_LEVEL = "info"

# 5. Q5: Analytics (Find the API key in the Q5 instruction tab)
Q5_API_KEY = "ak_ujcqntk3lp75xlovtqrgmi0a"

# 6. Q9: Idempotency & Rate Limit (Find total orders and rate limit)
Q9_TOTAL_ORDERS = 58
Q9_RATE_LIMIT = 19

# 7. Q10: Middleware Rate Limit (Find allowed origin and rate limit)
Q10_ALLOWED_ORIGIN = "https://app-lbvglz.example.com"
Q10_RATE_LIMIT = 11

# ==========================================
# FIXED VARIABLES (Do not change these)
# ==========================================
EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"
