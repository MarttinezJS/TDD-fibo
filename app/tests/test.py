from isPrime import is_prime
from getFiboNumber import get_fibo_number

def test_is_prime():
    assert is_prime(2) == False

def test_fibonacci():
    assert get_fibo_number(7) == 13