import sys #Searched up online how to stop code after an if statement. I Couldn't do it from memory.
height = int(input("Please enter your height: "))
weight = int(input("Please enter your weight: ")) 
print("=== BMI Calculator ===") 
print(f"Height in inches: {height}")
print(f"Weight in pounds: {weight}") 
if not height or not weight: 
    print("Please Enter positive values")  
    sys.exit()
unrounded_bmi = float((weight / (height ** 2)) * 703) 
BMI = round(unrounded_bmi, 1)
BMI_category = ("Underweight" if BMI < 18.5 else 
                "Normal" if 18.5 <= BMI <= 29.9 else
                "Overweight" if 25 <= BMI <= 29.9 else 
                "Obese"
                ) 
Recommendation = ("Gain weight" if BMI_category == "Underweight" else 
                  "Maintain weight" if BMI_category == "Normal" else 
                  "Lose weight" if BMI_category == "Overweight" else 
                  "Lose weight"
                  ) 
health_risk = ("moderate" if BMI_category == "Underweight" else 
               "Low" if BMI_category == "Normal" else
               "Moderate" if BMI_category == "Overweight" else
               "High"
               ) 

print("================================") 
print("BMI HEALTH REPORT") 
print("================================")  
print(f'Height: {height}"') 
print(f"Weight: {weight} lbs") 
print(f"BMI: {BMI}") 
print(f"Category: {BMI_category}") 
print(f"Recommendation: {Recommendation}")  
print(f"Health Risk: {health_risk}") 

print("================================") 