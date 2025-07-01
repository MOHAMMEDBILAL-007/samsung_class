# implementing stack using list from the end of the list using insert and del mwthods
stack1 =[]
def push():
    item = int(input("Enter the item to be pushed: "))
    stack1.insert(0,item)
    print(f"{item} inserted to the stack")
def pop():
    if len(stack1)==0:
        print("stack under flow")
    else: 
        print(f"{stack1[0]} was deleted from the stack")
        del stack1[0]
def display():
    print("stack contains the following elements")
    for i in stack1:
        print("%3d"%i)
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