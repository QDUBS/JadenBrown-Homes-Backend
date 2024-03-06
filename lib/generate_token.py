import jwt
from dotenv import load_dotenv
import os

load_dotenv()
def generate_token(payload):
    key = os.environ.get("SECRET_KEY")
    token = jwt.encode(payload=payload, key=key, algorithm="HS256")
    return token

def decode_token(token):
    key = os.environ.get("SECRET_KEY")
    payload = jwt.decode(token, key=key, algorithms="HS256")
    return payload
