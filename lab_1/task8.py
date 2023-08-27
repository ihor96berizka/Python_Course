#read N
N = int(input("What`s N?"))

#formated N
N2 = str(N)
N2 = N2[::-1]
N2 = int(N2)

#final logic
if N == N2:
    print('True')
else:
    print('False')
