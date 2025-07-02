#prime or not
temp = 0
n = int(input("Please enter a number: "))
for i in range(2, n//2):
    if n % i == 0:
        temp = 1
        break
if temp == 1:
    print("The given number is not a prime number")
else:
    print("The given number is a prime number")