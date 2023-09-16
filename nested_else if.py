height=float(input("enter height in metres: "))
weight=float(input("enter weight in kgs: "))
bmi=weight/(height)**2

if(bmi<18.5):
    print(f"Your bmi is {bmi} and you are underweight")
elif bmi <25:
    print(f"Your bmi is {bmi} and you are normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi} and you are overweight")
elif bmi<35:
    print(f"Your bmi is {bmi} and you are obese")
else:
    print(f"Your bmi is {bmi} and you are clinically obese")