# Write a prog to rev string and numbers without any pre-build methods.
# with builtin slicing method ->

str1 = "abc123"
rev_str = str1[::-1]
print(rev_str)

# Program to Reverse Each Word in a String:

my_string = "good day is today"
word = my_string.split()
new_word = word[::-1]
print(new_word)
print(' '.join(new_word))

def rev_string(name):
    word = name.split()
    rev_word = word[::-1]
    return " ".join(rev_word)

name = "day good is today"
print(rev_string(name))

# rev num
def reverse_number(number):
    if number >= 0:
        rev_num = int(str(number)[::-1])
    else:
        rev_num = -int(str(-number)[::-1])

    return rev_num

number = -34567
print(reverse_number(number))
