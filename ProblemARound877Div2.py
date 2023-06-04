num = int(input())
for i in range(num):
    n = int(input())
    A = list(map(int, input().split()))
    indicator = 0
    for i in A:
        if i < 0:
            indicator = 1
            print (i)
            break
    if indicator == 0:
        print (max(A))
