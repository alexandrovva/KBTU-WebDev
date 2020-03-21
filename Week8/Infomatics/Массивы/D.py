n = int(input())
x = list(map(int, input().split()))
count = 0

for i in range(1, n):
    if x[i]>x[i-1] :
        count+=1
print(count)