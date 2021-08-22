import json
import time
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

    def __init__(self, path: Path, pet: str):
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
            self.link += query + "breed_ids=" + breed

    def query_type(self, gif: bool):
        query = "?"

        #if params["breed"]:
        #    query += "breed_ids=" + params["breed"] + "&"

        if gif:
            query += "mime_types=gif"
        else:
            query += "mime_types=jpg,png"

        self.link += query

    async def load_pictures(self) -> Dict[str, str]:        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.link) as response:
                object = await response.json()

        self.pictures = object

    def picture_urls(self) -> List[str]:
        return [url['url'] for url in self.pictures]

    async def pet_get(self) -> str:
        await self.get_key()

        await self.load_pictures()
        

        return self.pictures[0]['url']

            
if __name__ == "__main__":
    context = {
        "amount": 3,
        "gif":0
    }

    test = Pet_Pics(path=Path("./env-var/env.json"), pet="cat")

    print(asyncio.run(test.simple_pet()))
    
    
    
