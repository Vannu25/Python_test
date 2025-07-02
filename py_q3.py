#Find a substring from a string and check if it exists as a dictionary key.
# If it does then print the value else print that string is invalid.
# Example - str = “thisisfirstmonth” Consider that this highlighted substring will always
# be at this position which between “thisis…month”
#dic1 = {‘first’: ‘jan’, ‘second’: ‘feb’, ‘third’: ‘march’, ‘fourth’: ‘april’, ‘fifth’: ‘may’, ‘sixth’: ‘june’}

def month(dict1):
    check_key_exists = "first"
    if check_key_exists in dict1:
        print(f"The value of key is : {dict1[check_key_exists]}")
        return dict1[check_key_exists]
    else:
        print("String is invalid")
        return None

dict1 = {
    "first": "jan",
    "second": "feb",
    "third": "march",
    "fourth": "april",
    "fifth": "may",
    "sixth": "june"
}
print(month(dict1))

# without function ===========================================================================
dict1 = {
    "first": "jan",
    "second": "feb",
    "third": "march",
    "fourth": "april",
    "fifth": "may",
    "sixth": "june"
}

# Input key from the user
key_to_find_in_dict = input("Enter key that needs to find: ")

# Check if the key exists in the dictionary
if key_to_find_in_dict in dict1:
    print(f"The key value is: {dict1[key_to_find_in_dict]}")
else:
    print("month is invalid")
