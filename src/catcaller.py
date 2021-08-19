import json
from pathlib import Path
from typing import Dict, List
import asyncio
import aiohttp


#todo: Make sure user can't input malicious input for breed
#^ make the responsibility belong to where breed is input
class Pet_Pics():
    query: str = ""
    key: str
    link: str
    pictures: str

    def __init__(self, path:str, pet: str):
        self.path = path

        if pet == "cat":
            self.link = "https://api.thecatapi.com/v1/images/search" + self.query
            self.key_type = "CAT_API_KEY"

        if pet == "dog":
            self.link = "https://api.thedogapi.com/v1/images/search" + self.query
            self.key_type = "DOG_API_KEY"

    async def get_key(self):
        self.key = json.load(self.path.open('r'))[self.key_type]

    def breed_response(self, breed:str):
        query = "?"

        if len(breed) == 4:
            self.query = query + "breed_ids=" + breed

    def query_response(self, params: Dict[str, str]):
        query = "?"
        if params["amount"]:
            query += "limit=" + str(params["amount"]) + "&"

        #if params["breed"]:
        #    query += "breed_ids=" + params["breed"] + "&"

        if params["gif"]:
            query += "mime_types=gif"
        else:
            query += "mime_types=jpg,png"

        self.query = query

    async def load_pictures(self) -> Dict[str, str]:        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.link) as response:
                object = await response.json()

        self.pictures = object

    def picture_urls(self) -> List[str]:
        return [url['url'] for url in self.pictures]
            


if __name__ == "__main__":
    context = {
        "amount": 3,
        "gif":0
    }

    to_keys = Path("./env-var/env.json")
    my_cats = Pet_Pics(to_keys, "cat")
    asyncio.run(my_cats.get_key())

    my_cats.query_response(context)
    asyncio.run(my_cats.load_pictures())

    for picture in my_cats.picture_urls():
        print(picture)
    
    
    
