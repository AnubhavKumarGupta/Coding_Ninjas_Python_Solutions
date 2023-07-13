## Read input as specified in the question.
## Print output as specified in the question.
a = int(input())
for i in range(1,a+1):
    
    # for space
    for j in range(1, a+1-i):
        print(' ', end='')
    
    # for decreasing pattern
    for j in range(i,0,-1):
        print(j, end='')
    
    # for increasing pattern 
    for j in range(2,i+1):
        print(j, end='')
    
    # Moving to next line
    print()
