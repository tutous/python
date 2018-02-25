def div(paramOne, paraTwo, error=-1):
    result = 0
    tmpResult = result
    try:
        tmpResult = paramOne / paraTwo
    except:
        ZeroDivisionError
        result = error
        print("You can't divide by zero!")
    else:
        """ try was successful"""
        result = tmpResult
    return result

print(div(1, 1))
print(div(1, 0))
print(div(1, 0, -2))
