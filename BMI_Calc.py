
def user_prompt():
    print("Please enter the following values for the user...")
    height = int(input("Height in inches: "))
    weight = int(input("Weight in pounds: "))
    age = int(input("Current age: "))
    RHR = int(input("Resting heart rate: "))
    return weight, height, age, RHR

#Calculate the BMI number   
def bmi_calc(pound_weight, inch_height):
    kg_weight = pound_weight * 0.45359237
    meter_height = inch_height * .0254
    bmi = kg_weight/meter_height**2
    return bmi

#Show which status the BMI is in
def bmi_category(bmi):
#status = True
    print("Results...")
    if bmi < 18.5:
        bmi_categ = "Underweight"
    elif bmi < 24.9:
        bmi_categ = "Normal"
    elif bmi <= 29.9:
        bmi_categ = "Overweight"
    elif bmi > 29.9:
        bmi_categ = "Obese"
    else:
        print("That is not a valid response")
    print("Your BMI is: " + str(bmi) + "--" + bmi_categ)
    print("\n")
        
def Max_HR(age, rhr):
    intensity = .50
    print("Intensity\tMax Heart Rate")
    for i in range(10):
    #karvonen function
        MaxRate = (((220 - age) - rhr) * intensity) + rhr
        print("{}\t\t{}".format(round(intensity,2), round(MaxRate,2)))git 
        intensity += .05


weight, height, age, RHR = user_prompt()
bmi = bmi_calc(pound_weight=weight, inch_height=height)
bmi_category(bmi)
Max_HR(age, RHR)
