story ='a millions of time ago there was a tiger he was runnig behind the hare so fast'
#string functions

#len
print(len(story))
#endswith
print(story.endswith("fast"))

print(story.endswith("more")) #the sentence given above is not ending with the more so it will print the false
print(story.count("a")) #it will count the particullar alphabet in an given array and show the how many times those are repeated

print(story.count("i"))

#capitalize,, this function capitalize the starting single word present in an string 
print(story.capitalize())
print(story.find("tiger"))
print(story.replace("a millions of time ago","once upon a time"))