a=44
t=type(a) #class<int>
print(t)

b =3.32
t=type(b)
print(t)

c="Tanishq"
t=type(c)
print(t)

d="3.32" #it will be treated as string only
t=type(d)
print(t)

e="32.34"
f=float(e)
t=type(f)
print(t)

#Input Function
z=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
print("Number 1 is: ",z)
print("Number 2 is: ",y)
print(("Sum of the entered numbers is: ") ,z+y)




