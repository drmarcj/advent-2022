from sys import stdin

final = 0

for data in stdin:
  if 'A X' in data:  
    final = final + 3 # lose + 1
  elif 'B X' in data:
    final = final + 1 # lose
  elif 'C X' in data:
    final = final + 2 # lose
  elif 'A Y' in data:
    final = final + 4 # draw 3+ 1
  elif 'B Y' in data:
    final = final + 5 # draw 3 + 2
  elif 'C Y' in data: 
    final = final + 6  # draw 3 + 3

  elif 'A Z' in data: 
    final = final + 8 # win 6 +2
  elif 'B Z' in data:
    final = final + 9 # win 6 + 3
  elif 'C Z' in data: 
    final = final + 7 # win 6 + 1

print(final)
