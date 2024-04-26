import math
n = 600851475143
while n % 2 == 0:
    print(2)
    n = n / 2
for i in range(3, int(math.sqrt(n))+1, 2):
    while n % i == 0:
        print(i)
        n = n / i
if n > 2:
    print(n)