## The continue Statement 
''' 
**Continue** = Skip to the next iteration 

**Difference from break:** 
-**break** -> Exit the loop completely 
-**continue ->  
''' 

count = 0 

while count < 5: 
    count += 1 
    if count == 3: 
        continue 
    print(count) #1 2  4 5