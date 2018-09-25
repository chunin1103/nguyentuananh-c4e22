h = 1 / 100 * float(input("Please enter your height specifically in centimeter "))
w = float(input("Please enter your weight specifically in kilogram "))

BMI = w / (h * h)

print("Your BMI score is ", BMI, ", shows that you are ", end="")
if BMI < 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normal")
elif BMI <= 30:
    print("Overweight")
else:
    print("Obese")
