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

def dpl(list):
    new_list = []
    prev_num = 0

    for i in list:
        if i != prev_num:
            new_list.append(i**list.count(i))
        prev_num = i

    return new_list



prev_list = []
cnt = 0
win = []
index = 1
lim = 5

#for index in range(1, 1000):
while cnt < lim-1:
#    print("Trying number", index)
    dpf = dpl(mylib.get_fracts(index))
    
#    print("Comparing",dpf,"with",prev_list)
    if len(prev_list) != len(dpf) or common_data(prev_list, dpf) or not dpf or len(dpf) != lim:
#        print("Erasing counter")
        cnt = 0
        win = [index]
    else:
        cnt = cnt + 1
#        print("Rising counter to",cnt)
        win.append(index)

    prev_list = dpf
    index = index + 1

print(win)

    
