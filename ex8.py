def power(a,b,mod):
    return (a**b)%mod
n=int(input("enter q:"))
g=int(input("enter a:"))
x=int(input("enter XA:"))
y=int(input("enter XB:"))
a=power(g,x,n)
b=power(g,y,n)
p=power(b,x,n)
q=power(a,y,n)
if(p==q):
    print("Exchange is done and Secret Key is : ",p)
else:
    print("Invalid Key.")
