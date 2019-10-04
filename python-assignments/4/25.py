def func(a,b):
    ans = 0
    try:
        ans = (a+b)/(a-b)
    except ZeroDivisionError:
        print("Division by Zero Error")
    except:
        print("Error")
    else:
        print("No Errors")
    finally:
        return ans

print(func(5,5))
print()
print(func(5,'5'))
print()
print(func(5,3))