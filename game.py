from meet import *
ball1={"radius": 50, "x":7, "y":5, "dy":0,"dx":1}

cells=[]
circle1= create_cell(ball1)
cells.append(circle1)
def limits(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		
		if (cell.xcor() > width): 
			cell.set_dx(-cell.get_dx())
		if (cell.ycor() > height):
			cell.set_dy(-cell.get_dy())

while(True):
	move_cells(cells)
	limits(cells)
