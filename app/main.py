from fastapi import FastAPI
from tests.isPrime import is_prime
from tests.getFiboNumber import get_fibo_number

app = FastAPI()


@app.get("/hello")
async def hello():
    return "Hello FastAPI"

@app.get("/is-prime/{number}")
def check_is_prime(number: int):
    if is_prime(number):
        return 'No es numero primo'
    return 'Es numero primo'

@app.get("/fibonacci/{position}")
def get_number(position: int):
    return {'Posición': position, 'Número': get_fibo_number(position)}