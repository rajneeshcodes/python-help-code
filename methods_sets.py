#methods in set
#adding values in empty set
b=set()
b.add(4)
b.add(3)
b.add(5)
b.add(5)
b.add(6)
b.add(6)
print(len(b)) #it will print the lengh of the set
b.remove(4) #it will remove the element
print(b)



#you can't add dictionary and list in the set beacause its not hashable in the sets in python
#b.add({4:5})
#b.add

# Propereties in sets
#set is unodered you can't access a element by its order
#you can't change the items
#sets don't contian duplicate value