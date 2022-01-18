## 2d robo / matrix
## PART 1

##  * bidimensional lists / arrays - matrix

# LEGEND
# 1 cell - 1m2
# 0 - empty
# 1 - wall
# 2 - robo
# 3 - base
from os import system

room_map = [
    [1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,3,1],
    [1,1,1,1,1,1,1,1,1,1]
]


###### PRINT THE MAP: nested loop ######
system("cls")                                         ### Clear the screen
for ri in range(10):
    for ci in range(10):
        if room_map[ri][ci] == 0:                     ### "." is printed if empty space on the map is identified
            print(".",end=" ")
        elif room_map[ri][ci] == 1:                   ### "#" is printed if an obstacle on the map is identified
            print("#",end=" ")
        elif room_map[ri][ci] == 2:                   ### "R" is printed if robot on the map is identified
            print("R",end=" ")
        elif room_map[ri][ci] == 3:                   ### "B" is printed if base on the map is identified
            print("B",end=" ")
    print("|", ri, end="")                            ### Coordinates of the map's rows are printed

    print() 

print("-"*21)
for ci in range(10):
    print(ci, end=" ")                                ### Coordinates of the map's columns are printed
print()
###### PRINT THE MAP: nested loop ######