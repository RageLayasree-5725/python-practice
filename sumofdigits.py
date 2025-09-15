#sum of digits
num=int(input("enter a number"))
sum=0
original=num
while num!=0:
    remainder=num%10
    sum=sum+remainder
    num=num//10
print(f"Sum of digits in given number {original} is {sum}")

    
