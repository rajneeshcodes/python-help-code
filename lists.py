#python list are the container to store the values of any type of data
# friends = ['akash','praveen','akshay','amit']
a = [2,34,22,23,51,12,23]
# print(a[0]) #it will print the whole list 
a[0]= 34 #also we can change the value of an list like this we changed
print(a)

#We can create a list with the defferent type of data types in the python
#for example here given blow.....
list = ['Meerut', 23111,False,34.4] 
print(list)



# List slicing

friends = ["rajneesh","harsh","vardhan","90"]
print(friends[0:3])
print(friends[-3: ])

#list methods
li = [1,2,12,4,6,4,3]
li.sort() #it will sort the list in ascending order
print(li)
#reverse
li.reverse() #it can reverse the element in the given array
print(li)
#append
li.append(23) #Meaning of append is to add any value at end of the string or a list array as in this function this will add the 23 in the list which is given above in program.
print(li) 
#insert
li.insert(2,44) #it has ablity to insert the particular element on the given index.
print(li)

#pop
li.pop(3) #it will pop the element from index number 3
print(li)
#REMOVE

li.remove(44) #it will remove the element 
print(li)

#entering the fruit list in a list
f1 =input("Enter the fruit name 1 = ")
f2 =input("Enter the fruit name 2 = ")
f3 =input("Enter the fruit name 3 = ")
f4 =input("Enter the fruit name 4 = ")
f5 =input("Enter the fruit name 5 = ")
f6 =input("Enter the fruit name 6 = ")
f7 =input("Enter the fruit name 7 = ")
f8 =input("Enter the fruit name 8 = ")
f9 =input("Enter the fruit name 9 = ")
myfruitlist =[f1,f2,f3,f4,f5,f6,f7,f8,f9]
print(myfruitlist)