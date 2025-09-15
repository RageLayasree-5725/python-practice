#write a python program to print fibonacci series upto n
n=int(input("Enter a number"))
a=0
b=1
print(a)
print(b)
t=0
while t<=n-2:
    c=a+b
    print(c)
    a=b
    b=c
    t+=1
#using forloop
n=int(input("Enter a number"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c
