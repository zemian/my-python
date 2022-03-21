# print a chess-board grid that has alternate color squares
row, col = 8, 8
for x in range(row):
    for y in range(col):
        color = "X" if (x + y) % 2 == 0 else "O"
        print(color, end=' ')
    print()
