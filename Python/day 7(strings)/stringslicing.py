#index slicing
name="Tanishq"
nameshort=name[0:3]
print(nameshort)
character1=name[1]
print(character1)

name2="Samsung"
character2=name2[4]
print(character2)

sl=name2[1:3]
print(sl)

#negative index slicing
name3="JammuKashmir"
print(name3[0:3])
print(name3[-4:-1])#simply convert negative indices to negative indices
print(name3[8:11])#this is positive indexing : -4=8,-1=11

#other slicing techniques
word="amazing"
print(word[:7])#print same as (0:7)
print(word[0:])#print same as (0:7)

#slicing with skip value
wordie="amazingzingzing"
print(wordie[1:12:2])#here we see it count the characters from 1=m and 12=i,where it take value by skipping 2 values 
print(wordie[1:8:3])
