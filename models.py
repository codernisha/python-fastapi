# models.py

from pydantic import BaseModel
from typing import List, Union

class Item(BaseModel):
    id: int = None
    name: str
    email: str
    phone: str = None
    address: str = None

class ItemsResponse(BaseModel):
    message: str
    data: Union[Item, List[Item], None]