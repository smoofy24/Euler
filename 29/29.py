
list =[]

for x in range(2, 101):
  for y in range(2, 101):
    if not (x**y in list):
      list.append(x**y)

print(len(list))

      
