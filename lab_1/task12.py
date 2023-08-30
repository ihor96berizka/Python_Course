# use slicing
N = [1, 2, 3, 4, 5]
N = N[::-1]
print(N)

# use built-in
N = [1, 2, 3, 4, 5]
N.reverse()
print(N)

# use for loop
N = [1, 2, 3, 4, 5]

for i in range(len(N) -1, -1, -1):
    print(N[i], end=" ")
print()

# use while loop
N = [1, 2, 3, 4, 5]
i = len(N) -1

while i != -1:
    print(N[i], end=" ")
    i -= 1
