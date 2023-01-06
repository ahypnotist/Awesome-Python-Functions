#this is a function that, when given a character, tells you its place in a specific list

#this function is meant to be used with an iterable

def ev(x):
    n = x.index(i)
    return n


#A demonstration of this function.

#This is our list. It includes 3 different strings.    
list1 = ["A", "B", "C"]

#This is a string. It could also be a list. It has to be a iterable.
string = "B"

#I do not know where B is in the list. This function will find its place.

for i in string:
    stringplace = ev(list1)

#B is the second item, so its place is 1
print(stringplace)
