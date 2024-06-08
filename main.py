from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float

bancoDados = {
    1:{
        "nome": "Pizza",
        "preco": 59.90
    },
    2:{
        "nome": "Lasanha",
        "preço":9.90
    }
}


app = FastAPI()

#rota principal de apresentação
@app.get("/")
def apresentacao():
    return {
       "mensagem": "Olá mundo!",
        "statusCode": 200
    }

@app.get("/{nome}")
def saudacao(nome):
    return {
        "mensagem": f'Olá {nome}!',
        "statusCode": 200
    }

@app.get("/produtos/")
def mostrarTodosProdutos():
    return bancoDados

@app.get("/produtos/{idProduto}")
def mostrarUMproduto(idProduto):
    try:
        if bancoDados[idProduto]:
            return {
                "produto": bancoDados[idProduto],
                "statusCode":200
            }
    except:
        return {
            "produto": "não encontrado",
            "statusCode": 404
        }

@app.post("/produtos/cadastrar/")
def cadastrarProduto( id: int, item: Produto):
    listaProdutos = bancoDados.values()

    for produto in listaProdutos:
        if produto['nome'] == item.nome:
            return {
                "mensagem": "Produto já cadastrado ",
                "statusCode" : 400
            }
        else :
            bancoDados[id]= item
            return {
                "mensagem": "Item cridado com sucesso",
                "Produto": item,
                "statusCode": 200
            }

@app.delete("/produtos/excluir/{id}")
def excluirProduto(id:int):
    bancoDados.pop(id)
    return {
        "mensagem": "Produto excluído",
        "idProduto": id,
        "statusCode":200
    }

