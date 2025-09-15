num=int(input("Enter a number="))
original_num=num

r=num%10
a1=r**3
q=(num//10)%10
a2=q**3
q1=num//100
a3=q1**3
armstrong_num=a1+a2+a3
print(original_num)
print(armstrong_num)
if(armstrong_num==original_num):
    print(f"Given number {original_num} is Armstrong number")
else:
    print("Given number is not armstrong number")



