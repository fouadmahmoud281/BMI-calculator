weight= input("enter your weight in kg :")
height= input("enter your height in m :")
BMI= round(float(weight) / float(height)**2 , 2)
BMI_as_string= str(BMI)
if BMI < 18.5:
  print(f"your BMI is {BMI} ,you are underweight")
elif BMI <=25:
  print(f"your BMI is {BMI} ,you have a normal weight")
elif BMI <=30:
  print(f"your BMI is {BMI} ,you are over weight")
elif BMI <=35:
  print(f"your BMI is {BMI} ,you are obese")
else:
  print(f"your BMI is {BMI} ,you are clinically obese")