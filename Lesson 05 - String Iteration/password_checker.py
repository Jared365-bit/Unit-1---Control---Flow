import sys
password = input("Enter your password: ") 
letter_count = 0 
digit_count = 0 
uppercase_count = 0
lowercase_count = 0 
special_count = 0
has_upper = False       
has_lower = False      
has_digit = False    
has_special = False 
min_length = 8 
if len(password) >= min_length: 
    for char in password: 
        if 'A' <= char <= 'Z': 
            has_upper = True 
            uppercase_count += 1
        elif 'a' <= char <= 'z': 
            has_lower = True 
            lowercase_count += 1
        elif '0' <= char <= '9': 
            has_digit = True  
            digit_count += 1
        elif not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9' or char == ' '):
            has_special = True 
            special_count += 1 
    print(f"Uppercase: {uppercase_count}")
    print(f"Lowercase: {lowercase_count}")
    print(f"Digit: {digit_count}")
    print(f"Special: {special_count}")


print(f"Enter a password: {password}") 


print('PASSWORD ANALYSIS:')

print('==================') 

print(f"Password: '{password}'") 



print("CHARACTER COUNTS") 
print(f"Length: {len(password)} characters") 
print(f"Uppercase: {uppercase_count}")
print(f"Lowercase: {lowercase_count}")
print(f"Digit: {digit_count}")
print(f"Special: {special_count}") 


print("REQUIREMENTS CHECK") 
if len(password) >= min_length: 
    print("✔️  Length (8+ characters): PASSED") 
else: 
    print("❌  Length (8+ characters): FAILED") 
if has_upper == True: 
    print("✔️  Uppercase letters: PASSED")  
else: 
    print("❌  Uppercase letters: FAILED")
if has_lower == True: 
    print("✔️  Lowercase letters: PASSED") 
else: 
    print("❌  Lowercase letters: FAILED")
if has_digit == True: 
    print("✔️  Digits: PASSED") 
else: 
    print("❌  Digits: FAILED")
if has_special == True: 
    print("✔️  Special characters: PASSED") 
else: 
    print("❌  Special characters: FAILED")


print("SECURITY ISSUES") 
three_in_row = False 
sequence = False

for i in range(len(password) - 2): 
    if password[i] == password[i+1] == password[i+2]: 
        three_in_row = True 
        print(f"Found 3 in a row: {password[i]}") 
        
        
for i in range(len(password) - 2):
    if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2: 
        sequence = True 
        print(f"Found sequence: {password[i:i+3]}")


if three_in_row == True: 
    print("⚠️  Repeated characters (3+)") 
else: 
    print("✔️ No repeated characters (3+)")

if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
    print(f"⚠️  Contains sequence  {password[i:i+3]} ") 
else: 
    print(f"✔️ Does not contain sequence") 
    

if has_digit == True and has_lower == True and has_upper == True and has_special == True and not three_in_row == True and not sequence == True and len(password) >= 8: 
    print("FINAL RATING: STRONG")
elif not has_digit == True or not has_lower == True or not has_upper == True or not has_special == True or  not three_in_row == True or  not sequence == True or len(password) < 8:
    print("FINAL RATING: MEDIUM") 
    if not has_upper == True: 
        print("- All requirements met but is missing uppercase letters") 
        sys.exit()
    elif not has_lower == True: 
        print("- All requirements met but is missing lowercase letters") 
        sys.exit()
    elif not has_digit == True: 
        print("- All requirements met but is missing digits")  
        sys.exit()
    elif not has_special == True: 
        print("- All requirements met but is missing special characters")  
        sys.exit()
    elif not three_in_row == True: 
        print("- All requirements met but has 3 same characters in a row") 
        sys.exit()
    elif not sequence == True: 
        print("- All requirements met but has a simple sequence") 
        sys.exit()
    elif len(password) < 8: 
        print("- All requirements met but is less than 8 characters") 
        sys.exit()
else: 
    print("FINAL RATING: WEAK") 
    if not has_upper == True: 
        print("- All requirements met but is missing uppercase letters") 
    if not has_lower == True: 
        print("- All requirements met but is missing lowercase letters") 
    if not has_digit == True: 
        print("- All requirements met but is missing digits") 
    if not has_special == True: 
        print("- All requirements met but is missing special characters")  
    if not three_in_row == True: 
        print("- All requirements met but has 3 same characters in a row") 
    if not sequence == True: 
        print("- All requirements met but has a simple sequence") 
    if len(password) < 8:
        print("- All requirements met but is less than 8 characters")
