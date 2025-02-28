user_input = input("Enter a list : ")
numbers = list(map(float, user_input.split()))
if len(numbers) == 0:
    print("The list is empty.")
else:
    max_value = numbers[0]
    min_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    print(f"The maximum value in the list is:",max_value)
    print(f"The minimum value in the list is:",min_value)
