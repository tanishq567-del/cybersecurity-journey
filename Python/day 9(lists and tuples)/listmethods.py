fruits=["Apple","Banana","Litchi","Tomato","Pineapple","Watermelon","Mango"]
print(fruits)

#1
print(fruits.append("Papaya"))#Why? Because append() adds "Papaya" to the list but returns None. #It add item to end of the list
print(fruits)

#2
list23=[1,43,543,2,313,6,54,34,87,654,886,999,0]
#list23.sort() #It sorts the list in ascending order
print(list23)

#3
#list23.reverse()
print(list23) #It reverses the given list from last to first but not in descending order

#4
list23.insert(5,8.00120) # this helps to insert value at entered index number and replace it with other entered number by user
print(list23)

#5
l1=[23,34,45,56,67,78,89]
#l1.pop(3) #it pops/remove the indexed value from the list
print(l1)

print(l1.pop(4)) # it will print the value that will be poped out
print(l1) # I have to use this print(l1) again or it will not print updated this

#6
#l1.remove(3) # list.remove(x): x not in list ,,,This error will come because remove() removes an item by its value. pop() removes an item by its index and returns the removed value.
l1.remove(45)
print(l1)

#7
l1.extend([1,2,3,4,5,6,7,8,9,0]) #Pass all the values inside a single list using square brackets []. #extend adds multiple values to the list
print(l1)

#8
l1.clear() #removes all items from the list
print(l1)

l1.extend([1,2,3,4,5,6,7,8,9])
print(l1)

#9
l2=l1.copy() #copies all the items in one list to another
print(l2)

#10
l3=[1,1,1,2,3,4,5,6,77,88,77,88,66,78,89,9]
print(l3.count(1)) #it counts the number of occurences the specific value has appeared

print(l3.index(6)) #returns the index of value
print(l3.index(1)) #it only returns the first occurence of the value given

