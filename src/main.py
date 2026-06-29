from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models.clientes import Cliente, ClienteCreate, ClienteUpdate, ClienteOut

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão Financeira")


@app.get("/clientes", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()