from turtle import update


dict = {
    "rajneesh":" Is a coder", "Apple":"it is an American company populor for iphones which provide features..."
   
}

#methods in dictionary
print(dict.keys()) #it will help to print the keys mentioned in dictionary
print(list(dict.keys()))
print(dict.values()) #it will print the all vaules in the  keys
print(dict.items()) #it will print the keys and value of dictionary
updatedict = {
            "shubhham":"friend", "mayank":"friend","akshay":"brother"
 }
dict.update(updatedict) #this is can upodate the  dictionary
print(dict)

print(dict.get("rajneesh3")) # returns non as rajneesh3 is not persent in the dictionary
#print(dict["rajneesh3"]) #this is will throw an error in the dictionary 