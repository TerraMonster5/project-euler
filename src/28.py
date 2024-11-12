from funcs import A316667

spiral = {tup: num for num, tup in A316667(1001**2)}

diagonals = set()

for i in range(501):
    diagonals.add(spiral[(i, i)])
    diagonals.add(spiral[(i, -i)])
    diagonals.add(spiral[(-i, i)])
    diagonals.add(spiral[(-i, -i)])

print(sum(diagonals))