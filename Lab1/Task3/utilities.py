def find_even_numbers(numbers: list) -> list:
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers
