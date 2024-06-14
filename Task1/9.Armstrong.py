def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end} are:")
print(armstrong_numbers)
