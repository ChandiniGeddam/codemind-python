N=int(input())
i=0
while N>0:
    r=N%10
    N=N//10
    if r>i:
        i=r
print(i)
        
