import os
from app import app, custom_tag
from controllers import (
    get_all_items,
    create_item,
    read_item,
    update_item,
    delete_item
)
from models import Item, ItemsResponse
from print_info import print_info
from fastapi import UploadFile
from fastapi.responses import JSONResponse

UPLOAD_FOLDER = "uploads"

# Route to get all items
@app.get("/emp/", response_model=ItemsResponse, tags=[custom_tag])
def get_items():
    items = get_all_items()
    return ItemsResponse(data=items, message="Items retrieved successfully")

# Route to create an item
@app.post("/emp/", response_model=ItemsResponse, tags=[custom_tag])
def create_items(item: Item):
    newItem = create_item(item)
    return ItemsResponse(data=newItem, message="Items added successfully!")

# Route to read an item
@app.get("/emp/{item_id}", response_model=ItemsResponse, tags=[custom_tag])
def read_items(item_id: int):
    itemInfo = read_item(item_id)
    if itemInfo is None:
        return ItemsResponse(data=itemInfo, message="Get item info successfully!")
    else:
        return ItemsResponse(data=None, message="Item not found")

# Route to update an item
@app.put("/emp/{item_id}", response_model=ItemsResponse, tags=[custom_tag])
def update_items(item_id: int, item: Item):
    updateItem = update_item(item_id, item)
    return ItemsResponse(data=updateItem, message="Items updated successfully!")

# Route to delete an item
@app.delete("/emp/{item_id}", response_model=ItemsResponse, tags=[custom_tag])
def delete_items(item_id: int):
    itemInfo = delete_item(item_id)
    if itemInfo is None:
        return ItemsResponse(data=None, message="Deleted successfully!")
    else:
        return ItemsResponse(data=None, message="Item not found")

@app.post("/uploadfile/", response_model=None, tags=[custom_tag])
async def create_upload_file(file: UploadFile):
    # Create the uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Read the content of the uploaded file and write it to the destination file
    with open(file_path, "wb") as destination:
        destination.write(file.file.read())

    response = {
        "message": "File uploaded successfully",
        "filename": file.filename, 
    }
    return JSONResponse(content=response)

# Get configuration from environment variables
host = os.getenv("HOST")
port = int(os.getenv("PORT", 4000))

if __name__ == "__main__":
    print_info("FastAPI application started!")
    import uvicorn
    uvicorn.run(app, host=host, port=port)