## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
a=int(input())
even=0
odd=0
while a!=0:
    last=a%10
    if last %2 ==0:
        even =even + last
    else:
        odd=odd+last
    a=a//10
print(even, " " ,odd)
