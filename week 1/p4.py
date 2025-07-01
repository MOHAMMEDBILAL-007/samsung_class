average_score = int(input("enter teh average score of the student : "))
if average_score in range(0,70):
    print("result is fail")
elif average_score in range(70,85):
    print("result is second class")
elif average_score in range(85,96):
    print("result is first class")
elif average_score in range(96,101):
    print("result is excellent")
else:
    print("invalid average score")#dfhfd