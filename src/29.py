from itertools import product

print(len(set(a**b for a, b in product(range(2, 101), repeat=2))))