n = int(input("Enter number of terms: "))

first_number = 0
second_number = 1

for i in range(n):
    print(first_number)
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
