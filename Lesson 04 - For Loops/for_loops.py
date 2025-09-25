# Three forms of range() function 
#1 range(stop) 
for i in range(5): #0,1,2,3,4
    print(i)  
#2 range(start, stop)   
for i in range(3,8): #3,4,5,6,7
    print(i)   
#3 range(start, stop. step)   
for i in range(2,11,2): #2,4,6,8,10
    print(i)  
#Counting backwards
for i in range(10,1,-2): 
    print(i) 
    
#Countdown Timer 
import time
for seconds in range(10,-1,-1): 
    print(f"{seconds}-seconds")  
   # time.sleep(1) #wait 1 second between numbers 
print("BLAST OFF!🚀")
    
#Multiplication Table 
# Take user input for number and print the table 
#if the user submitted 5
#5x1=5
#5x2=10 
number = int(input("Enter a number (1-12) : ")) 
if 1 <= number <= 12: 
    for i in range(1, 13):
     print(f"{number} × {i:2d} = {number * i:3d}") 
else: 
    print("Please enter a number between 1 and 12")