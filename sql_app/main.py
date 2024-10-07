from fastapi import FastAPI, HTTPException

from . import crud, schemas

app = FastAPI()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user.model_dump())
@app.post("/eventos/", response_model=schemas.Evento)
def create_evento(evento: schemas.EventoCreate):
    db_evento = crud.get_evento_by_nome(evento.nome)  # Usar a nova função de busca por nome
    if db_evento:
        raise HTTPException(status_code=400, detail="Evento already registered")
    return crud.create_evento(evento.model_dump())


@app.post("/tipos/", response_model=schemas.Tipo)
def create_tipo(tipo: schemas.TipoCreate):
    db_tipo = crud.get_tipo_by_nome(tipo.nome)  
    if db_tipo:
        raise HTTPException(status_code=400, detail="Tipo already registered")
    return crud.create_tipo(tipo.model_dump())
@app.post("/locais/", response_model=schemas.Local)
def create_local(local: schemas.LocalCreate):
    db_local = crud.get_local_by_nome(local.nome)  # Corrigido para buscar pelo nome
    if db_local:
        raise HTTPException(status_code=400, detail="Local already registered")
    return crud.create_local(local.model_dump())
@app.get("/eventos/", response_model=list[schemas.Evento])
def read_eventos(skip: int = 0, limit: int = 100):
    return crud.get_eventos(skip=skip, limit=limit)
@app.get("/tipos/", response_model=list[schemas.Tipo])
def read_tipos(skip: int = 0, limit: int = 100):
    return crud.get_tipos(skip=skip, limit=limit)
@app.get("/locais/", response_model=list[schemas.Local])
def read_locais(skip: int = 0, limit: int = 100):
    return crud.get_locais(skip=skip, limit=limit)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100):
    return crud.get_users(skip=skip, limit=limit)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    db_user = crud.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate):
    db_user = crud.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_item(user_id=user_id, item=item.model_dump())


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100):
    return crud.get_items(skip=skip, limit=limit)


# CRUD para Locais

@app.get("/locais/{local_id}", response_model=schemas.Local)
def read_local(local_id: int):
    db_local = crud.get_local(local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return db_local

@app.put("/locais/{local_id}", response_model=schemas.Local)
def update_local(local_id: int, local: schemas.LocalUpdate):
    db_local = crud.get_local(local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return crud.update_local(local_id, local.model_dump())

@app.delete("/locais/{local_id}", response_model=dict)
def delete_local(local_id: int):
    db_local = crud.get_local(local_id)
    if db_local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return crud.delete_local(local_id)

# CRUD para Eventos

@app.get("/eventos/{evento_id}", response_model=schemas.Evento)
def read_evento(evento_id: int):
    db_evento = crud.get_evento(evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return db_evento

@app.put("/eventos/{evento_id}", response_model=schemas.Evento)
def update_evento(evento_id: int, evento: schemas.EventoUpdate):
    db_evento = crud.get_evento(evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.update_evento(evento_id, evento.model_dump())

@app.delete("/eventos/{evento_id}", response_model=dict)
def delete_evento(evento_id: int):
    db_evento = crud.get_evento(evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    return crud.delete_evento(evento_id)

# CRUD para Tipos

@app.get("/tipos/{tipo_id}", response_model=schemas.Tipo)
def read_tipo(tipo_id: int):
    db_tipo = crud.get_tipo(tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo not found")
    return db_tipo

@app.put("/tipos/{tipo_id}", response_model=schemas.Tipo)
def update_tipo(tipo_id: int, tipo: schemas.TipoUpdate):
    db_tipo = crud.get_tipo(tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo not found")
    return crud.update_tipo(tipo_id, tipo.model_dump())

@app.delete("/tipos/{tipo_id}", response_model=dict)
def delete_tipo(tipo_id: int):
    db_tipo = crud.get_tipo(tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo not found")
    return crud.delete_tipo(tipo_id)