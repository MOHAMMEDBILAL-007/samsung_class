#Implement Stack using list, insert and delete from end of the list
stack2 = []
def push():
    item = int(input("Enter the item to be pushed: "))
    stack2.append(item)
    print(f"{item} inserted to the stack")
def pop():
    if len(stack2) == 0:
        print("stack under flow")
    else:
        print(f"{stack2[-1]} was deleted from the stack")
        del stack2[-1]
def display():
    print("stack contains the following elements")
    for i in range(len(stack2)-1,0,-1):
        print("%3d"%stack2[i])
while True:
    input_number = int(input("enter :1 if push \nenter :2 if pop \nenter :3 if display \n:-"))
    if input_number == 1:
        push()
    elif input_number ==2:
        pop()
    elif input_number ==3:
        display()
    else:
        print("invalid input")