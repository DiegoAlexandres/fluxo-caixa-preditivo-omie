from .models import Conta, ContaBase

contas: list[Conta] = []

_proximo_id = 1

def listar_contas() -> list[Conta]:
    return contas


def criar_conta(dados: ContaBase) -> Conta:
    global _proximo_id

    nova_conta = Conta(
        id = _proximo_id,
        nome = dados.nome,
        valor = dados.valor,
        data = dados.data,
        tipo = dados.tipo,
    )

    contas.append(nova_conta)
    _proximo_id += 1

    return nova_conta

