#Write a program to find sum of all values in dictionary
#Example - d = {'a':230,'b':100, 'c': 170, 'd' :50} . Ans - 550

d = {'a':230,'b':100, 'c': 170, 'd' :50}
summ = (d.values())
new_summ = sum(summ)
print(new_summ)


def sum_of_values(dict):
    # Use sum() to calculate the total of all values in the dictionary
    return sum(dict.values())

# Dictionary with numeric values
d = {'a': 230, 'b': 100, 'c': 170, 'd': 50}

# Call the function and store the result
res = sum_of_values(d)
print(res)
