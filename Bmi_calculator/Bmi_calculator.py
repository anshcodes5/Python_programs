print("Type your weight and height to calculate your BMI!")

weight = input("What is your weight?\n")
height = input("What is your height?\n")

weight_as_integer = int(weight)
height_as_float = float(height)

bmi = int(weight_as_integer / height_as_float ** 2)

print("your body mass index is - " + str(bmi))
input("Press enter to close the program")