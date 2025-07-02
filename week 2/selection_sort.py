input_list = list(map(int,input("enter the elements seperated by spaces").split()))

n = len(input_list)
for i in range(n):
    min =i
    for j in range(i+1,n):
        if input_list[min]>input_list[j]:
            min =j
    input_list[i],input_list[min]=input_list[min],input_list[i]
       
print(input_list)