num_rows = int(input())

for i in range(num_rows, 0, -1):
    line = ""
    for j in range(i, num_rows + 1):
        line += chr(j + 64)
    print(line)
