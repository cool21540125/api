# https://stackoverflow.com/questions/59886504/python-json-web-token-jwt-get-request-401-error-with-apple-store-connect
import jwt
import os
import time
from dotenv import load_dotenv

load_dotenv()

ISSUER_ID = os.getenv("ISSUER_ID")
KEY_ID = os.getenv("KEY_ID")

with open("AuthKey_4F74XL6KL9.p8", "r+b") as keyfile:
    private_key = keyfile.read()

expir = round(time.time() + 20 * 60)

token = jwt.encode(
    {"iss": ISSUER_ID, "exp": expir, "aud": "appstoreconnect-v1"},
    private_key,
    "ES256",
    headers={"kid": KEY_ID},
)

print(token)
