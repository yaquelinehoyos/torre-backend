from fastapi import FastAPI
import requests
import json
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/bio/{bio_id}")
async def read_bio(bio_id):
    torre_bio_url = "https://torre.bio/api/bios/"+bio_id
    torre_bio = requests.get(torre_bio_url)
    if torre_bio.status_code == 200:
        data = json.loads(torre_bio.content.decode('utf-8'))
        return {"message": data}

@app.get("/content/filters")
async def read_filters():
        filters = {
            "frontend" : [ "Vue", "React", "Angular" ],
            "backend" : [ "Laravel", "Django", "FastAPI", "Ruby on rails", "Flask", "NodeJs" ],
            "computer_science" : [ "History", "Theorical computer science", "Computer systems and computacional processes", "Artificial intelligence", "Applied computer science" ]
         }
        return {"message": filters}