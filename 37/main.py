from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI App",
    version="1.0.0"
)

@app.get("/products")
def read_root():
    return {"message": "Products received successfully"}

@app.post("/products")
def create_product():
    return {"message": "Product created"}

@app.put("/products/{product_id}")
def update_product(product_id: int):
    return {"message": f"Product {product_id} updated"}

@app.patch("/products/{product_id}")
def patch_product(product_id: int):
    return {"message": f"Product {product_id} patched"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {"message": f"Product {product_id} deleted"}