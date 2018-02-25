def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b , a + b

        
fib(5)
print()


# function with optional arguments 
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

       
# positioning arguments
print(ask_ok("confirm: ", 5))

# keyword arguments
print(ask_ok(retries=5, prompt="confirm: "))


# unknown count of arguments
def do_steps(*steps):
    for step in steps:
        print(step)

do_steps('one', 'two')


# unknown count of keyword arguments
def create_person(first_name, last_name, **infos):
    person = {"first_name":first_name, "last_name":last_name}
    for key, info in infos.items():
        person[key] = info
    return person


print(create_person("Uwe", "Sluga", living="WOB", profession="informatics"))
    
