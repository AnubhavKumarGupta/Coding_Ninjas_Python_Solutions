## Read input as specified in the question
## Print the required output in given format
i=int(input())
for i in range(i, 0, -1):
    for j in range(0, i):
        print(i, end="")
    print()
