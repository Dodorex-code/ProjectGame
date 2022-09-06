import keyboard
import os
import random
import winsound




pcinp = ""
posx = 1
posy = 1
height = 12 #max value 61
width = 18 #max value 118
last_pcinp = ""
base_tile_symbol = "."
base_player_symbol = "@"
base_tree_symbol = "1"
base_exit_symbol = "O"
tree_pos = [[2,1], [4,4], [6,5], [3,8], [4,17], [2,14], [6,9], [9,16], [6,12], [15,3], [13,10], [9,2]]
exitposx = random.randint(3, width -2)
exitposy = random.randint(3, height - 2)

def printpos():
    print(f"x: {str(posx)} y: {str(posy)}")

def update():
    
    os.system('cls')

    printpos()

    for y in range(height):
        for x in range(width):
            tile_symbol = base_tile_symbol
            if y == posy and x == posx:
                tile_symbol = base_player_symbol
            for p in range(len(tree_pos)):
                treex = tree_pos[p][0]
                treey = tree_pos[p][1]
                if y == treey and x == treex:
                    tile_symbol = base_tree_symbol
            if y == exitposy and x == exitposx:
                tile_symbol = base_exit_symbol
            print(tile_symbol, end=" ")
        print()

    winsound.Beep(200,100)

update()

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        pcinp = event.name

    if pcinp == "s":
        if posy < height - 1: 
            posy += 1
            for p in range(len(tree_pos)):
                treex = tree_pos[p][0]
                treey = tree_pos[p][1]
                if posy == treey and posx == treex:
                    posy -= 1
    if pcinp == "w":
        if posy > 0:
            posy -= 1
            for p in range(len(tree_pos)):
                treex = tree_pos[p][0]
                treey = tree_pos[p][1]
                if posy == treey and posx == treex:
                    posy += 1
    if pcinp == "a":
        if posx > 0:
            posx -= 1
            for p in range(len(tree_pos)):
                treex = tree_pos[p][0]
                treey = tree_pos[p][1]
                if posy == treey and posx == treex:
                    posx += 1
    if pcinp == "d":
        if posx < width - 1:
            posx += 1
            for p in range(len(tree_pos)):
                treex = tree_pos[p][0]
                treey = tree_pos[p][1]
                if posy == treey and posx == treex:
                    posx -=1

    if posx >= width:
        posx = width
    if posy >= height:
        posy = height

    if posx == exitposx and posy == exitposy:
        winsound.Beep(400,200)
        os.system('cls')
        os.system('python game.py')

    last_pcinp = pcinp
    update()