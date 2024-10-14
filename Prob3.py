########################################
# Name: Jennifer Arreola
# Collaborators: CHAT GPT 
# Estimate time spent (hrs): 1.5 hrs
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    def on_mouse_down(event): #defines actions to be taken once mouse is clicked
        x = event.get_x() #gets x-coord of click
        y = event.get_y() #gets y-coord of click
        in_box(x,y) #takes in the click coordinates to check if they're in the box
        label.set_label(str(score)) #sets label to whatever updated score comes out of in_box(x,y)
        box.set_location(get_rx(),get_ry()) #set a new random location for the box using the random x and y coord functions


    gw = GWindow(GW_WIDTH, GW_HEIGHT) #create GWindow
    gw.add_event_listener("click", on_mouse_down) #adds even listener for click

    def get_rx(): #function for random positioning in the x-plane
        return random.randint(0, GW_WIDTH-SQUARE_SIZE)
    def get_ry(): #function for random positioning in the y-plane
        return random.randint(0, GW_HEIGHT-SQUARE_SIZE)
    
    box = GRect(get_rx(), get_ry(), SQUARE_SIZE, SQUARE_SIZE) #create box
    box.set_color("Blue") 
    box.set_filled(True)
    gw.add(box) #add colored box to GWindow

    score = 0 # initialize score
    label= GLabel(str(score), SCORE_DX, GW_HEIGHT-SCORE_DY) #show score from initialization
    label.set_font(SCORE_FONT)
    gw.add(label) #adds score to GWindow both as the initialized and to be updated

    def in_box(x,y): #function checks if the click coordinates are in the box range
        x_range = list(range(box.get_x(), box.get_x()+SQUARE_SIZE+1)) #creates a range of numbers that x or y could fall in to be considered in the box
        y_range = list(range(box.get_y(), box.get_y()+SQUARE_SIZE+1))

        nonlocal score ##CHAT GPT (could'nt figure out how to access the score since I want it to initially display 0 also)

        if x in x_range and y in y_range: #checks if the click is within bounds by checking if it falls within the range
            score += 1 #if criteria is met it adds one point to score
        else: #if criteria not met ie. click was outside of the box score is reset
            score = 0
    




if __name__ == '__main__':
    clicky_box()
