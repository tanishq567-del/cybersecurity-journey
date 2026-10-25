storage=["Apple","Banana",45,546.65,"Kamal",True,"Rohan"]
print(storage)
print(storage[0])
storage[0]="Grapes"
print("After changing the first input we get the new list as :",storage)#lists are mutable unlike strings means we can change the existing list instead of making new list


#HERE I USED REPL WE SEE THAT STRINGS ARE INMMUTABLE WHEREAS LISTS ARE MUTABLE
# >>> a="Tanishq"
# >>> a[0]
# 'T'
# >>> a[9]
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     a[9]
#     ~^^^
# IndexError: string index out of range
# >>> a[2]
# 'n'
# >>> a[3]=e
# Traceback (most recent call last):
#   File "<python-input-4>", line 1, in <module>
#     a[3]=e
#          ^
# NameError: name 'e' is not defined
# >>> a[3]="e"
# Traceback (most recent call last):
#   File "<python-input-5>", line 1, in <module>
#     a[3]="e"
#     ~^^^
# TypeError: 'str' object does not support item assignment
# >>> b=[tanishq]
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     b=[tanishq]
#        ^^^^^^^
# NameError: name 'tanishq' is not defined
# >>> b=["tanishq"]
# >>> b[4]="5"
# Traceback (most recent call last):
#   File "<python-input-8>", line 1, in <module>
#     b[4]="5"
#     ~^^^
# IndexError: list assignment index out of range
# >>> b[0]="234"
# >>> print(b)
# ['234']
# >>>


#LIST INDEXING
print(storage[0:3])#list slicing
print(storage[6])
#slicing negatively
print(storage[-3:-1])#prints [4:6]
print(storage[-7:-1])#prints[0:6]
print(storage[-1:-7])#prints[6:0]
print(storage[:3])
print(storage[0:])
print(storage[1:6:2])#slicing with skip value