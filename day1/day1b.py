from sys import stdin

elves = []
tot = 0

for data in stdin:
  if data == '\n':
    elves.append(tot)
    tot = 0
    
  else:
    tot = tot + int(data)

elves.sort(reverse=True)
print( sum(elves[0:3]))
