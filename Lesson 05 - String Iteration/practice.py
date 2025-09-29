text = "hello world" 
# count = 0 
# for char in text:
#     if char == 'a'or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U': 
#         count += 1 
# print(f"Number of vowels: {count}") 

vowels = "aeiouAEIOU"  
vowel_count = 0
for char in text: 
    if char in vowels: 
        vowel_count += 1 
print(f"vowels in '{text}': {vowel_count}") 

text = "ABC123xyz" 

for i in range(len(text)): 
    if '0' <= text[i] <= '9': 
        print(f"Digit at position {i}: {text[i]}")

word = "Hello" 

for i in range(len(word)): 
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {-1-i}")