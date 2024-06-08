from fastapi import FastAPI
from pydantic import BaseModel

bdLirvros = {}

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    preco: float
    disponibilidade: bool

app = FastAPI()

@app.get("/")
def mostrarInfos():
    return {
        "mensagem": "Api de livros",
        "versao": "1.0"
    }

@app.get("/livros/")
def mostrarTodosLivros():
    return{
        "livros": bdLirvros,
        "statusCode": 200
    }

@app.get("/livros/{id}")
def mostrarUmLivro(id: int):
    try:
        return {
            "livro": bdLirvros[id],
            "statusCode": 200
        }
    except:
        return {
            "livro": "não encontrado",
            "statusCode": 404
        }