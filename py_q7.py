# Write a prog to remove duplicates from a list.
# using inbuilt method


list1 = [4, 6, 6, 7, 8, 8, 3]
rem_dup = set(list1)
print(list(rem_dup))

new_list = []
ex = [1,3,2,5,6,1,5,8,7]
for i in ex:
    if i not in new_list:
        new_list.append(i)
print(new_list)

def rem_dup(ex):
    exp_list = []
    for i in ex:
        if i not in exp_list:
            exp_list.append(i)
    return exp_list

ex = [1,3,2,5,6,1,5,8,7]
print(rem_dup(ex))


# ex - remove duplicates from string.
# "Today is Thursday. Thursday is a weekday"

str1 = "Today is Thursday. Thursday is a weekday"
dup_rem = []
nor_str = str1.replace(".", "")
new_str = nor_str.split()
print(new_str)
for i in new_str:
    if i not in dup_rem:
        dup_rem.append(i)
print(dup_rem)
final_res = " ".join(dup_rem)
print(final_res)