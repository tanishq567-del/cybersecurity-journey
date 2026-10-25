# Check that tuple type cannot be changed in python 

a=("Tanishq",23,12,True)
# a[2]="Guru"
print(a)

# TypeError: 'tuple' object does not support item assignment
# Tuple is immutable so it cannot be changed


print(type(a))
