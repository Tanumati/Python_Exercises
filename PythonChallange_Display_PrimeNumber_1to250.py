
## Print prime numbers 1 to 250

for num in range(1,250):
    if all(num%i!=0 for i in range(2,num)):
       print ( "print prime number " + str(num))