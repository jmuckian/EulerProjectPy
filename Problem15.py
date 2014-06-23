"""
Starting in the top left corner of a 2 2 grid, there are 6 routes (without backtracking) to the
bottom right corner.

How many routes are there through a 20 20 grid?
"""

"""
cells = 10
paths = []
lastcell = cells - 1
currentcell = 0
totalpaths = 1          # Set to 1 to account for the initial state


for cell in range(cells):
    paths.append(cells)
    

while currentcell >= 0:
    if currentcell == lastcell:                         # If this is the last cell
        while paths[currentcell] > 0:                   # while the last cell is greater than 0
#            print paths
            paths[currentcell] -= 1                     # Count down 1 in the current cell
            totalpaths += 1                             # And add 1 to the total
    if paths[currentcell] == 0:                         # If the current cell equals 0
        currentcell -= 1                                # Step back one cell
    elif paths[currentcell] > 0:                        # If the current cell is greater than 0
        if paths[currentcell + 1] != 0:                 # And if the next cell does not equal 0
            currentcell += 1                            # Step into the next cell
        elif paths[currentcell + 1] == 0:               # But if the next cell does equal 0
#            print paths
            paths[currentcell] -= 1                     # Count down 1 in the current cell
            totalpaths += 1                             # Add that 1 to the total
            currentcount = paths[currentcell]           # Reset the count to the current cell total
            while currentcell < lastcell:               # And until we get beyond the last cell
                currentcell += 1                        # Step into the next cell
                paths[currentcell] = currentcount       # Reset the current cell to the last cell
                
    
print totalpaths
"""

currentcell = 1.0
cellpaths = 2.0

while currentcell < 20.0:
    currentcell += 1.0
    cellpaths = cellpaths * (4.0 - 2.0/currentcell)
    print (currentcell, cellpaths)
    
    