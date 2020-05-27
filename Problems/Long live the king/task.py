col = int(input())
row = int(input())
move = (col, row)

val3 = [(1, 1), (1, 8), (8, 1), (8, 8)]

val5 = [(1, x) for x in range(2, 8)]
temp5 = [(y, 1) for y in range(2, 8)]
val5.extend(temp5)
temp5 = [(8, x) for x in range(2, 8)]
val5.extend(temp5)
temp5 = [(y, 8) for y in range(2, 8)]
val5.extend(temp5)


if move in val3:
    print(3)
elif move in val5:
    print(5)
else:
    print(8)