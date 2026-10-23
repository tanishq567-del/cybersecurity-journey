# Write a program to fill the letter template given below with name and data 
# letter='''Dear <|Name|>
# You are selected!
# <|Date|>'''

letter='''Dear <|Name|>\n\tYou are selected!\n<|Date|>'''
print (letter.replace("<|Name|>","Tanishq").replace("<|Date|>","23 October,2026")) # this is called chaining