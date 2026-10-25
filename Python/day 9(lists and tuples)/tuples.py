#Tuples are same as list but they are immutable data type in python

a=(1,2,3,4,5) #tuple with mutiple elements
print(a)
print(type(a)) #<class 'tuple'>

b=() #empty tuple
print(b)

c=(9,) #tuple with only one element
print(c)

d=(1,3,5,7,9,"Shawn",True)
#d[3]=23# 'tuple' object does not support item assignment because tuple are immutable
print(d)

#TUPLEMETHODS

# In Python, tuples have only two built-in methods: count() and index(). Unlike lists, tuples are immutable, which means you cannot change, add, or remove their elements after creation.
# Why don't tuples have methods like append() or remove()?
# Because tuples are immutable. Their elements cannot be changed after creation.

e=d.count(3) #prints how many times the elements has appeared
print(e)

i=a.index(4) # prints the index of the given value
print(i)
