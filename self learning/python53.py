#map ,filter ,reduce

#MAP()
# function for cube of a number
def cube(x):
    return x*x*x
print(cube(2))

# if i need to pass a list as an argument directly it will give me an error
# so we use a loop and a new list to perform the operation
l1 =[1,2,3,4,5,6,7,8]
nl1=[]
for i in l1:
    nl1.append(cube(i))
print(nl1)
# the above method is so long 

# so we use map function
nl2 =list(map(cube,l1))# map function takes 2 arguments 1 the function to perform and other on which iteratable object to perform
print(nl2)

# FILTER
