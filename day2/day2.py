from sys import stdin

final = 0

for data in stdin:
  if 'A X' in data:  
    final = final + 4 # tie 3 + 1
  elif 'A Y' in data:
    final = final + 8 # win 6 + 2
  elif 'A Z' in data: 
    final = final + 3 # lose 0 + 3
  elif 'B X' in data:
    final = final + 1 # lose 0 + 1
  elif 'C X' in data:
    final = final + 7 # win 6 + 1
  elif 'B Y' in data:
    final = final + 5 # tie 3 + 2
  elif 'B Z' in data:
    final = final + 9 # win 6 + 3
  elif 'C Y' in data: 
    final = final + 2  # lose 0 + 2
  elif 'C Z' in data: 
    final = final + 6 # tie 3 + 3

print(final)
