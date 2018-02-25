# list
numbers = [1, 2, 3, 4]
print(numbers)
print(numbers[0:3])

numbers.insert(4, 5)
print(numbers)

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

print("max is " + str(max(numbers)))
print(len(numbers))

del(numbers[0:1])
print(numbers)

names = ["uwe", "anton", "anni"]
names.insert(3, "sabine")
print(names)
names[3] = "SABINE"
print(names)
print(names.pop())
print(names)
del names[0]
print(names)

# tuple
tuples = ("one", "two", "three", "four", "one")
print(tuples)
print(tuples[0:3])
print(tuples.count("one"))

for tuple in tuples:
    print(tuple) 
    
for index in range(0, 4):
    print(tuples[index])

# dictionary
person_0 = {'first_name':'Uwe', 'last_name':'Sluga', 'hobbies':["diving", "sailing"]}
person_1 = {'first_name':'Anton', 'last_name':'Sluga', 'hobbies':["programing", "running"]}
persons = (person_0, person_1)
print(persons[0:2])
# add attribute
person_0['attr1'] = 'added'
print(persons[0])

for key in person_0.keys():
    print(key)
    
for value in person_0.values():
    print(value)  
    
for item in person_0.items():
    print(item)    

