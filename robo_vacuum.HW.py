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
from time import sleep

def mapPrint (map,x,y,z):
    for ri in range(10):
        for ci in range(10):
            if robo_r == ri and robo_c == ci:            
                print("R",end=" ")
            elif map[ri][ci] == 0:                   
                print(x,end=" ")
            elif map[ri][ci] == 1:                   
                print(y,end=" ")                 
            elif map[ri][ci] == 3:                  
                print(z,end=" ")
        print("|", ri, end="")                            

        print() 
    
    print("-"*21)
    for ci in range(10):
        print(ci, end=" ")                                ### Coordinates of the map's columns are printed
    print()
room_map = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,3,1],
    [1,1,1,1,1,1,1,1,1,1]
]
# LEGEND
# 0 - not visited
# 1 - visited
robo_steps = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
# LEGEND
# 0 - clean area
# 1 - cleaned area
# 3 - dirty are
dust_map = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,0,3,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

robo_r = 8                                                ### Robot's coordinates
robo_c = 8
robo_steps[robo_r][robo_c] = 1
dust_map[robo_r][robo_c] = 0
score = 0
charge = 3                                                ### %

while True:
    ###### PRINT THE MAP: nested loop ######
    system("cls")                                         ### Clear the screen
    mapPrint(room_map,".","#","B")
    for ri in range(10):
        for ci in range(10):
            if robo_steps[ri][ci] == 0:                   ### "." is printed if robot has not yet visited this place
                print(".",end=" ")
            elif robo_steps[ri][ci] == 1:                 ### "+" is printed if robot has visited this place 
                print("+",end=" ")                 
        print("|", ri, end="")                            ### Coordinates of the map's rows are printed

        print() 

    print("-"*21)
    for ci in range(10):
        print(ci, end=" ")                                ### Coordinates of the map's columns are printed
    print()

    mapPrint(dust_map,"-","*","~")
    print("Current battery level is", charge, " %")
    print("Current score is", score, " points")
    ###### PRINT THE MAP: nested loop ######

    ###### ROBOT MAKES A DECISION ######
    # HIGHEST PRIORITY / plan A
    # up
    if robo_r > 0 and room_map[robo_r-1][robo_c] != 1 and robo_steps[robo_r-1][robo_c] != 1:
        robo_r -= 1
    # right
    elif robo_c < 9 and room_map[robo_r][robo_c+1] != 1 and robo_steps[robo_r][robo_c+1] != 1:
        robo_c += 1
    # down
    elif robo_r < 9 and room_map[robo_r+1][robo_c] != 1 and robo_steps[robo_r+1][robo_c] != 1:
        robo_r += 1
    # left
    elif robo_c > 0 and room_map[robo_r][robo_c-1] != 1 and robo_steps[robo_r][robo_c-1] != 1:
        robo_c -= 1
    # MID PRIORITY / plan B
    # up
    elif robo_r > 0 and room_map[robo_r-1][robo_c] != 1 and robo_steps[robo_r-2][robo_c] != 1:
        robo_r -= 1
    # right
    elif robo_c < 9 and room_map[robo_r][robo_c+1] != 1 and robo_steps[robo_r][robo_c+2] != 1:
        robo_c += 1
    # down
    elif robo_r < 9 and room_map[robo_r+1][robo_c] != 1 and robo_steps[robo_r+2][robo_c] != 1:
        robo_r += 1
    # left
    elif robo_c > 0 and room_map[robo_r][robo_c-1] != 1 and robo_steps[robo_r][robo_c-2] != 1:
        robo_c -= 1
    # LOWER PRIORITY / plan C
    # up
    elif robo_r > 0 and room_map[robo_r-1][robo_c] != 1 and robo_steps[robo_r-3][robo_c] != 1:
        robo_r -= 1
    # right
    elif robo_c < 9 and room_map[robo_r][robo_c+1] != 1 and robo_steps[robo_r][robo_c+3] != 1:
        robo_c += 1
    # down
    elif robo_r < 9 and room_map[robo_r+1][robo_c] != 1 and robo_steps[robo_r+3][robo_c] != 1:
        robo_r += 1
    # left
    elif robo_c > 0 and room_map[robo_r][robo_c-1] != 1 and robo_steps[robo_r][robo_c-3] != 1:
        robo_c -= 1
    # VERY LOW PRIORITY / plan D
    # up
    elif robo_r > 0 and room_map[robo_r-1][robo_c] != 1 and robo_steps[robo_r-4][robo_c] != 1:
        robo_r -= 1
    # right
    elif robo_c < 9 and room_map[robo_r][robo_c+1] != 1 and robo_steps[robo_r][robo_c+4] != 1:
        robo_c += 1
    # down
    elif robo_r < 9 and room_map[robo_r+1][robo_c] != 1 and robo_steps[robo_r+4][robo_c] != 1:
        robo_r += 1
    # left
    elif robo_c > 0 and room_map[robo_r][robo_c-1] != 1 and robo_steps[robo_r][robo_c-4] != 1:
        robo_c -= 1
    # LOWEST PRIORITY / plan E
    # up
    elif robo_r > 0 and room_map[robo_r-1][robo_c] != 1 and robo_steps[robo_r-5][robo_c] != 1:
        robo_r -= 1
    # right
    elif robo_c < 9 and room_map[robo_r][robo_c+1] != 1 and robo_steps[robo_r][robo_c+5] != 1:
        robo_c += 1
    # down
    elif robo_r < 9 and room_map[robo_r+1][robo_c] != 1 and robo_steps[robo_r+5][robo_c] != 1:
        robo_r += 1
    # left
    elif robo_c > 0 and room_map[robo_r][robo_c-1] != 1 and robo_steps[robo_r][robo_c-5] != 1:
        robo_c -= 1

    # remember current step
    robo_steps[robo_r][robo_c] = 1
    ###### ROBOT MAKES A DECISION ######

    sleep(.2)

    ###### SCORE COUNTING         ######
    for p in dust_map:
        if dust_map[robo_r][robo_c] == 3:
            dust_map[robo_r][robo_c] = 1
            score += 1
    ###### SCORE COUNTING         ######

    ###### ENERGY CONSUMPTION     ######
    charge -= 0.1
    if charge < 2:
        print("Battery low!")
        break
    ###### ENERGY CONSUMPTION     ######