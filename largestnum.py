num1=int(input('Enter a 1st number:'))
num2=int(input('Enter a 2nd number:'))
num3=int(input('Enter a 3rd number:'))
if num1>num2 & num1>num3:
    print('1st number is largest.')
elif num2>num1:
    print('2nd number is largest.')
else:
    print('3rd number is largest.')