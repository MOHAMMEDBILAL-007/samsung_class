#recursion
def factorial(x):
    if x == 0 or x == 1 : #base condition 
        return 1
    else:
        return x*factorial(x-1)
print(factorial(4))
def fibonacci(x):
    if x<= 0:
        return 0
    elif x==1:
        return 1
    else :
        return fibonacci(x-1)+fibonacci(x-2)
for i in range(10):
    print(fibonacci(i))