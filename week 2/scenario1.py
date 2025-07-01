def fun(str1,str2):
    temp = str1*2
    if str2 in temp:
        print(1)
    else:
        print(-1)
os = input("enter the original string :")
rs = input("enter the rotated number :")
fun(os,rs)