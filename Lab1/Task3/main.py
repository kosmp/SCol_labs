import utilities

numbers = input("Enter a list of numbers: ").split(' ')

try:
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    even_numbers = utilities.find_even_numbers(numbers)
    print(even_numbers)
except ValueError:
    print("Error, incorrect input. Can't convert number")
