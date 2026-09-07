from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
from fastapi import FastAPI, HTTPException, status


products = []


class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    discount_price: float | None = Field(None, gt=0)
    quantity: int = Field(ge=0)
    category: str = Field(min_length=1, max_length=20)
    sku: str = Field(min_length=5, max_length=20)
    email: EmailStr
    stock: bool = Field(default=True)

    @field_validator("name")
    @classmethod
    def check_spaces(cls, value: str):
        return value.strip()

    @field_validator("sku")
    @classmethod
    def check_sku(cls, value: str):
        if " " in value:
            raise ValueError("SKU must not contain spaces")
        if value.upper() in [product.sku for product in products]:
            raise ValueError("SKU must be unique")
        return value.upper()

    @model_validator(mode="after")
    def check_discount_price(self):
        if self.discount_price is not None and self.discount_price >= self.price:
            raise ValueError("Discount price must be less than the regular price")
        return self


class ProductResponse(BaseModel):
    name: str
    price: float
    discount_price: float | None
    quantity: int
    category: str
    stock: bool

app = FastAPI(
    title="Product API",
    version="1.0.0"
)

@app.post("/products/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    products.append(product)
    return product

@app.get("/products/{sku}", response_model=ProductResponse)
def get_product(sku: str):
    for product in products:
        if product.sku == sku:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
