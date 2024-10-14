############################################################
# Name: Jennifer Arreola
# Name(s) of anyone worked with:
# Est time spent (hr): 1hr
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel, GPolygon

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a basic rendition of the Antigua-Barbuda Flag.
    Disclaimer:on the actual flag the sun has rays, I just wasn't able to find a way to code this that wasn't gonna take an egragious amount of time findiing the vertexes for the polygon."""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    cx= WIDTH/2
    cy= HEIGHT/2
    
    # red background
    r= GRect(cx-200,cy-150,400,300)
    r.set_fill_color("darkred")
    r.set_filled(True)
    gw.add(r)
    #black triangle
    bt = GPolygon()
    bt.add_vertex(100,150)
    bt.add_vertex(500,150)
    bt.add_vertex(300,450)
    bt.set_fill_color("black")
    bt.set_filled(True)
    gw.add(bt)
    #sun
    s= GOval(cx-45,cy-100, 100, 100)
    s.set_fill_color("Yellow")
    s.set_filled(True)
    gw.add(s)

    #two overlapping triangles
    blt = GPolygon()
    blt.add_vertex(167,250)
    blt.add_vertex(433,250)
    blt.add_vertex(300,450)
    blt.set_fill_color("Blue")
    blt.set_filled(True)
    gw.add(blt)

    wt = GPolygon()
    wt.add_vertex(200,300)
    wt.add_vertex(400,300)
    wt.add_vertex(300,450)
    wt.set_fill_color("White")
    wt.set_filled(True)
    gw.add(wt)
    #label 
    label= GLabel("Antigua-Barbuda", cx-175,cy-175)
    label.set_font("50px 'Times New Roman'")
    label2= GLabel("Flag", cx-40, cy+210)
    label2.set_font("50px 'Times New Roman'")
    gw.add(label)
    gw.add(label2)
    
    l = GLine(100, cy-170, 500,cy-170)
    l2 = GLine(150, cy + 220,450, cy + 220 )
    gw.add(l)
    gw.add(l2)



if __name__ == '__main__':
    draw_image()

