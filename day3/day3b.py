from sys import stdin

result = 0
count = 0

for data in stdin:
  count = count +1
  if count == 1:
  	part1 = data
  elif count == 2:
    part2 = data.strip('\n')
  elif count == 3:
  	part3 = data
  	common = set(part1) & set(part2) & set(part3)
  	print(common)
  	count = 0
  	val = ord(repr(common)[2])
  	if (val > 97):
  	  result = result + val-96
  	elif (val > 10):
   	  result = result + val-38
  	else:
   	  print("*")
  	print (result)
  
  
  