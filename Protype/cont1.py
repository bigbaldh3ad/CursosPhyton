from fastapi import FastAPI
import json

app = FastAPI()

with open('env.json') as f:
    data = json.load(f)

@app.get("/")
def read_root():
    return {"message": data["message"]}
