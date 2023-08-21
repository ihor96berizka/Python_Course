i = 1
N = 5
u = 5
S = 5

while i <= N:
    j = 1
    while j <= i:
        print(i * 1, end=' ')
        j = j + 1
    print()

    i = i + 1

while u <= S:
    j = 1
    while j <= u:
        print(u * 1, end=" ")
        j = j + 1
    print()

    u = u - 1
    if u == 0:
        break
