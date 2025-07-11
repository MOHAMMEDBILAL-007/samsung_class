import re
a ="17 hardest 12choice 3434requires 2 strongest 33will"
b ="12345553"
result = re.search(r"\d+",a)# this returns matched or  , + is used to search the associated number also
print(result.group())# .group() helps to extracted matched string from a
# the above method returns only the first number the number that is in beteeen gaps is not writtened 
# the above method returns 17 but doesent return 2

result2 = re.findall(r"\d+",a)#returns all the digits
print(result2)

result3 = re.match(r"17 hardest",a)# returns matched only if the string is started from the same searching string
print(result3)# .group() extracts the matched string

result4=re.fullmatch(r"\d+",b)# returns matched only if all the string is digit, + checks the associated digits 
print(result4)

result5 = re.finditer(r"\d+",a) # now this is a iterateable it cannot be directly printed
for i in result5:
    print(i.group(),end = " ")
# above method works similar to er.findall() 
print()

result6 = re.sub(r"\d","#",a)# replaces every single digit with # ,if i add + with \d all the associated digits will be replaced by a single #
print(result6)

result7 = re.subn(r"\d","#",a)# returns tuple of replaced string and number of digits replaced, if i add + with \d all the associated digits will be replaced by a single #
print(result7)

result8 = re.split(r"[ a]",a)# inside the square bracket i have space and a it means split where there is space or a ,no need to seperate by comma
#[] is used to split at multiple charectors
print(result8)

result8= list(map(str,re.split(r"\d+",a)))#here at every associated digits the string is split
print(result8)

result9= re.compile(r"\d+")# now result acts like a compiled object 
print(result9.findall(a))# now we can use result9 as as an object to run methods and passing attributes
