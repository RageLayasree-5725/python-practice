#program to find factorial of a number
def factorial(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result
number=int(input("Enter a number="))
factorial(number)
print(f"factorial of {number} is {factorial(number)}")
