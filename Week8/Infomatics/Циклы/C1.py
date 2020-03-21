import math
a = int(input())
b = int(input())

sqrt_a = int(math.ceil(math.sqrt(a)))
sqrt_b = int(math.sqrt(b))
for i in range(sqrt_a, sqrt_b+1):
    print(i*i)