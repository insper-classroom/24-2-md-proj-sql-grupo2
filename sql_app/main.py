from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# Criando as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


################################################### CRUD para Locais ###################################################

@app.post("/locais/", response_model=schemas.Local, tags=["Locais"])
def create_local(local: schemas.LocalCreate, db: Session = Depends(get_db)):
    db_local = crud.get_local_by_nome(db, local.nome)
    if db_local:
        raise HTTPException(status_code=400, detail="Local já registrado")
    return crud.create_local(db, local.model_dump())


@app.get("/locais/", response_model=list[schemas.Local], tags=["Locais"])
def read_locais(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_locais(db, skip=skip, limit=limit)


@app.get("/locais/{local_id}", response_model=schemas.Local, tags=["Locais"])
def read_local(local_id: int, db: Session = Depends(get_db)):
    db_local = crud.get_local(db, local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local não encontrado")
    return db_local


@app.put("/locais/{local_id}", response_model=schemas.Local, tags=["Locais"])
def update_local(local_id: int, local: schemas.LocalUpdate, db: Session = Depends(get_db)):
    db_local = crud.get_local(db, local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local não encontrado")
    return crud.update_local(db, local_id, local.model_dump())


@app.delete("/locais/{local_id}", response_model=dict, tags=["Locais"])
def delete_local(local_id: int, db: Session = Depends(get_db)):
    db_local = crud.get_local(db, local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local não encontrado")
    return crud.delete_local(db, local_id)


########################################################################################################################


################################################### CRUD para Eventos ###################################################


@app.post("/eventos/", response_model=schemas.Evento, tags=["Eventos"])
def create_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    db_evento = crud.get_evento_by_nome(db, evento.nome)
    if db_evento:
        raise HTTPException(status_code=400, detail="Evento já registrado")
    return crud.create_evento(db, evento.model_dump())


@app.get("/eventos/", response_model=list[schemas.Evento], tags=["Eventos"])
def read_eventos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_eventos(db, skip=skip, limit=limit)


@app.get("/eventos/{evento_id}", response_model=schemas.Evento, tags=["Eventos"])
def read_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = crud.get_evento(db, evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return db_evento


@app.put("/eventos/{evento_id}", response_model=schemas.Evento, tags=["Eventos"])
def update_evento(evento_id: int, evento: schemas.EventoUpdate, db: Session = Depends(get_db)):
    db_evento = crud.get_evento(db, evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return crud.update_evento(db, evento_id, evento.model_dump())


@app.delete("/eventos/{evento_id}", response_model=dict, tags=["Eventos"])
def delete_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = crud.get_evento(db, evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return crud.delete_evento(db, evento_id)


#######################################################################################################################


################################################### CRUD para Tipos ###################################################


@app.post("/tipos/", response_model=schemas.Tipo, tags=["Tipos"])
def create_tipo(tipo: schemas.TipoCreate, db: Session = Depends(get_db)):
    db_tipo = crud.get_tipo_by_nome(db, tipo.nome)
    if db_tipo:
        raise HTTPException(status_code=400, detail="Tipo já registrado")
    return crud.create_tipo(db, tipo.model_dump())


@app.get("/tipos/", response_model=list[schemas.Tipo], tags=["Tipos"])
def read_tipos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tipos(db, skip=skip, limit=limit)


@app.get("/tipos/{tipo_id}", response_model=schemas.Tipo, tags=["Tipos"])
def read_tipo(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = crud.get_tipo(db, tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")
    return db_tipo


@app.put("/tipos/{tipo_id}", response_model=schemas.Tipo, tags=["Tipos"])
def update_tipo(tipo_id: int, tipo: schemas.TipoUpdate, db: Session = Depends(get_db)):
    db_tipo = crud.get_tipo(db, tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")
    return crud.update_tipo(db, tipo_id, tipo.model_dump())


@app.delete("/tipos/{tipo_id}", response_model=dict, tags=["Tipos"])
def delete_tipo(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = crud.get_tipo(db, tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")
    return crud.delete_tipo(db, tipo_id)

#######################################################################################################################