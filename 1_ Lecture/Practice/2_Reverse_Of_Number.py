n=int(input(""))
reversed=0
while n!=0:
    d=n%10;
    reversed=reversed*10+d;
    n=n//10

print(reversed)