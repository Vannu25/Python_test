# even numbers
for i in range(2, 11, 2):
    print(i)

# odd numbers
for i in range(1, 10, 2):
    print(i)

#decreemental order
for i in range(10, 0, -1):
    print(i)

#while loop
print('-----------------------------------------------------------')
i = 1
while i<=10:
    print(i)
    i = i+1

print('------------------------------------------------------------')
i = 10
while i>=1:
    print(i)
    i=i-1
print('------------------------------------------------------------')
# How do you iterate through a list in Python?

l = [ 5, 7, 9]
for i in l:
    print(i)

print('--------------------------------------')
[print(i) for i in l] # list comprehension

    