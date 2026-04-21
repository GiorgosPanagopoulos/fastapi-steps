from fastapi import FastAPI

#https://127.0.0.1:8000/docs

# Create the FastAPI application instance
app = FastAPI(
  title="Hello FastAPI",
  description="Our first FastAPI application",
  version="1.0.1"
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Read a single item by its ID.
    The type hit `int` telss FastAPI to:
    1. Validate that item_id is an integer.
    2. Convert the string from url to an int.
    3. Return 422 if validation fails.
    """

    return {
      "item_id" : item_id,
      "name" : f"Item #{item_id}"
  }