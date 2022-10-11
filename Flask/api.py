from typing import Optional, List, Dict, Any
import json
from fastapi import FastAPI
from pydantic import BaseModel
#  para rodar, no terminal: python3.10 -m uvicorn api:app --reload

app = FastAPI()


#  Serializador de saída, boa prática ter um "Out" no nome
class PersonOut(BaseModel):
    id: int
    name: str
    picture: str
    age: int
    email: str
    about: Optional[str] = ""  # optional precisa de valor default
    is_active: bool


@app.get("/", response_model=List[PersonOut])
# colocando "/docs", o fastapi cria uma página web de
#  documentação da API
# também tem o "/redoc"
async def read_root(is_active: Optional[str] = None):
    #return {"nome": "thiago"}  # dicionário, mas aceita classes também:
    if is_active is not None:  # caso não seja passado nada, não filtra
        is_active = True if is_active.lower() is not None else False

    return get_pessoas(is_active=is_active)
    #  adicionando a capacidade de buscar por pessoas ativas na url
    #  localhost:8000?is_active=active


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    #  o "q" serve para indicar que pode ser passada query string, com "?q="
    #  localhost:8000/items/99?q=teste
    return {"item_id ": item_id, "q": q}


def get_pessoas(is_active=None) -> List[Dict[str, Any]]:
    with open("data.json") as datafile:
        data = json.loads(datafile.read())
        if is_active is not None:
            return [
                pessoa for pessoa in data if pessoa["is_active"] == is_active
            ]
        return data
