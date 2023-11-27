# first way
def number_of_digits_in_a_number1(n):
    count = len(str(n))
    return count


# second way
def number_of_digits_in_a_number2(n):
    i = 0
    if n == 0:
        pass
    while n != 0:
        n = n//10
        i += 1
    return i


# read N
n = int(input("What`s N?"))
count1 = number_of_digits_in_a_number1(n)
count2 = number_of_digits_in_a_number1(n)
print(count1, count2)
