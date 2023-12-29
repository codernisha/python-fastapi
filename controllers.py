from fastapi import HTTPException
from db_config import create_connection
from models import Item

# Initialize the database connection when the script is executed
conn = create_connection()

def get_all_items():
    try:
        with conn.cursor() as cursor:
            query = "SELECT id, name, email, phone, address FROM emp"
            cursor.execute(query)
            items = cursor.fetchall()
        return [
            {
                "id": item[0], 
                "name": item[1], 
                "email": item[2], 
                "phone": item[3], 
                "address": item[4]
            }
            for item in items
        ]
    except Exception as e:
        print(f"Error getting item list: {e}")
        raise HTTPException(status_code=400, detail=e)

def create_item(item: Item):
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO emp (name, email, phone, address) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (item.name, item.email, item.phone, item.address))
        conn.commit()
        return item
    except Exception as e:
        print(f"Error creating new item: {e}")
        raise HTTPException(status_code=400, detail=e)

def read_item(item_id: int):
    try:
        with conn.cursor() as cursor:
            query = "SELECT id, name, email, phone, address FROM emp WHERE id=%s"
            cursor.execute(query, (item_id,))
            item = cursor.fetchone()
        if item is None:
            return None
        return {
            "id": item[0], 
            "name": item[1], 
            "email": item[2], 
            "phone": item[3], 
            "address": item[4]
        }
    except Exception as e:
        print(f"Error getting specific item.id: {e}")
        raise HTTPException(status_code=400, detail=e)

def update_item(item_id: int, item: Item):
    try:
        with conn.cursor() as cursor:
            query = "UPDATE emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            cursor.execute(query, (item.name, item.email, item.phone, item.address, item_id))
        conn.commit()
        item.id = item_id
        return item
    except Exception as e:
        print(f"Error updating item.id: {e}")
        raise HTTPException(status_code=400, detail=e)

def delete_item(item_id: int):
    try:
        with conn.cursor() as cursor:
            query = "DELETE FROM emp WHERE id=%s RETURNING id"
            cursor.execute(query, (item_id,))
            deleted_id = cursor.fetchone()
        if deleted_id:
            conn.commit()
            return {
                'id': deleted_id[0]
            }
        else:
            return None
    except Exception as e:
        print(f"Error deleting item.id: {e}")
        raise HTTPException(status_code=400, detail=e)