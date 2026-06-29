# Backend Sistema de Gestão Financeira

API REST em Python (FastAPI) para um sistema de gestão financeira simples: cadastro de clientes, fornecedores, categorias, e controle de contas a pagar e a receber.

## O problema

Pequenas e médias empresas frequentemente gerenciam contas a pagar e a receber em planilhas, sem um sistema centralizado que relacione esses lançamentos a clientes, fornecedores e categorias de forma estruturada. Este projeto constrói essa base: um backend com modelagem relacional real, pronto para servir um frontend de gestão financeira.

Este é o backend do sistema — o [frontend](https://github.com/DiegoAlexandres/frontend-sistema-gestao-financeira) (Next.js) consome esta API para oferecer as telas de cadastro e visualização.

## Modelagem

- **Cliente** — quem paga (relacionado a Conta a Receber)
- **Fornecedor** — quem recebe (relacionado a Conta a Pagar)
- **Categoria** — classificação de lançamentos (ex: Aluguel, Vendas, Impostos), compartilhada entre os dois tipos de conta
- **Conta a Receber** — lançamentos a receber de um cliente, com data de emissão, vencimento e pagamento
- **Conta a Pagar** — lançamentos a pagar a um fornecedor, com a mesma estrutura de datas

## Stack

- **Python 3.14**
- **FastAPI** — framework web e validação de dados
- **PostgreSQL 18** — banco de dados relacional (via Docker em desenvolvimento)
- **SQLAlchemy** — ORM
- **Uvicorn** — servidor ASGI
- **uv** — gerenciamento de dependências e ambiente

## Como rodar

```bash
git clone https://github.com/DiegoAlexandres/backend-sistema-gestao-financeira.git
cd backend-sistema-gestao-financeira
docker compose up -d
uv sync
uv run uvicorn src.main:app --reload
```

Acesse a documentação interativa em [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) para testar as rotas direto no navegador.

## Próximos passos

- CRUD completo de Cliente, Fornecedor e Categoria
- CRUD completo de Conta a Receber e Conta a Pagar, com relacionamento via chave estrangeira
- Rota de saldo consolidado
- Testes automatizados
- Deploy em ambiente de produção (Neon)

## Licença

MIT