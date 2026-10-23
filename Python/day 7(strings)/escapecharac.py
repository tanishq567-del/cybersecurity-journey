#b="I totally agree 
#but i still have my doubts"

#print(b)
# we wanted that this line to be print at down but i showed unterminated literal error so to avoid this 
# WE USE ESCAPE SEQUENCE CHARACTERS

b="I totally agree \nbut i still have my\tdoubts" #\n helps to give new line , \t helps to give tab space 
print(b)

# c="Sham is "very happy" today."  It will show error

c="Sham is \"very happy\" today"  # \" helps to give double quote in string"
print(c)
# d="Sham is 'very happy' today"  It will run 
# d='Sham is 'very happy' today' But not in this case
d='Sham is \'very happy\' today'
print(d)

#Some other escape characters'
a="Hello\\there" #print a backslash
print(a)
e="Yeme\bn" #uses backspace in string
print(e)
w="HELLO\rBYE" # carriage return- it take the word back to front replacing the characters in front with it 
print(w)