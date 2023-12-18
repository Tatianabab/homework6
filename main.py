import time
def calculate_time(func):
    def wrapper(*args):
        g = time.time()
        func(*args)
        k = time.time()
        print(k-g)
    return wrapper
@calculate_time
def some_function(a):
    return list(range(1, a+1))
a = int(input("Введите число:"))
b = some_function(a)
print(b)






