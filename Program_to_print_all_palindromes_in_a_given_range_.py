a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    t=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==t:
        print(t,end=' ')
