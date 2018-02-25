# simple
message = 'Uwe is learning Python '
print('\'' + message.title() + '\'')

# delete space
print('\'' + message.strip()  + '\'')

# concatenate
first_name = "Uwe"
last_name = "Sluga"
full_name = first_name + " " + last_name
print(full_name)

# as function with default parameter
def print_full_name(first_name, last_name, middle_name="",upper_case=""):
    """ print the full name """
    full_name = ""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name;
    else:
        full_name = first_name + " " + last_name
    if upper_case == "upper":
        print(full_name.upper())
    else:
        print(full_name)
    return full_name


print_full_name(first_name, last_name)
print_full_name(first_name="Anni", last_name="Sluga")
print_full_name("Anton", "Sluga", "Moritz","upper")

