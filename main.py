from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descrição": "Um telefone inteligente",
        "preco": 1500.0,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descrição": "Um computador móvel",
        "preco": 3500.0,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descrição": "Um computador portátil",
        "preco": 2500.0,
    }
]



@app.get("/") # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}

@app.get("/produtos")
def listar_produtos():
    return produtos