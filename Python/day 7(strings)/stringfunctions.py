name="Tanishq"
print(len(name))#len function prints the length of string
print(name.endswith("hq"))
print(name.endswith("la"))

name1="Yamraj"
print(name1.endswith("aj"))
print(name1.startswith("ya")) #as y is small we needed capital , as it is function case sensitive
print(name1.startswith("Ya"))
print(name.capitalize()) # capitalize first character of string

string="Hello World"
index=string.find("World") # finds the word in string and gives output as first character of the word's index
inde=string.find("world") #as first character is lowercase and python is case sensitive it will not find its word and will give output as -1
print(index)
print(inde)

s="Hi Friends"
replaced_string=s.replace("Friends","Guys") #replace the old word with new word in the entire string
print(replaced_string)
#it replaces all occurences in the string

s="Hi I am very very glad to meet you all"
replace=s.replace("very","so") 
print(replace)

r="India"
print(r.upper()) #make all characters of word uppercase
print(r.lower()) #make all characters of word lowercase
y="ye mera india"
print(y.title()) #make every word first character capital
print(s.split()) #split words of string to form list
q="           hji          "
print(q.strip())  #remove spaces from both ends
print(s.find("y")) #finds the first occurence position of character
print(s.count("a")) #count all the occurences of particular input value
print(r.isalpha()) #checks whether all characters are letters
print(r.isdigit())
e="123456"
print(e.isdigit()) # checks whether all characters are digit