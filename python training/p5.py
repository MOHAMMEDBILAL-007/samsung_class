# a = int(input("entare the number to print its math table :"))
# for i in range(1,11):
#     print("%2d * %2d = %3d"%(a,i,a*i))
try:
    print("hello")
    print(2/0)
    print("bye")
except Exception as a:
    print("an error occured")
except ZeroDivisionError as e:
    print("never divided by zero")
except :
    print('error')