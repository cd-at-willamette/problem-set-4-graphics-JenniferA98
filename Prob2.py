########################################
# Name: Jennifer Arreola
# Collaborators:
# Estimated time spent (hrs): 2 hrs
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    gw = GWindow(WIDTH, HEIGHT) #creates GWindow
    cx = WIDTH/2 #establishes the center of in the x coordinate plane
    cy= (HEIGHT - (BRICK_HEIGHT * BRICKS_IN_BASE))/2 #establish a center in the y coordinate plane based off the projected space the pyramid will take

    def brick(x:int,y:int): # code to create a singular brick that takes in the positions as arguments
        b = GRect(x,y, BRICK_WIDTH, BRICK_HEIGHT) # creates the brick with the pre determinded size
        gw.add(b) #adds brick to GWindow
    
    for r in range(BRICKS_IN_BASE): #creates the rows stacked of bricks by updating the y coordinate position
        y = cy + BRICK_HEIGHT * r #updates the y coordinate position by moving down a row based on BRICK_HEIGHT
        x0 = cx - (r * BRICK_WIDTH) / 2 # finds the center position of each row based off the width space the current row(r) will take
        for i in range(r+1): #creates the brick joined rows by updating the amound of bricks to be made, the argument is r+1 becuase the position of the x has to be updated from the first row
            x = x0 + (i * BRICK_WIDTH) #updates the x position based off the amount of bricks in that row, incrementing the position for each consecutive brick based on the amount of bricks that have been placed before it
            brick(x,y) #places a brick in the updated position incremently






if __name__ == '__main__':
    draw_pyramid()
