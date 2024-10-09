from fastapi import FastAPI, HTTPException

from . import crud, schemas

app = FastAPI()


################################################### CRUD para Locais ###################################################


@app.post("/locais/", response_model=schemas.Local, tags=["Locais"])
def create_local(local: schemas.LocalCreate):
    db_local = crud.get_local_by_nome(local.nome)  # Corrigido para buscar pelo nome
    if db_local:
        raise HTTPException(status_code=400, detail="Local already registered")
    return crud.create_local(local.model_dump())


@app.get("/locais/", response_model=list[schemas.Local], tags=["Locais"])
def read_locais(skip: int = 0, limit: int = 100):
    return crud.get_locais(skip=skip, limit=limit)


@app.get("/locais/{local_id}", response_model=schemas.Local, tags=["Locais"])
def read_local(local_id: int):
    db_local = crud.get_local(local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return db_local


@app.put("/locais/{local_id}", response_model=schemas.Local ,tags=["Locais"])
def update_local(local_id: int, local: schemas.LocalUpdate):
    db_local = crud.get_local(local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return crud.update_local(local_id, local.model_dump())


@app.delete("/locais/{local_id}", response_model=dict, tags=["Locais"])
def delete_local(local_id: int):
    db_local = crud.get_local(local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return crud.delete_local(local_id)


#########################################################################################################################


################################################### CRUD para Eventos ###################################################


@app.post("/eventos/", response_model=schemas.Evento,tags=["Eventos"])
def create_evento(evento: schemas.EventoCreate):
    db_evento = crud.get_evento_by_nome(evento.nome)
    if db_evento:
        raise HTTPException(status_code=400, detail="Evento already registered")
    return crud.create_evento(evento.model_dump())


@app.get("/eventos/", response_model=list[schemas.Evento], tags=["Eventos"])
def read_eventos(skip: int = 0, limit: int = 100):
    return crud.get_eventos(skip=skip, limit=limit)


@app.get("/eventos/{evento_id}", response_model=schemas.Evento, tags=["Eventos"])
def read_evento(evento_id: int):
    db_evento = crud.get_evento(evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return db_evento


@app.put("/eventos/{evento_id}", response_model=schemas.Evento, tags=["Eventos"])
def update_evento(evento_id: int, evento: schemas.EventoUpdate):
    db_evento = crud.get_evento(evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.update_evento(evento_id, evento.model_dump())


@app.delete("/eventos/{evento_id}", response_model=dict, tags=["Eventos"])
def delete_evento(evento_id: int):
    db_evento = crud.get_evento(evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.delete_evento(evento_id)


#######################################################################################################################


################################################### CRUD para Tipos ###################################################


@app.post("/tipos/", response_model=schemas.Tipo, tags=["Tipos"])
def create_tipo(tipo: schemas.TipoCreate):
    db_tipo = crud.get_tipo_by_nome(tipo.nome)
    if db_tipo:
        raise HTTPException(status_code=400, detail="Tipo already registered")
    return crud.create_tipo(tipo.model_dump())


@app.get("/tipos/", response_model=list[schemas.Tipo], tags=["Tipos"])
def read_tipos(skip: int = 0, limit: int = 100):
    return crud.get_tipos(skip=skip, limit=limit)


@app.get("/tipos/{tipo_id}", response_model=schemas.Tipo, tags=["Tipos"])
def read_tipo(tipo_id: int):
    db_tipo = crud.get_tipo(tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo not found")
    return db_tipo


@app.put("/tipos/{tipo_id}", response_model=schemas.Tipo, tags=["Tipos"])
def update_tipo(tipo_id: int, tipo: schemas.TipoUpdate):
    db_tipo = crud.get_tipo(tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo not found")
    return crud.update_tipo(tipo_id, tipo.model_dump())


@app.delete("/tipos/{tipo_id}", response_model=dict, tags=["Tipos"])
def delete_tipo(tipo_id: int):
    db_tipo = crud.get_tipo(tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo not found")
    return crud.delete_tipo(tipo_id)


#######################################################################################################################
