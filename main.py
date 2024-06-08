from fastapi import FastAPI

bancoDados = {
    "1":{
        "nome": "Pizza",
        "preco": "59,90"
    },
    "2":{
        "nome": "Lasanha",
        "preço":"9,90"
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
            "statuCode": 404
        }