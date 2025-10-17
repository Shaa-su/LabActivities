#============================================================================================================================
# Activity1 A1 Personalized Greeting with Year of Birth
print("=================================================================")
print("Activity1 A1 Personalized Greeting with Year of Birth")
print("=================================================================")
Name = input("write your full name: ") #user can input their name and age
Age = input("What is your age?: ")

birth =  2025 - int(Age) #current age minus the year which is 2025 currently

print("Welcome "+ Name+"!"+" You are already", Age+" and was born around", birth); #to print the output
print("")
#============================================================================================================================
# Activity1 A2 Basic Calculator with user input
print("=================================================================")
print("Activity1 A2 Basic Calculator with user input")
print("=================================================================")
a = int(input(" insert the first number: ")) #user inputs
b = int(input(" insert the second number: "))
#This is where the conversion happens
Sum = a + b
Difference = a - b
Product = a * b
Quotient = round(a / b, 2)
#print of the output
print("--------Result of the Calculation--------")
print("=^.^=")
print("Sum:", Sum)
print("Difference:", Difference)
print("Product:", Product)
print("Quotient:", Quotient)
print("")
#============================================================================================================================
# Activity1 A3 Student Email Generator (String Manipulation)
print("=================================================================")
print("Activity1 A3 Student Email Generator (String Manipulation)")
print("=================================================================")
Fname = input(" Type your first name:") #for user input
Lname = input(" Type your lastname name:")
#to make the first and last name lowercase 
Lowfname = Fname.lower()
Lowlname = Lname.lower()

print(Lowfname+"."+Lowlname+"@bulsu.edu.ph") #print the output
print("")
#============================================================================================================================
# Activity1 A4 Demonstrate type casting by converting
print("=================================================================")
print("Activity1 A4 Demonstrate type casting by converting")
print("=================================================================")
number = int(input("Type any integer: "))

inttofloat = float(number)
floattostr = str(inttofloat)
strtoint = int(float(floattostr))

print("integer to float: ",inttofloat)
print("float to string: "+ floattostr)
print("string to Integer: ",strtoint)
print("")
#============================================================================================================================
# Activity1 B5 Grade Calculator
print("=================================================================")
print("Activity1 B5 Grade Calculator")
print("=================================================================")
prelim = int(input(" type your prelim score: ")) #user can input the grades
midterms = int(input(" type your midterms score: "))
final = int(input(" type your final score: "))

FinalGrade = (prelim*0.30)+(midterms*0.30)+(final*0.40) #given calculation

if FinalGrade >= 75: # to know if the student pass or fail lower then 75 then student fails
    print("PASSED")
else:
    print("FAILED")
print("")
#============================================================================================================================
# Activity1 B6 Student Information System (Dictionary Practice)
print("=================================================================")
print("Activity1 B6 Student Information System (Dictionary Practice)")
print("=================================================================")
Student = {
    "StudentID": input("Enter studentid: "),   # dictionary 
    "Full_name": input("Enter your full name: "),
    "Coursandsec": input("Enter your grade and section: "),
     "Email": input("Enter your Email: ") ,
}
# print the output
print("=====================================================================")
print("Student ID: "+Student["StudentID"]) # printing using dictionary
print("Full Name: "+Student["Full_name"])
print("Course and Section: "+Student["Coursandsec"])
print("Email Address: "+Student["Email"])
print("=====================================================================")
print("")
#============================================================================================================================
# Activity1 B7 Set Operations- Unique Courses
print("=================================================================")
print("Activity1 B7 Set Operations- Unique Courses")
print("=================================================================")
A = {"BSIT", "BSCS", "BSECE"}  #given groups
B = {"BSCS", "BSIS", "BSTM"}

Union_res = A.union(B)   # combination of all unique elements
Intersection_res = A.intersection(B) # to get only the ones that both group has a similarity
Difference_res = A.difference(B) # to get the ones that don't the other group don't have
# print of the results
print("=====================================================================")
print("Union result: " , Union_res)
print("Intersection result: " , Intersection_res)
print("Difference result: " , Difference_res)
print("=====================================================================")
print("")
#============================================================================================================================
# Activity1 B8 Simple Cashier Program
print("=================================================================")
print("Activity1 B8 Simple Cashier Program")
print("=================================================================")
Product = {
"product1": float(input("type first product: ")),  # I used dictionary again just like the prev activity to practice
"product2": float(input("type second product: ")),
"product3": float(input("type third product: ")),
"Cash": float(input("Enter the amount of cash: ")),
}

totalamount = Product["product1"] + Product["product2"] + Product["product3"] # simple adding of the products to get the total
change = Product["Cash"] - totalamount # the amount the user will pay
# print the output
print("+++++ Official Receipt +++++")
print("Product 1: " , Product["product1"])
print("Product 2: " , Product["product2"])
print("Product 3: " , Product["product3"])
print("Total amount:  " , totalamount)
print("Cash:  " , Product["Cash"])
print("Change:  " , change)

print("please come again!");
#============================================================================================================================