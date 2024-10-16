
# OPENING THE FILE
file_object = open('test1.txt', encoding='utf8')
data = file_object.read()

# CONVERTING IT TO 2D AND 1D ARRAY
array_2d = [row.split(',') for row in data.split('\n')]
array_1d = [item for sublist in array_2d for item in sublist]

# CREATING A COPY AND WORKING ON IT
a = array_1d.copy()

# SEPARATING THEM FOR EACH COORDINATE
l=[]
for i in range(len(a)):
  l.append(list(a[i]))

# LOOKING FOR THE START POSITION
for i in range(len(l)):
  for j , value in enumerate(l[i]):
    if value == 'S':
      Start = (i,j)

# LOOKING FOR THE END POSITION
for i in range(len(l)):
  for j , value in enumerate(l[i]):
    if value == 'E':
      End = (i ,j)

# CONVERTING THE VALUES TO 0 AND 1
for i in range(len(l)):
  for j in range(len(l[i])):
    if l[i][j] == '.':
      l[i][j] = 0
    elif l[i][j] == '#':
      l[i][j] = 1
    elif l[i][j] == 'S':
      l[i][j] = 0
    elif l[i][j] == 'E':
      l[i][j] = 0

# DEFINING THE ACTIONS
directions = [(-1, 0), (1, 0), (0, -1),(0, 1)]

# CREATING THE SOLVE FUNCTION
def solve(maze,start,end):
  Answers=[]
  visited = []
  rows, cols = len(maze), len(maze[0])
  path=[]
  path.append(start)
  current = path[-1]
  visited.append(current)
  i=0
  q=0
  while path:
    current = path[-1]
    if q==1:
      path.pop()
    if current == end :
      return path
    for direction in directions:
      row, col = current[0] + direction[0], current[1] + direction[1]
      q=1
      if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0 and (row, col) not in visited:
        path.append((row,col))
        visited.append((row, col))
        q=0
        break
  return None
path = solve(l, Start, End)

# CONVERTING THE COORDINATES IN THE PATH TO PRE-DEFINED MOVES
moves=[]
if path:
  for i in range(len(path)):
    if i == len(path)-1:
      break
    moves.append((path[i+1][0]-path[i][0],path[i+1][1]-path[i][1]))

# CONVERTING THE MOVES TO HUMAN-LANGUAGE WORDS
for i in range(len(moves)):
  if moves[i] == (-1,0):
    moves[i] = 'UP'
  elif moves[i] == (1,0):
    moves[i] = 'DOWN'
  elif moves[i] == (0,-1):
    moves[i] = 'LEFT'
  elif moves[i] == (0,1):
    moves[i] = 'RIGHT'

# PRINTING THE RESULTS
if moves == []:
  print('No moves')
else:
  print(moves)

