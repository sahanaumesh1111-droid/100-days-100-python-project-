height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is", bmi)
if(bmi<18.5):
    print('you are under weight')
elif(bmi>25):
    print('you are over weight')
else:
    print("you are normal weight")
