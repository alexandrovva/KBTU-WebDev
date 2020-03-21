n = int(input())
a = list(map(int, input().split()))
s = ''

for i in range(n-1, -1, -1):
    s+=str(a[i]) + ' '

print(s)