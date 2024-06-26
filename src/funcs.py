from typing import Generator
from math import sqrt, factorial

def divisors(n: int) -> Generator:
    for x in range(1, int(sqrt(n))+1):
        if x == sqrt(n):
            yield x
        elif n % x == 0:
            yield x
            if x != 1:
                yield n//x

def primeNumbers() -> Generator:
    yield 2
    num = 1
    while True:
        num += 2
        prime = True
        for i in range(3, int(sqrt(num))+1, 2):
            if not num % i:
                prime = False
        if prime:
            yield num

def collatz(start: int) -> Generator:
    yield start
    while start != 1:
        if start % 2 == 0:
            start = start // 2
            yield start
        else:
            start *= 3
            start += 1
            yield start

def fibonacci(start: tuple=(1, 0)) -> Generator:
    a, b = start
    while True:
        a, b = b, a + b
        yield b

def choice(n: int, k: int) -> float:
    return factorial(n) / (factorial(k) * factorial(n-k))

def amicableNumbers() -> Generator:
    num = 1
    while True:
        divSum = sum(divisors(num))
        if divSum != num and num == sum(divisors(divSum)):
            yield num
        num += 1