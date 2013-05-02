#!python

size = 20

grid = [ [1] * (size+1) ] * (size+1)

for i in range(1,size+1):
    for j in range(1,size+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

        
print "For a grid of size", size, "there are", grid[size][size], "lattice paths"
