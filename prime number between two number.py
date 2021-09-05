#print the prime number between two number range
# we can take two user input value
x=int(input('ENTER 1st NUMBER:'))
y=int(input('ENTER 2nd NUMBER:'))
# we cane use for loop
# we add 1 in 2nd value in range function
print('PRIME NUMBER BETWEEN',x,'AND',y,'IS:')
for number in range(x,y+1):
#we are know 1 is not prime number so we can only take number greater than 1
    if number>1:
        # for prime number only two divisor 1 and itself so divisor is always take less then number
        for i in range(2,number):
         #divisor is more than two not a prime number
          if number % i==0:
           break
        else:
           print(number)
# THANKS akhlakansari94@gmail.com