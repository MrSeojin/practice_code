flag = False
count = 0
for _ in range(8):
    space = input()
    flag = not flag
    for a in range(8):
        if flag and space[a] != '.':
            count += 1
        flag = not flag
print(count)
