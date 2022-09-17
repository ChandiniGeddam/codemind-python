n=int(input())
c=0
s=0
while n>0:
    r=n%10
    if r%2==0:
        c+=1
    elif r%2!=0:
        s+=1
    n=n//10
if s==0:
    print("Even")
elif c==0:
    print("Odd")
else:
    print("Mixed")
