# check if string or num is palindrome or not.

text = input("Enter your text: ")
new_text = text[::-1]
if new_text == text:
    print("it is palindrome")
else:
    print("It is not a palindrome")


def check_palindrome(numbers):
    new_num = str(numbers)
    print(new_num)
    new_check = new_num[::-1]
    if new_check == new_num:
        return "yes"
    else:
        return "no"

numbers = 14541
res = check_palindrome(numbers)
print(res)