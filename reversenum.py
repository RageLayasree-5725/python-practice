num=int(input("Enter a number:"))
reverse=0
original=num
while num!=0:
    remainder = num%10
    reverse=reverse*10+remainder
    num=num//10
print(f"Reverse of {original}={reverse}")
