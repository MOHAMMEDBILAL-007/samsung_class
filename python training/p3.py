average_score = int(input("enter teh average score of the student : "))
if average_score >=0 and average_score <= 69:
    print("result is fail")
elif average_score >= 70 and average_score <= 84:
    print("result is second class")
elif average_score >= 85 and average_score <= 95:
    print("result is first class")
elif average_score >= 96 and average_score <= 100:
    print("result is excellent")
else:
    print("invalid average score")