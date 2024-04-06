import mylib
import math

def common_data(list1, list2):
    result = False

    # traverse in the 1st list
    for x in list1:

        # traverse in the 2nd list
        for y in list2:

            # if one common
            if x == y:
                result = True
                return result

    return result

cnt = 0
index = 10
prev_list = []
new_list = []
prev_number = 2

while cnt != 3:
    print("Testing for number", index)
    lister = mylib.get_fracts(index)
    print("Fractions are", lister)
    print("Counter is",cnt)
    new_list = []
    old_num = 0

    for i in lister:
        if old_num != i:
            new_list.append(i**lister.count(i))
        old_num = i

    print(new_list, prev_list)
    if len(new_list) != len(prev_list):
        index = index+1
        prev_list = new_list
        cnt = 0
        continue

    print("Compare",new_list,"with", prev_list)
    if not common_data(new_list, prev_list) and len(new_list) == 3:
        cnt = cnt+1
    else:
        cnt = 0

    prev_list = new_list
    index = index + 1
