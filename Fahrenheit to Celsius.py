# Read input as sepcified in the question
# Print output as specified in the question
S=int(input())
E=int(input())
W=int(input())
V=S
while V<=E:
    F=(5.0/9)*(V-32)
    print(int(V),int(F))
    V=V+W
