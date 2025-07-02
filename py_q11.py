#Find how many times given character has occurred in the string
#Example - str=’thisistest’ . Find how many times ‘s’ is in the string.

def count_character(string, char_to_find):
    count = 0
    for char in string:
        if char == char_to_find:
            count += 1
    return count


# Example input
string = "thisistest"
char_to_find = 't'

# Count occurrences
occurrences = count_character(string, char_to_find)
print(f"The character '{char_to_find}' appears {occurrences} times in the string.")



# without function

str2 = "thisistest"
char_tobe_found = input("enter char: ")
count = 0
for i in str2:
    if i == char_tobe_found:
        count += 1

print(f"The {char_tobe_found} occurred {count} times in string")
