def construct_grid(n, m):
    x = (2 * m) + 1
    while x <= n * m:
        for i in range(m):
            print(x + i, end=" ")
        print()
        x += 2 * m
    
    for i in range(1, m + 1):
        print(i, end=" ")
    print()

    for i in range(3 * m + 1, 4 * m + 1):
        print(i, end=" ")
    print()

    x = m + 1
    while x <= n * m:
        if x == 3 * m + 1:
            x += 2 * m
            continue
        for i in range(m):
            print(x + i, end=" ")
        print()
        x += 2 * m

num = int(input())

# Iterate over the test cases
for i in range(num):
    # Read the dimensions of the grid
    val1, val2 = map(int, input().split())

    grid = construct_grid(val1, val2)
