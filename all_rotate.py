def generate_rotations(n):
    num_digits = len(str(n))
    for _ in range(num_digits - 1):
        first_digit = n // (10 ** (num_digits - 1))
        n = (n * 10 + first_digit) % (10 ** num_digits)
        print(n, end = ' ')

if __name__ == "__main__":
    n = int(input())
    generate_rotations(n)
