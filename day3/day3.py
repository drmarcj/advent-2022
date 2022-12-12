from sys import stdin

result = 0

for data in stdin:
  l = int(len(data)/2)
  part1 = data[0:l] 
  part2 = data[l:]
  common = set(part1) & set(part2)
  print(common)
  val = ord(repr(common)[2])

  if (val > 97):
  	result = result + val-96
  elif (val > 10):
  	result = result + val-38
  else:
  	print("*")
print (result)
  
  
  