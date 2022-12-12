from sys import stdin

max = 0
sum = 0

for data in stdin:
  if data == '\n':
    if sum > max:
      max = sum
    sum = 0
    
  else:
    sum = sum + int(data)

print(max)
