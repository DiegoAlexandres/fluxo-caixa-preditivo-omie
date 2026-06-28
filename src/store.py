from .models import Conta, ContaBase

contas: list[Conta] = []

_proximo_id = 1

def listar_contas() -> list[Conta]:
    return contas