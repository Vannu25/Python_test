# Write a program to remove n-th character from the string
#Example = str=’thisistest” Remove 6th Character.


def remove_nth_character(string, n):
    # Ensure n is within the valid range
    if n <= 0 or n > len(string):
        return "Invalid position!"
    # Remove the n-th character
    result = string[:n-1] + string[n:]
    return result

# Example input
string = "thisistest"
n = 5  # Position to remove (1-based index)

# Remove and print the result
result = remove_nth_character(string, n)
print(f"String after removing the {n}-th character: '{result}'")

#without function

str5 = "thisistest"
n = int(input("Enter the position (1-based) of the character to be removed: "))

# Check if the input position is valid
if n <=0 or n > len(str5):
    print("invalid")
else:
    result = str5[:n-1] + str5[n:]
    print("result after removing", result)


