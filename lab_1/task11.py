import datetime

iterations = 10000000

print('----start-------')
start_time = datetime.datetime.now()
# insert code snippet here

# first way
for i in range(iterations):
    N = int('12345678')
    count = len(str(N))


end_time = datetime.datetime.now()
print(end_time - start_time)

print('----start-------')
start_time = datetime.datetime.now()
# insert code snippet here

# second way
for u in range(iterations):
    N = int(12345678)
    i = 0

    if N == 0:
        pass
        # print('i = 1')

    while N != 0:
        N = N//10
        i += 1
        # print('n =', N)
        # print('i =', i)
    #print(i)

end_time = datetime.datetime.now()
print(end_time - start_time)

# third way
# N = input("What`s N? ")
# i = 0

# for _ in N:
#     i += 1
# print(i)
