def brixUsed(available, size, goal):
  maxBrix = int(goal/size)
  if maxBrix > available:
    return available
  else:
    return maxBrix


def make_bricks(small, big, goal):
  bigUsed = brixUsed(big, 5, goal)
  goal = goal - (bigUsed*5)
  smallUsed = brixUsed(small, 1, goal)
  goal = goal - (smallUsed * 1)
  if goal:
    return False
  else:
    return True
  
make_bricks(3, 1, 8)
make_bricks(1, 4, 12)
make_bricks(43, 1, 46)
make_bricks(0, 2, 10) 
make_bricks(1000000, 1000, 1000100)
make_bricks(2, 1000000, 100003) 