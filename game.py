from meet import *
import meet
from random import randint
cells=[]
colors=["purple","pink","blue","red","yellow","green","orange"]
cells_num= 0

for i in range (15):
	ball1={"radius":randint(9,50), "x":randint(0,50), "y":randint(0,50), "dy":random.randint(-4,1),"dx":random.uniform(0,1),"color":random.choice(colors)}
	cells_num+=1	
	circle =create_cell (ball1)
	cells.append(circle)

user_cell={"radius":randint(5,15), "x":randint(10,10), "y":randint(15,25), "dy":random.randint(-15,-1),"dx":random.uniform(-0.80,0.12),"color":random.choice(colors)}
t=create_cell(user_cell)
cells.append(t)

def limits(cells):
	for cell in cells:
		dx=cell.get_dx()
		dy=cell.get_dy()
		if (meet.get_x(cell)>meet.get_screen_width()): 
			cell.set_dx(-dx)
		elif(meet.get_x(cell)<-meet.get_screen_width()):
			cell.set_dx(-dx)
		if (meet.get_y(cell) > meet.get_screen_height()):
			cell.set_dy(-dy)
		elif(meet.get_y(cell)<-meet.get_screen_height()):
			cell.set_dy(-dy)

	
while(True):
	move_cells(cells)
	limits(cells)
	dx,dy = get_user_direction(t)
	t.set_dx(dx)
	t.set_dy(dy)
	for i in cells:
		r=i.get_radius()
		x=i.xcor()
		y=i.ycor()
		for g in cells:
			r2=g.get_radius()
			x2=g.xcor()
			y2=g.ycor()
			if((x-x2)**2+ (y-y2)**2)**0.5 <= (r-r2):
				if(r > r2):
					g.goto(get_random_x(),meet.get_random_y())
					i.set_radius(r + r2*0.3)
					
				else :
					g.bye()
				 

meet.mainloop()




	



	
