from fastapi import FastAPI
import json
import httpx

app = FastAPI()

with open('env_2.json') as f:
    data = json.load(f)

@app.get("/")
async def read_root():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://cont1:8000")
        other_service_data = response.json()
    return {"message": data["message"], "cont1_response": other_service_data}
