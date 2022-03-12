def add_if_not_zero(x,y,g):
    if grid[x][y] != 0:
        grid[x][y] += 1
    return



lines = open('input11.txt','r').readlines()
grid = []
for num, line in enumerate(lines):
    row = []
    for l in line.strip():  
        row.append(int(l))
    grid.append(row)

num_steps = 100
num_flashes = 0

for _ in range(0,num_steps):
    for i,r in enumerate(grid):
        for j,c in enumerate(r):
            grid[i][j] = c + 1

    no_flashes = 0
    while not no_flashes:
        no_flashes = 1
        for i,r in enumerate(grid):
            for j,c in enumerate(r):
                if c > 9:
                    grid[i][j] = 0
                    num_flashes += 1
                    num_rows = len(grid) - 1
                    num_cols = len(grid[0]) - 1
                    if i == 0 and j == 0: #top left corner
                        add_if_not_zero(i,j+1,grid) # mid right
                        add_if_not_zero(i+1,j,grid) # bottom mid
                        add_if_not_zero(i+1,j+1,grid) # bottom right
                    elif i == 0 and j > 0 and j < num_cols: # top row non-corner
                        add_if_not_zero(i,j-1,grid) # mid left
                        add_if_not_zero(i,j+1,grid) # mid right
                        add_if_not_zero(i+1,j-1,grid) # bottom left
                        add_if_not_zero(i+1,j,grid) # bottom mid
                        add_if_not_zero(i+1,j+1,grid) # bottom right
                    elif i == 0 and j == num_cols: # top right corner
                        add_if_not_zero(i,j-1,grid) # mid left
                        add_if_not_zero(i+1,j-1,grid) # bottom left
                        add_if_not_zero(i+1,j,grid) # bottom mid
                    elif i > 0 and i < num_rows and j == 0: # left col non-corner
                        add_if_not_zero(i-1,j,grid) # top mid
                        add_if_not_zero(i-1,j+1,grid) # top right
                        add_if_not_zero(i,j+1,grid) # mid right
                        add_if_not_zero(i+1,j,grid) # bottom mid
                        add_if_not_zero(i+1,j+1,grid) # bottom right
                    elif i > 0 and i < num_rows and j > 0 and j < num_cols: # central
                        add_if_not_zero(i-1,j-1,grid) # top left
                        add_if_not_zero(i-1,j,grid) # top mid
                        add_if_not_zero(i-1,j+1,grid) # top right
                        add_if_not_zero(i,j-1,grid) # mid left
                        add_if_not_zero(i,j+1,grid) # mid right
                        add_if_not_zero(i+1,j-1,grid) # bottom left
                        add_if_not_zero(i+1,j,grid) # bottom mid
                        add_if_not_zero(i+1,j+1,grid) # bottom right
                    elif i > 0 and i < num_rows and j == num_cols: # right col non-corner
                        add_if_not_zero(i-1,j-1,grid) # top left
                        add_if_not_zero(i-1,j,grid) # top mid
                        add_if_not_zero(i,j-1,grid) # mid left
                        add_if_not_zero(i+1,j-1,grid) # bottom left
                        add_if_not_zero(i+1,j,grid) # bottom mid
                    elif i == num_rows and j == 0: # bottom left corner
                        add_if_not_zero(i-1,j,grid) # top mid
                        add_if_not_zero(i-1,j+1,grid) # top right
                        add_if_not_zero(i,j+1,grid) # mid right
                    elif i == num_rows and j > 0 and j < num_cols: # bottom row non-corner
                        add_if_not_zero(i-1,j-1,grid) # top left
                        add_if_not_zero(i-1,j,grid) # top mid
                        add_if_not_zero(i-1,j+1,grid) # top right
                        add_if_not_zero(i,j-1,grid) # mid left
                        add_if_not_zero(i,j+1,grid) # mid right
                    elif i == num_rows and j == num_cols: # bottom right corner
                        add_if_not_zero(i-1,j-1,grid) # top left
                        add_if_not_zero(i-1,j,grid) # top mid
                        add_if_not_zero(i,j-1,grid) # mid left              

                    no_flashes = 0
                    break
            if not no_flashes:
                break
for r in grid:
    print(r)

print(num_flashes)



            