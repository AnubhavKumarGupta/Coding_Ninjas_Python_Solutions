#Write Your Code Here

a=int(input())
result=0
while a>0:
    result = result*10+ a%10
    a=a//10
print(int(result))
    
