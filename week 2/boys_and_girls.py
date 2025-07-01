n = int(input("enter the number of students :"))
blist =list(map(int,input("enter the heights of the boys seperated by spaces :").split()))
glist =list(map(int,input("enter the heights of the girls seperated by spaces :").split()))
blist.sort()
glist.sort()
line =True
for i in range(0,len(blist)-1):
    if glist[i+1] >= glist[i] and blist[i]<=glist[i+1]:
        pass
    else:
        line = False
        break
if line :
    print("YES")
else:
    print("NO")
    