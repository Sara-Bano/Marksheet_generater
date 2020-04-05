name =input('What is your name ?\n')

math_marks =int(input("please enter your math marks out of 100 \n "))

english_marks =int(input("please enter your english marks  out of 100 \n "))

urdu_marks =int(input("please enter your urdu marks  out of 100 \n "))

total = 300
obtained_marks = math_marks + english_marks + urdu_marks

percentage = (obtained_marks / total ) * 100

print("\n ********************************************* MARKSHEET *********************************************************** \n")

print(name + " your percentage is " + str(percentage) + "%")
print("And Your --------->")

if(percentage <= 100 and percentage >= 90):
    print("Grade is A+")
elif(percentage >= 80 and percentage < 90 ):
    print("Grade is A")
elif(percentage >= 70 and percentage < 80  ):
    print("Grade is B")
else:
    print("Grade is C")




