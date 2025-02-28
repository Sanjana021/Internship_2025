input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"  
count = 0
index = 0
while index < len(input_string):
    if input_string[index] in vowels:
        count += 1
    index += 1
print("The number of vowels in the given string is:",count)
