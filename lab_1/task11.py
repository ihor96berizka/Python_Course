# first way
N = input("What`s N? ")
print(len(N))

# second way
N = input("What`s N? ")
i = 0

while i < len(N):
    i += 1
print(i)

# third way
N = input("What`s N? ")
i = 0

for _ in N:
    i += 1
print(i)
