n = int(input())
x = list(map(int, input().split()))
count = 0

for i in range(n):
    if x[i]>0:
        count+=1
print(count)