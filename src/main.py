from fastapi import FastAPI, Query

from .models import Conta, ContaBase, DiaProjetado
from .repository import listar_contas, criar_conta

app = FastAPI(title="Fluxo de Caixa Preditivo")

@app.get("/contas", response_model=list[Conta])
def rota_listar_contas():
    return listar_contas()


@app.post("/conta", response_model=Conta, status_code=200)
def rota_criar_conta(dados: ContaBase):
    return criar_conta(dados)