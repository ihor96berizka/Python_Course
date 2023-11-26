def is_palindrome(n):
    reverse_n = int(str(n)[::-1])
    return n == reverse_n


# read N
n = int(input("What`s N?"))

result = is_palindrome(n)
print(result)
