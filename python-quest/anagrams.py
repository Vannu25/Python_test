def if_anagrams(n1, n2):
    if len(n1) != len(n2):
        return False

    ana1 = sorted(n1)
    ana2 = sorted(n2)

    return ana1 == ana2


# Examples:
print(if_anagrams("geeks", "kseeg"))  # True
print(if_anagrams("allergy", "allergic"))  # False
print(if_anagrams("g", "g"))  # True

