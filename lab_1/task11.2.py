# first way
def fun1(n):
    count = len(str(n))
    return count

# second way
def func2(n):
    i = 0
    if n == 0:
        pass
        # print('i = 1')
    while n != 0:
        n = n//10
        i += 1
        # print('n =', N)
        # print('i =', i)
    return i

#read N
N = int(input("What`s N?"))
count1 = fun1(N)
count2 = func2(N)
print(count1, count2)


# third way
# N = input("What`s N? ")
# i = 0

# for _ in N:
#     i += 1
# print(i)
