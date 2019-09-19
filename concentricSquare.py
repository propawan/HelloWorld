def sayHello():
    print("Hello!!!")


n = 4
t = 2 * n - 1
i = 0
row = 0

while i < t:

    ch = n
    j = 0
    while j < row:
        print(ch, end=" ")
        ch -= 1
        j += 1

    ch = n - row
    k = 0
    while k < t - 2 * row:
        print(ch, end=" ")
        k += 1

    ch = n - row + 1
    l = 0
    while l < row:
        print(ch, end=" ")
        ch += 1
        l += 1

    if i < t // 2:
        row += 1
    else:
        row -= 1

    i += 1
    print()

print("program by Dev")
print(":-)")
