def func(a,b=2,c=3):
    print(f" the numbers : {a},{b},{c}")
    return a+b+c


print(func(1))


strr = "AABBCDD"
char_count = {}

for i in strr:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

# Only print characters with count > 1
for char, count in char_count.items():
    if count > 1:
        print(f"{char}{count}", end='')
    if count == 1:
        print(f"{char}", end= '')



