def sum_of_numbers(n):
    sum_num = 0
    for x in range(1, n+1):
        sum_num += x
    return sum_num


# getting number from user
n = int(input("What`s N?"))
sum_num = sum_of_numbers(n)
print(sum_num)
