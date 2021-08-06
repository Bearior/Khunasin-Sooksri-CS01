A = int(input("Enter loop: "))
score_list = []
a = 0
for i in range(A):
    data = int(input("input score: "))
    score_list += [data]
while a <= A -1:
    if score_list[a] < 0:
        break
    print(score_list[a])
    a += 1