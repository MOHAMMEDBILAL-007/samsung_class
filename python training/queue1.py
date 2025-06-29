#Implement Queue using list, insert at rear delete from front the list
queue1 = []
def enqueuq():
    item = int(input("Enter the item to be inserted in the queue: "))
    queue1.append(item)
    print(f"{item} inserted in the queue")
def dequeue():
    if len(queue1)==0:
        print("que under flow")
    else :
        print(f"{queue1[0]} was deleted from the queue")
        queue1.pop(0)
def display():
    print("elements in the que are :")
    print(queue1)
while True:
    input_number = int(input("enter :1 if enqueue \nenter :2 if dequeue \nenter :3 if display \n:-"))
    if input_number == 1:
        enqueuq()
    elif input_number ==2:
        dequeue()
    elif input_number ==3:
        display()
    else:
        print("invalid input")
