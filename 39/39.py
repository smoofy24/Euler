
max_val = [0,0]
list=[]
res_list=[]
UPLIMIT=20

res_list=[0]*UPLIMIT

for x in range(3,UPLIMIT):
#  print("Dealing with ", x," value.")
  for y in range(1,x):
    for z in range(y, x):
      if (y>0) and (z>0) and (x-(y+z)>0):
        tmp_set=[y,z,x-(y+z),x]
        tmp_set.sort()
        print(tmp_set)
        if tmp_set[0]+tmp_set[1]>tmp_set[2]:
          if not tmp_set in list:
            list.append(tmp_set)

for val in list:
  if val[0]**2+val[1]**2==val[2]**2:
    res_list[val[0]+val[1]+val[2]]=res_list[val[0]+val[1]+val[2]]+1

print(res_list)
print(res_list.index(max(res_list)))
