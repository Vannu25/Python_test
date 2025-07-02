# Write a prog to find largest number in the list
# Example - [10,45,23,22,5] . Expected Ans - 45

items = [3, 7, 8, 9, 10, 1, 2]
# using pre-built method
print(max(items))

# As func with loops

def find_largest(numbers):
    largest = numbers[0] # initialize the 1st large number to 0 - starting of numbers.
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [10,45,23,22,5]
print(find_largest(numbers))

# without func and only using loop
items = [3, 7, 8, 9, 10, 1, 2, 25]
largest = items[0]
for i in items:
    if i > largest:
        largest = i
print(largest)
