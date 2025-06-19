from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the request model
class Numbers(BaseModel):
    num1: float
    num2: float

# Define the route for addition
@app.post("/add")
def add_numbers(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}
