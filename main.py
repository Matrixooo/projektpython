from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Simple FastAPI CRUD example")



class ItemBase(BaseModel):
    name: str = Field(..., example="Przykładowy przedmiot")
    description: Optional[str] = Field(None, example="Opis przedmiotu")

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: Optional[str] = None
    description: Optional[str] = None

class Item(ItemBase):
    id: int



db: Dict[int, Item] = {}
next_id = 1

def _get_next_id() -> int:
    global next_id
    nid = next_id
    next_id += 1
    return nid


@app.get("/items", response_model=List[Item])
def get_items():
    return list(db.values())

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item_in: ItemCreate):
    item_id = _get_next_id()
    item = Item(id=item_id, **item_in.dict())
    db[item_id] = item
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_in: ItemUpdate):
    stored = db.get(item_id)
    if not stored:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    updated_data = stored.dict()
    update_fields = item_in.dict(exclude_unset=True)
    updated_data.update(update_fields)

    updated = Item(**updated_data)
    db[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del db[item_id]
    return None
