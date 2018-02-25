def read(fileName):
    try:
        with open(fileName) as file:
            contents = file.read()
    except:
        FileNotFoundError
        contents = ""
    return contents
    
print(read("text.txt"))
    
