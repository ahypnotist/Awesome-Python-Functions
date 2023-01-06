#this is a function I made
#It gets the first item of a list and puts it at the end
#"lst" is the list, and "number" is the number of times you do it

def puf(lst, number):
    for i in range(number):
        added = lst[0]
        lst.pop(0)
        lst.append(added)