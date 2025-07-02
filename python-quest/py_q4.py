#Write a program to find common elements from 2 lists
#Example - list1 = [2,4,1,6,8,3] list2=[4,2,6,7,5,9] Expected Ans - [2,4,6]

list1 = [2,4,1,6,8,3]
list2=[4,2,6,7,5,9]

combined_list = set(list1) & set(list2)
new_com = list(combined_list)
print(new_com)

common_list = []
for i in list1:
    if i in list2 and i not in common_list:
        common_list.append(i)
print(common_list)


# function

def com_list(lists1, lists2):
    exp_list = []
    for i in lists1:
        if i in lists2 and i not in exp_list:
            exp_list.append(i)
    return exp_list

lists1 = [2,4,1,6,8,3]
lists2=[4,2,6,7,5,9]

print(com_list(lists1, lists2))




