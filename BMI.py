#Owen Coleman
#Weekly task 2
#Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. 
#The output is their weight divided by their height in metres squared.

#Two variables which take float values for weight and height. 
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

#BMI calculation: weight by height(in metres) squared
bmi = weight / ((height / 100) **2)

#prints the output
print("BMI is", bmi)

