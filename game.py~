from meet import *
import meet
from random import randint
cells=[]
colors=["purple","pink","blue","red","yellow","green","orange"]
cells_num= 0
balls1={'radius':20,'x': 0,'y':-220,'dx':0,'dy':0,'color':'pink'}

for i in range (15):
	ball1={"radius":random.randint(0,30), "x":random.randint(-200,100), "y":random.randint(-200,100), "dy":random.randint(-2,2),"dx":random.uniform(-2,2),"color":random.choice(colors)}
	cells_num+=1	
	circle =create_cell (ball1)
	cells.append(circle)

user_cell={"radius":20.2, "x":500, "y":500, "dy":random.randint(-15,-1),"dx":random.uniform(-0.80,0.12),"color":random.choice(colors)}
t=create_cell(user_cell)
cells.append(t)

def limits(cells):
	for cell in cells:
		sw=meet.get_screen_width()
		sh=meet.get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (x > sw): 
			cell.set_dx(-cell.get_dx())
		if (y > sh):
			cell.set_dy(-cell.get_dy())
		if (x < -sw):
			cell.set_dx(-cell.get_dx())
		if (y < -sh):
			cell.set_dy(-cell.get_dy())

	
while True:
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
				else: 
					pass#exit()	

						
					
				#else :
					#g.bye()		 

meet.mainloop()




	



	
