# Fluxo Caixa Preditivo Omie

API REST em Python FastAPI para projeção de fluxo de caixa: cadastro de contas a pagar e a receber, e cálculo do saldo futuro projetado dia a dia, com identificação de datas de risco de caixa negativo.

## O problema

Pequenas e médias empresas frequentemente não têm visibilidade clara sobre seu saldo de caixa nos próximos dias/semanas, informação hoje mantida manualmente em planilhas. Esta API projeta o saldo futuro a partir das contas a pagar e a receber já cadastradas, permitindo identificar com antecedência se o caixa ficará negativo em algum momento.

## Stack

- **Python 3.14**
- **FastAPI** — framework web e validação de dados
- **Uvicorn** — servidor ASGI
- **uv** — gerenciamento de dependências e ambiente

## Como rodar

```bash
git clone https://github.com/DiegoAlexandres/fluxo-caixa-preditivo-omie.git
cd fluxo-caixa-preditivo-omie
uv sync
uv run uvicorn main:app --reload
```

Acesse a documentação interativa em [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) para testar todas as rotas direto no navegador.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/contas` | Cadastra uma conta a pagar ou a receber (nome, valor, data, tipo) |
| `GET` | `/contas` | Lista todas as contas cadastradas |
| `GET` | `/forecast` | Retorna a projeção de saldo dia a dia, a partir de um saldo inicial e um número de dias |
| `GET` | `/forecast/alertas` | Retorna as datas em que o saldo projetado fica negativo |

## Exemplo de uso

**Cadastrar uma conta a pagar:**
```bash
curl -X POST http://127.0.0.1:8000/contas \
  -H "Content-Type: application/json" \
  -d '{"nome": "Aluguel", "valor": -2500.00, "data": "2026-07-05", "tipo": "pagar"}'
```

**Consultar a projeção de saldo para os próximos 30 dias:**
```bash
curl "http://127.0.0.1:8000/forecast?saldo_inicial=10000&dias=30"
```

## Próximos passos

- Persistência em banco de dados (PostgreSQL)
- Integração opcional com a API da Omie (contas a pagar/receber reais)
- Testes automatizados

## Licença

MIT
