Num = int(input('Enter loop numbers:'))
Numtotal = []
for i in range(Num):
    data = int(input('Enter data:'))
    Numtotal += [data]
        Numtotal.sort(reverse=False)
        print(Num[0])
        nvm = len(Num)
        print(Num[nvm-1])
