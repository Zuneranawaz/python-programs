# program to display prime numbers with an interval
lower=int(input("enter lowest interval"))
upper=int(input("enter upper interval"))
for n in range(lower,upper+1):
  if n>1:
    for i in range(2,n):
      if(n%i)==0:
        break
  else:
    print(n)
