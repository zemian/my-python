size = 8
for x in range(size):
    for y in range(size):
        color = "X" if (x + y) % 2 == 0 else "O"
        print(color, end=' ')
    print()
