n = int(input("enter the number requests :"))
req = list(map(int,input("enter the requests seperated by space :").split()))
memory_units =0
for i in range(n):
    if i ==0:
        memory_units+=req[0]
    elif i %2 ==0:
        memory_units+=req[i]
    else:pass
print(memory_units)
