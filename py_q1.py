"""Find how many times a given character has occurred in the string and
create a dictionary with key as character and value as number of occurrences.
Example- str=’thisistest’ . Find how many times ‘s’ is in the string.
If it's 3 times then {‘s’: 3} and so on, the dictionary will have each unique character as a key."""

char_count = {} #empty dic to store newly created
str = "thisistest"

for i in str:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print(char_count)

"""for above question also do char count"""

char_count = {}
def occurrences(char):
    for i in char:
        if i in char_count:
            char_count[i] += 1

        else:
            char_count[i] = 1
    return char_count

char = "thisistest"
output = occurrences(char)
print(f" the dict output is : ",output)

print("=======================================================")
# Find the least frequent character in the string
# Example - str=’thisistest’

char1 = "thisistest"
least_freq = {}

# Count the frequency of each character
for i in char1:
    if i in least_freq:
        least_freq[i] += 1  # Increment count if character is already in the dictionary
    else:
        least_freq[i] = 1  # Initialize count to 1 if character is not in the dictionary

# Find the least frequent character
min_freq = min(least_freq.values())  # Find the minimum frequency
least_frequent_chars = [char for char, freq in least_freq.items() if freq == min_freq]

print("Character frequencies:", least_freq)
print("Least frequent character(s):", least_frequent_chars)



