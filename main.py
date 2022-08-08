#write a code to calculate the sum of prime numbers of any range
primenum = int(input("Enter a number:"))
the_sum  = 2

for num in range(primenum + 1):
    if int(num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
            elif i == (num - 1):
                the_sum += num

print("The sum is", str(the_sum))