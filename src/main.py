from fastapi import FastAPI, Query

from .models import Conta, ContaBase, DiaProjetado
from .store import listar_contas

app = FastAPI(title="Fluxo de Caixa Preditivo")

@app.get("/contas", response_model=list[Conta])
def rota_listar_contas():
    return listar_contas()