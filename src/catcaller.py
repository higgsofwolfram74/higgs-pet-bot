import json
import time
from pathlib import Path
from typing import Dict, List, Tuple, Union
import asyncio
import aiohttp


#todo: Make sure user can't input malicious input for breed
#^ make the responsibility belong to where breed is input
class Pet_Pics():
    animal: str
    key: str
    link: str
    pictures: str

    def __init__(self, path: Path, pet: str):
        self.path = path

        if pet == "cat":
            self.link = "https://api.thecatapi.com/v1/images/search"
            self.key_type = "CAT_API_KEY"


        elif pet == "dog":
            self.link = "https://api.thedogapi.com/v1/images/search"
            self.key_type = "DOG_API_KEY"

        else:
            print("Invalid animal type")

    async def get_key(self):
        self.key = json.load(self.path.open('r'))[self.key_type]

    def breed_response(self, breed:str):
        query = "?"

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
        async with aiohttp.ClientSession(headers={'x-api-key': self.key}) as session:
            print(f"Getting animal from {self.link}")
            async with session.get(self.link) as response:
                object = await response.json()

        self.pictures = object

    def picture_urls(self) -> List[str]:
        return [url['url'] for url in self.pictures]

    async def pet_get(self) -> str:
        await self.get_key()

        await self.load_pictures()
        

        return self.pictures[0]['url']

    async def get_breeds(animal: str) -> List[Tuple[Union[str,int], str]]:
        if animal == 'cat':
            ani = "https://api.thecatapi.com/v1/breeds"

        elif animal == 'dog':
            ani = "https://api.thedogapi.com/v1/breeds"
        
        else: 
            print("Invalid animal")
            return None

        async with aiohttp.ClientSession() as session:
            async with session.get(ani) as response:
                object = await response.json()

        time.sleep(1)

        return [(breed['id'], breed['name']) for breed in object]



            
if __name__ == "__main__":
    context = {
        "amount": 3,
        "gif":0
    }

    test = Pet_Pics(path=Path("./env-var/env.json"), pet="dog")

    breeds = asyncio.run(Pet_Pics.get_breeds("dog"))
    time.sleep(1)
    for breed in breeds:
        print(f"The breed {breed[1]} has the id {breed[0]}")
    
    
    
