# today i need to become comfortable with operators so 
# i am doing yesterday problem today :
# 1. Student eligibility checker :

age = int(input("Please enter your age :"))
marks = int(input("Please enter your marks : "))

courses = ["python","english learning","java","html","css"]

course = input("Please enter your prefered course :").lower()
if (age >= 18 and marks >= 85 and course in courses) :
    print("you are eligible for selection")
elif (age != 18 and marks >= 85 and course in courses ):
    print("your age in not eligible in our criteria")
elif (age >= 18 and marks != 85 and course in courses):
    print("your marks is not under the criteria")
elif (age >= 18 and marks >= 85 and course not in courses):
    print("your prefered courses is not in our criteria yet")
else :
    print("you are not eligible")

# 2. driving license :

age = int(input("Please enter your age :"))
test_score = int(input("Please enter your test score : "))

vehicle_category = ["truck","car","bike"]
vehicle = input("Please enter your prefered vehicle :").lower()

if (age >= 18 and test_score >= 80 and vehicle in vehicle_category):
    print("Here is your license brother")
elif (age != 18 and test_score >= 80 and vehicle in vehicle_category):
    print("Please wait till turn 18 ")
elif (age >= 18 and test_score != 80 and vehicle in vehicle_category) :
    print("Please try again later")
elif (age >= 18 and test_score >= 80 and vehicle  not in vehicle_category):
    print("This vehicle is not in our facility")
else :
    print("not eligibilty")