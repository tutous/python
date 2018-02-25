name = str(input("write your name:"))
print("welcome: " + name)

parents = ["uwe", "sabine"]
childs = ["anton", "anni"]

if name in parents:
    print(name + " has to do some work")
elif name in childs:
    print(name + " please make a break")
else:
    print("you are not in the family")
   

# boolean + and/or 
value = True
if value and 1 == 1:
    print("true")
    
if value or 1 == 2:
    print("true")    

