# name=input("Enter your name")
# print("good afternoon\t"+name)
# 
# 
letter = ''' Hello Mr <|NAME|> your last recharge was successful <|DATE|> with the racharge of 399 in jio and it will be end on <|ENDDATE|> thank team jio'''
name = input("enter your name")
date = input("enter date when recharge was successful")
enddate = input("enter enter the date when recharge will be ended thank you team jio")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
letter = letter.replace("<|ENDDATE|>",enddate)
print(letter)
