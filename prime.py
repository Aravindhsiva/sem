num = int(input())
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("It is not a prime number")
           break
   else:
       print("It is a prime number")
else:
   print("It is not a prime number")
