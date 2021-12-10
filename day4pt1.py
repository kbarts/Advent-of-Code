import re

f = open("input4.txt", "r")
lines = f.readlines()
balls = [int(ball) for ball in lines[0].split(',')]
boards = [[[int(num) for num in re.split(r"\s+", line.strip())]
           for line in lines[2 + 6 * i:7 + 6 * i]]
          for i in range(0, (len(lines) - 1) // 6)]

board_segments = boards

for k in range(0,100):
    for j in range(0,5):
        board_segments[k].append([board_segments[k][i][j] for i in range(0,5)])

winning_board_nums = set()
for k in range(0,len(balls)):
  

  for bnum, board in enumerate(board_segments):
      for rc_num, rc in enumerate(board):
          for num, val in enumerate(rc):
              if val == balls[k]:
                  board_segments[bnum][rc_num][num] = 0

  if k >= 4:
    for bnum, board in enumerate(board_segments):
      for rc_num, rc in enumerate(board):
        if sum(rc) == 0:
          winning_board_nums.add(bnum)

    if winning_board_nums:
      for board_num in winning_board_nums:
        winning_sum = 0
        for row_num, row in enumerate(board_segments[board_num][0:5]):
          winning_sum = sum(row, winning_sum) 
        print(winning_sum * balls[k])
        break
      break