#methods of file handeling
f = open("manage 49.txt",'r')
while True:
    text = f.readline()
    if not text:
        break
    print(f"{text}")
f.close()

f = open("manage 49.txt",'r')
for txt in f.readlines():
    l1=list(txt.split(" "))
    print(l1)
f.close()

f = open("manage 49.txt",'a')#iam not using w mode because it will override the whole text
lines = ["\n-\"in human society lands are seperated with borders marking their territories \non the right side children may starve to death \non the left side however idel dreds who do nothing have every thing\"\n","wars will only lead to dispair \nthat dispair will serve as a fuel this world to burn "]
#above i need to use \n for every new line even if the element is different new line will not be added automatically
f.writelines(lines)

f.close()