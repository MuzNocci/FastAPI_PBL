import uvicorn
from fastapi import FastAPI



app = FastAPI()


vendas = {
    1: {'produto':'Camisa', 'tamanho':'P', 'estampa':'Não', 'cor':'Preta', 'preco':29.90, 'quantidade':2},
    2: {'produto':'Camisa', 'tamanho':'M', 'estampa':'Sim', 'cor':'Branca', 'preco':29.90, 'quantidade':1},
    3: {'produto':'Short', 'tamanho':'M', 'estampa':'Não', 'cor':'Vermelha', 'preco':35.90, 'quantidade':1},
    4: {'produto':'Bermuda', 'tamanho':'G', 'estampa':'Não', 'cor':'Azul', 'preco':49.90, 'quantidade':1},
    5: {'produto':'Camisa', 'tamanho':'M', 'estampa':'Não', 'cor':'Laranja', 'preco':29.90, 'quantidade':1},
}


@app.get('/')
def index():

    return vendas


@app.get('/{id_venda}')
def consulta_venda(id_venda:int):

    if id_venda and isinstance(id_venda, int):
        return vendas[id_venda]
    else:
        return {'Error':'Venda não encontrada'}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)