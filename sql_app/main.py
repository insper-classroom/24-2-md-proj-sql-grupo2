from fastapi import FastAPI, HTTPException

from . import crud, schemas

app = FastAPI()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user.model_dump())


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
