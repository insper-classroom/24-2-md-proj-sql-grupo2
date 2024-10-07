# dicionários para armazenar dados temporários
from .database import users_db, user_id_counter, items_db, item_id_counter


def get_user(user_id: int):
    if user_id < 0 or user_id > len(users_db):
        raise ValueError("User ID is out of range")

    # Se users_db for um dicionário
    if user_id not in users_db:
        raise ValueError("User not found")

    return users_db[user_id]


def get_user_by_email(email: str):
    for user in users_db.values():
        if user["email"] == email:
            return user
    return None


def get_users(skip: int = 0, limit: int = 100):
    return list(users_db.values())[skip : skip + limit]


def create_user(user: dict):
    global user_id_counter
    new_user = {
        "id": user_id_counter,
        "email": user["email"],
        "hashed_password": user["password"] + "notreallyhashed",
        "is_active": True,
        "items": [],
    }
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    return new_user


def get_items(skip: int = 0, limit: int = 100):
    return list(items_db.values())[skip : skip + limit]


def create_user_item(user_id: int, item: dict):
    global item_id_counter
    new_item = {
        "id": item_id_counter,
        "title": item["title"],
        "description": item.get("description", None),
        "owner_id": user_id,
    }
    items_db[item_id_counter] = new_item
    users_db[user_id]["items"].append(new_item)
    item_id_counter += 1
    return new_item
