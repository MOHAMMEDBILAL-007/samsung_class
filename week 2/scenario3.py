n,x,y = map(int,input("enter n elements x elements y elements seperated by space :").split())
list1 = list(map(int,input("enter the list elements :").split()))
list1.sort(reverse=True)
if n == len(list1):
    xlist=list1[:x]
    ylist=list1[x+1:]
    numberOFp = xlist[len(xlist)-1] - ylist[0] -1
    print(list1)
    print("the number of p that exist are:",numberOFp)
else:pass
