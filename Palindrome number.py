a=int(input())
n=a
result=0
while n>0:
    result = result*10+ n%10
    n=n//10
if result == a:
    print("true")
else:
    print("false")
