#!python

size = 20

grid = [ [1] * (size+1) ] * (size+1)

for i in range(1,size+1):
    for j in range(1,size+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

        
print "Lattice Paths: ", grid[size][size]
