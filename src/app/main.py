from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import pandas as pd
from pydantic.typing import Literal

app = FastAPI()

@app.get("/")
def home():
    return{"message": "our app is up"}