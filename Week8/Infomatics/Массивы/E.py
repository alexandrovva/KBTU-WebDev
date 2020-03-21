n = int(input())
x = list(map(int, input().split()))
count = 0

for i in range(n-1):
    if (x[i]>0 and x[i+1]>0) or (x[i]<0 and x[i+1]<0):
        count+=1
        break
if count>0:
    print('YES')
else:
    print('NO')