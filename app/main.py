from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        'id': 1,
        'nome': 'Smartphone',
        'descricao': 'Um telefone que é inteligente',
        'preco': 1500.0,
    },
    {
        'id': 2,
        'nome': 'Notebook',
        'descricao': 'um computador que é móvel',
        'preco': 3500.0,
    },
    {
        'id': 3,
        'nome': 'Tablet',
        'descricao': 'Um computador que é móvel',
        'preco': 2500.0,
    },

]


@app.get("/") # Request

def hello_word():
    return {'Olá':'Mundo'}


@app.get("/produtos")

def listar_produtos():
    return produtos



@app.get("/produtos/{id}")

def buscar_prutdo(id: int):
    for produto in produtos:
        if produto['id'] == id:
            return produto
    return {'Status': 404, 'Mensagem':'Produto não encontrado'}