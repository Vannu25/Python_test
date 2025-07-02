def left_shift_numbers(n):
    s = str(n) #convert the num to str
    length = len(s)
    print(length)

    for i in range(1, length):  # skip the original number (i=0)
        rotated = s[i:] + s[:i]
        print(int(rotated), end=' ')

# Example usage
n = int(input("enter num: "))
left_shift_numbers(n)

