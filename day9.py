lines = open('input9.txt','r').readlines()
mat = []
for num, line in enumerate(lines):
    mat.append([])
    for i in line.strip():
        mat[num].append(int(i))

low_points = []

risk_level_sum = 0
for row, vals in enumerate(mat):
    for col, val in enumerate(vals):
        if row == 0:
            top = 9
            bottom = mat[row +1][col]
        elif row == len(mat)-1:
            bottom = 9
            top = mat[row - 1][col]
        else:
            bottom = mat[row + 1][col]
            top = mat[row - 1][col] 
        
        if col == 0:
            left = 9
            right = mat[row][col+1]
        elif col == len(vals)-1:
            right = 9
            left = mat[row][col-1]
        else:
            right = mat[row][col +1]
            left = mat[row][col -1]
        if val < top and val < bottom and val < left and val < right:
            low_points.append((row, col))

num_rows = len(mat)
num_cols = len(mat[0])
def scan_point(point, basin):
    (row,col) = point
    if mat[row][col] == 9:
        return
    elif point in basin:
        return
    else:
        basin.add(point)
        if row != 0:
            scan_point((row-1, col), basin)
        if row != num_rows - 1:
            scan_point((row+1, col), basin)
        if col != 0:
            scan_point((row, col-1), basin)
        if col != num_cols -1:
            scan_point((row, col+1), basin)
    
# top 0 right 1 bottom 2 left 3
basins = []
for low_point in low_points:
    basin = set()
    scan_point(low_point, basin)
    basins.append(basin)

basin_sizes = []
for basin in basins:
    basin_sizes.append(len(basin))


top_three_basins_product = 1
for j in range(0,3):
    max_bs = (0,0)
    for i, bs in enumerate(basin_sizes):
        if bs > max_bs[0]:
            max_bs = (bs, i)
    top_three_basins_product *= max_bs[0]
    basin_sizes[max_bs[1]] = 0
print(top_three_basins_product)
