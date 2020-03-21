a = int(input())

def my_function(a):
    count = 0
    while a>0:
        count+=1
        a = a//10
    if count%2==0:
        print("Beautiful number")
    else:
        print("Foo")

my_function(a)


