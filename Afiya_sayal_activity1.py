from turtle import Turtle, Screen
sc = Screen()
harry = Turtle()
harry.shape("turtle")
harry.left(180)
harry.speed(5) # increases the speed of turtle from default 1 to 5
leg_height = 50
length = 250
breadth = 100
height_layer = 20
length_layer = 100
tray_length = 125
tray_height = 10
radius = 10
cherry_radius = 5
extent = 180
x_tab = 200
x_t = -15
kx = 1000
ky = 1000

table_color = "black"
lcolor_1 = "white"
lcolor_2 = "yellow"
lcolor_3 = "brown"
lcolor_4 = "pink"
cherry_color = "red"
tray_color = "white"
frosting_color = "white"

def draw_table(leg_height, table_color, breadth, length):
    '''
    This function is used to draw a table with 4 legs 
    leg_height: int
    table_color: string
    breadth: int
    length: int
    '''
    harry.up()
    harry.fd(x_tab)
    harry.down()
    harry.right(90)
    harry.begin_fill() # gives turtle the signal to fill the rectangle after it is drawn
    harry.fillcolor(table_color)
    harry.fd(leg_height + 10) # draws the tables legs
    harry.right(60)
    harry.fd(breadth)
    harry.right(120)
    harry.fd(leg_height + 10)
    harry.right(180)
    harry.fd(leg_height + 10)
    harry.right(90)
    harry.fd(length)
    harry.right(90)
    harry.fd(leg_height + 10)
    harry.right(180)
    harry.fd(leg_height + 10)
    harry.left(125)
    harry.fd(breadth - 10)
    harry.left(55)
    harry.fd(leg_height + 10)
    harry.right(180)
    harry.fd(leg_height + 10)
    harry.left(90)
    harry.fd(length + 12.5)
    harry.end_fill() # tells turtle to stop filling the rectangle
    harry.left(90)
    harry.fd(leg_height+5)
    harry.right(90)
    harry.up()
    harry.goto(0,leg_height + height_layer) # moves turtle to a position above the table suitable for the tray
    harry.down()

def draw_tray(tray_length, tray_height, tray_color):
    '''
    This function draws the tray on the table
    tray_length: int
    tray_height: int
    tray_color: string
    '''
    harry.begin_fill()
    harry.fillcolor(tray_color)
    harry.fd(tray_length)
    harry.right(90)
    harry.fd(tray_height)
    harry.right(90)
    harry.fd(tray_length)
    harry.right(90)
    harry.fd(tray_height)
    harry.right(90)
    harry.fd(tray_length)
    harry.end_fill()
    harry.up()
    harry.goto(x_t,leg_height + height_layer) # moves turtle to the bottom right edge of the tray
    harry.right(90)
    harry.fd(tray_height) # moves turtle to suitable position to draw the cake
    harry.left(90)
    harry.down()

def draw_layer(length_layer, height_layer,layer_color):
    '''
    This function draws the cake layer 
    length_layer: int
    height_layer: int
    layer_color: string
    '''
    harry.begin_fill()
    harry.fillcolor(layer_color)
    harry.fd(length_layer)
    harry.right(90)
    harry.fd(height_layer)
    harry.right(90)
    harry.fd(length_layer)
    harry.right(90)
    harry.fd(height_layer)
    harry.right(90)
    harry.fd(length_layer)
    harry.end_fill()

def stack_layer():
    '''
    This function stacks the layers on top of each other
    '''
    harry.right(90)
    harry.fd(height_layer) # moves turtle up by the height of the layer 
    harry.left(90)
    harry.bk(length_layer) # moves turtle backwards to the start of the layer

def draw_frosting(radius,extent):
    '''
    This function draws the frosting on the cake
    radius: int
    extent: int(degrees)
    '''
    harry.begin_fill()
    harry.fillcolor(frosting_color)
    harry.circle(radius, extent) # draws only half a circle as extent = 180
    harry.end_fill()
    harry.right(180)

def draw_cherry(cherry_color, cherry_radius):
    '''
    This function draws the small cherry on top of the cake
    cherry_color: string
    cherry_radius: int
    '''
    harry.right(90)
    harry.fd(length_layer)
    harry.right(180)
    harry.fd(length_layer)
    harry.right(180)
    harry.fd(length_layer/2) # moves turtle to the center of the top layer
    harry.right(180)
    harry.begin_fill()
    harry.fillcolor(cherry_color)
    harry.circle(cherry_radius)
    harry.end_fill()

def main():
    '''
    Finally, this function calls upon all previously defined functions to draw a cake
    '''
    draw_table(leg_height, table_color, breadth, length)
    draw_tray(tray_length, tray_height, tray_color)
    draw_layer(length_layer, height_layer, lcolor_1)
    stack_layer()
    draw_layer(length_layer, height_layer, lcolor_2)
    stack_layer()
    draw_layer(length_layer, height_layer, lcolor_3)
    stack_layer()
    draw_layer(length_layer, height_layer, lcolor_4)
    harry.right(90)
    harry.fd(height_layer)  # these 3 code move turtle to the left of the top layer in a position to draw the frosting
    harry.left(180)
    draw_frosting(radius,extent)
    draw_frosting(radius,extent)
    draw_frosting(radius,extent)
    draw_frosting(radius,extent)
    draw_frosting(radius,extent)
    draw_cherry(cherry_color, cherry_radius)
    harry.up()
    harry.goto(kx,ky)

    sc.exitonclick()

if __name__ == "__main__":
    main()