def pn(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    else:
        return False
n=int(input())
print(pn(n))