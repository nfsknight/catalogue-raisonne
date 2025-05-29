import os
from typing import Annotated, Optional
from datetime import date

from fastapi import FastAPI, Depends

import motor.motor_asyncio

from pydantic.functional_validators import BeforeValidator
from pydantic import BaseModel


app = FastAPI(
    title="Catalogue Raisonné API",
    summary="A catalogue of all the known paintings and sculptures of artists"
)

#create client
client = motor.motor_asyncio.AsynchIOMotorClient(os.environ["MONGODB_URL"])
db = client.artists

#_id objects
PyObjectID = Annotated[str, BeforeValidator(str)]

#pydantic classes
class ArtModel(BaseModel):
    title: str (required)
    date: date | None = None
    location: str | None = None
    collection: str | None = None
    owner: str | None = None
    provenance: list[str] | None = None
    documentation: list[dict] | None = None

class UpdateArtModel(BaseModel):

class ArtCollection(BaseModel):

#operations: post, put, get, delete
#get all artists
#get artist collection
collection = db.get_collection(artist)
#get work of artist
