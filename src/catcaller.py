import json
from pathlib import Path
import requests
from typing import Dict

#todo: Make sure user can't input malicious input for breed
#^ make the responsibility belong to where breed is input
def breed_response(breed:str):
    query = "?"

    if len(breed) == 4:
        query += "breed_ids=" + breed
        return query


def query_response(params: Dict[str, str]):
    query = "?"
    if params["amount"]:
        query += "limit=" + str(params["amount"]) + "&"

    #if params["breed"]:
    #    query += "breed_ids=" + params["breed"] + "&"

    if params["gif"]:
        query += "mime_types=gif"
    else:
        query += "mime_types=jpg,png"

    return query

def cat_get(query: str):

    link = "https://api.thecatapi.com/v1/images/search" + query
    
    key = json.load(Path("./env-var/env.json").open('r'))["CAT_API_KEY"]
    
    url = json.loads(requests.get(link, headers={"x-api-key": key}).content)

    return url

if __name__ == "__main__":
    context = {
        "amount": 3,
        "gif": 1
    }
    imgs = cat_get(breed_response("beng"))
    for img in imgs:
        print(img["url"])
    
