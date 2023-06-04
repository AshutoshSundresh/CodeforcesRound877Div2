num = int(input())
for i in range(num):
    n = int(input())
    A = list(map(int, input().split()))
    
    one = -1
    two = -1
    maximum = -1

    for i in range(n):
        if A[i] == 1:
            one = i
        elif A[i] == 2:
            two = i
        elif n == A[i]:
            maximum = i

    if (one < maximum and maximum < two) or (two < maximum and maximum < one):
        print((one + 1), (two + 1))
        continue
    else:
        if maximum > one and maximum > two:
            print((maximum + 1), (1 + max(one, two)))
        else:
            print((maximum + 1), (1 + min(one, two)))
