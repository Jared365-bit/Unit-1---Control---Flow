# print("Step 1: Get 2 bread slices") 
# print("Step 2: Get peanut butter") 
# print("Step 3: Get jelly") 
# print("Step 4: Get knife") 
# print("step 5: Spread penaut butter and jelly on two slices of bread with knife") 
# print("Step 6: Put the two bread slices toegther") 
# print("Step 7: Enjoy!") 


# age = int(input("Enter your age: "))
# if age >= 18: 
#     print("You can vote!") 
# else: 
#     print("You cannot vote!") 

# fav_number = int(input("What is your favorite number (Please enter a non-decimal interger): ")) 

# if fav_number % 2 == 0: 
#     print("Your number is even") 
# else: 
#     print("You number is odd") 



#-----Steps for Brushing Teeth------- 
# print("Step 1: Get toothbrush")
# print("Step 2: Get toothpaste")
# print("Step 3: Put toothpaste on toothbrush")
# print("Step 4: put toothbrush on teeth")
# print("Step 5: Brush teeth with toothbrush for 2 minutes with circular motions") 
# print("Step 6: spit excess toothpaste and wash mouth") 

#-----------Favorite color---------- 
# color = input("what is your favorite color: ") 

# print(f"Wow, I like {color} too!") 


#-----------Positive, negative, or zero--------- 

# number = int(input("Pick a number: ")) 

# if number > 0: 
#     print("Your number is positive!") 
# elif number == 0:  
#     print("Your number is zero!") 
# else: 
#     print("Your number is negative") 
    
    
    #-----------Simple loop-------- 
# name = "Jared Vasquez"
# for _ in range(3):
#     print(name)
    
    
    
    
#-------------Even or Odd---------- 
# user_number = int(input("Pick a number: ")) 

# if user_number % 2 == 0: 
#     print("Your number is even") 
# else: 
#     print("Your number is odd") 
    
    
    #---------Multiplication Table Generator------ 
    
# number = int(input("Enter a number: "))


# for i in range(1, 11):
#     print(f"{number} × {i} = {number * i}")
    
    

#-------------Movie Ticket Price:----------- 
# age = int(input("What is your age: ")) 

# if age < 13: 
#     print("Child ticket: $8") 
# elif 13 <= age <= 59: 
#     print("Adult ticket: $12") 
# elif 60 <= age: 
#     print("Senior ticket: $6")  
    
    
#------------------------ATM Machine-----------------

# pin = 2332 

# input = int(input("Enter your pin: ")) 

# balance = 10 

# # balance = 0

# withdrawl = None


# if pin == input: 
#     print("Access allowed") 
#     if balance > 0: 
#         while balance > 0: 
#             print("Withdrawl allowed") 
#             withdrawl = True 
#             break 
#     else: 
#         print("Withdrawl premission Denied") 
#         withdrawl = False 
# else: 
#     print("Pin is incorrect")
    
    
#--------------------Password Practice Challenge-------------- 

# input = input("Enter password: ") 

# password = "BCTS2025" 

# if input == password: 
#     print("Welcome!") 
# else: 
#     print("Try again.")


#---------------Money for Snacks---------------- 

money= float(input("Enter how much money you have: "))  
change = money -2

if money < 2: 
    print("Not enough money") 
elif money == 2: 
    print("Dispense snack") 
else: 
    print(f"Dispense snack + return {change}")