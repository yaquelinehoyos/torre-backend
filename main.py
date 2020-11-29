from fastapi import FastAPI
import requests
import json
from starlette.middleware.cors import CORSMiddleware
import filters

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/bio/{username}")
async def read_bio(username):
    torre_bio_url = "https://torre.bio/api/bios/"+username
    torre_bio = requests.get(torre_bio_url)
    if torre_bio.status_code == 200:
        data = json.loads(torre_bio.content.decode('utf-8'))
        return {"message": data}


@app.get("/content/filters")
async def read_filters():
    return {"message": filters.filters}
