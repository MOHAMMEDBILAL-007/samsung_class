#Implement Queue using list, insert front, delete from rear of the list
queue2 =[]
def enqueuq():
    item = int(input("Enter the item to be inserted in the queue: "))
    queue2.insert(0,item)
    print(f"{item} inserted in the queue")
def dequeue():
    if len(queue2)==0:
        print("que under flow")
    else :
        print(f"{queue2[-1]} was deleted from the queue")
        queue2.pop()
def display():
    print("elements in the que are :")
    print(queue2)
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