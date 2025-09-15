#To find a number is palindrome or not
def is_palindrome(num: int):
    num=str(num)
    return str(num)==str(num[::-1])
number=int(input("Enter a number="))
if is_palindrome(number):
    print(f'{number} is palindrome')
else:
    print(f'{number} is not palindrome')
                         
