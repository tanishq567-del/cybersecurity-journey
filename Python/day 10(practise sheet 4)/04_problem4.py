# Write a program to sum the list of 4 numbers of a list 

l=[1,3,5,6]
print(sum(l))

s=[]
number1=int(input("Enter 1st number:"))
s.append(number1)
number2=int(input("Enter 2nd number:"))
s.append(number2)
number3=int(input("Enter 3rd number:"))
s.append(number3)
number4=int(input("Enter 4th number:"))
s.append(number4)

print("The sum of the 4 numbers that you have entered is",sum(s))