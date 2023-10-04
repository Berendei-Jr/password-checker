from fastapi import FastAPI
from pydantic import BaseModel

from password_checker import PasswordChecker

class Request(BaseModel):
    login: str
    password_hash: str

PasswordChecker.Init()
app = FastAPI()

@app.post("/api/v1/password_check")
async def create_item(req: Request):
    return {'result': PasswordChecker.check_credentials(req.login, req.password_hash)}
