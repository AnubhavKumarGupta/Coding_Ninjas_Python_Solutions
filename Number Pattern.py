## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=0
while i<n:
    j=1
    while j<n-i+1:
        print(j,end = "")
        j=j+1
    i=i+1
    print()
