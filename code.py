def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before calling the function.")
        result=func(*args,**kwargs)
        print("After calling the function.")
        return result

    return wrapper


# Applying the decorator to a function
@decorator
def greet(a,b):
     print(f"hello,{a, b}")
     return a+b
c=greet(4,6)
print(c)