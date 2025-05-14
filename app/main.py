from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos
from typing import List

app = FastAPI()
lista_produtos = Produtos()

@app.get("/") # Request

def hello_word():
    return {'Olá':'Mundo'}


@app.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos():
    return lista_produtos.listar_produtos()



@app.get("/produtos/{id}", response_model=ProdutosSchema)
def buscar_produto(id: int):
    return lista_produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto:ProdutosSchema):
    return produto.adicionar_produto(produto.model_dump())