N = int(input("What`s N?"))
N2= str(N)
N2 = N2[::-1]
N2 = int(N2)
if N == N2:
    print('True')
else:
    print('False')
