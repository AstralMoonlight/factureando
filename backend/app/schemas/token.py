# app/schemas/token.py

from pydantic import BaseModel

class TokenOut(BaseModel):
    access_token: str
    token_type: str
