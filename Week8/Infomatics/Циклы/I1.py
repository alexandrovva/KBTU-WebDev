n = int(input())
count = 0

for i in range(1, int(n ** 0.5) + 1):
    if n%i == 0:
        count+=1

if float(n ** 0.5)!=int(n ** 0.5):
    count = 2*count
else:
    count = 2*count - 1

print(count)