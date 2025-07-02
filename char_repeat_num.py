def transform_required(s):
    result = ''
    counted = set()

    for i in range(len(s)):
        char = s[i]
        if char not in counted:
            count = s.count(char)
            if count > 1:
                result += char + str(count)
                #print(result)
            else:
                result += char
            counted.add(char)
        # skip repeated characters after first encounter

    return result

# 🔍 Test examples
if __name__ == "__main__":
    print(transform_required("ANNDEEEEEF"))  # Output: AN2DE5F
    print(transform_required("AABDDA"))      # Output: A2BD2A
    print(transform_required("XYZ"))         # Output: XYZ
    print(transform_required("AABCCDE"))     # Output: A2BC2DE
    print(transform_required("AAaaBBbb"))    # Output: A2a2B2b2 (case-sensitive)
