import re

f = open("input4.txt", "r")
lines = f.readlines()
balls = [int(ball) for ball in lines[0].split(',')]
boards = [[[int(num) for num in re.split(r"\s+", line.strip())]
           for line in lines[2 + 6 * i:7 + 6 * i]]
          for i in range(0, (len(lines) - 1) // 6)]

board_segments = boards

for k in range(0, 100):
    for j in range(0, 5):
        board_segments[k].append(
            [board_segments[k][i][j] for i in range(0, 5)])

winning_board_nums = {}
for ball_num in range(0,len(balls)):
    for bnum, board in enumerate(board_segments):
        for rc_num, rc in enumerate(board):
            for num, val in enumerate(rc):
                if val == balls[ball_num]:
                    board_segments[bnum][rc_num][num] = -1

    if ball_num >= 4:
        for bnum, board in enumerate(board_segments):
            if bnum not in winning_board_nums:
                for rc_num, rc in enumerate(board):
                    if sum(rc) == -5:
                        winning_board_nums[bnum] = ball_num
                        break

    if len(winning_board_nums) == len(board_segments):
        break

last_entry = (0, 0)
for board_num, ball_num in winning_board_nums.items():  
    if last_entry[1] < ball_num:
        last_entry = (board_num, ball_num)

print(last_entry)
winning_sum = 0
for row_num, row in enumerate(board_segments[last_entry[0]][0:5]):
    for val in row:
        if val != -1:
            winning_sum += val
print(winning_sum * balls[last_entry[1]])