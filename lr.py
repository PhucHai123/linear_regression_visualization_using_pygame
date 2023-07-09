import pygame
import math
import numpy as np
from sklearn import linear_model

class Draw_panel:
	def __init__(self,BLUE,RED,BLACK,GREY,YELLOW,GREEN,BACKGROUP):
		self.BLUE = BLUE
		self.RED = RED
		self.BLACK = BLACK
		self.GREY = GREY
		self.YELLOW = YELLOW
		self.GREEN = GREEN
		self.BACKGROUP = BACKGROUP

def color():
	BLUE = (0,0,153)
	RED = (204,0,0)
	BLACK = (0,0,0)
	GREY = (192,192,192)
	YELLOW = (255,255,0)
	GREEN = (0,102,0)
	BACKGROUP = (255,255,255)
	return Draw_panel(BLUE,RED,BLACK,GREY,YELLOW,GREEN,BACKGROUP)

def calc_linear_ressgrion(x,y):
	A = np.array([x]).T
	b = np.array([y]).T
	x0 = [min(x),max(x)]
	ones = np.ones((A.shape[0],1), dtype=np.int8)
	A = np.concatenate((A, ones), axis =1)
	x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
	y01 = x[1][0] + x[0][0]*x0[0]
	y02 = x[1][0] + x[0][0]*x0[1]
	return (x0[0],y01,x0[1],y02,x[0][0],x[1][0])

def calc_error(points,a,b):
	init = 0
	for i in range(len(points)):
		y = points[i][0]*a + b
		init += abs(points[i][1] - y)
	return init

def lr(x,y):
	A = np.array([x]).T
	b = np.array([y]).T
	lr = linear_model.LinearRegression()
	lr.fit(A,b)
	x0  = min(x)
	y0 = x0*lr.coef_[0][0] + lr.intercept_[0]
	x = max(x)
	y = x*lr.coef_[0][0] + lr.intercept_[0]
	return (x0,y0,x,y,lr.coef_[0][0],lr.intercept_[0])

def init(running,screen,clock,COLORS,ox,oy,points,x,y,list_value,CLEAR_BUTTON,font,list_distance,
		TITLE,init_value,name_ox,name_oy,font_new,error_lr,list_error_lr,list_value_result,reset_button,font_note,
		font_recipe,font_library,list_error_note,list_error_data,font_data_point):
	
	while running:
		clock.tick(60)
		screen.fill(COLORS.BACKGROUP)
		x_mouse,y_mouse = pygame.mouse.get_pos()

		pygame.draw.rect(screen,COLORS.BLACK,(45,645,1150,50))
		
		pygame.draw.line(screen,COLORS.BLACK,(50,50),(50,600),3)
		pygame.draw.line(screen,COLORS.BLACK,(50,600),(1100,600),3)
		screen.blit(ox,(44,32))
		screen.blit(oy,(1100,588))

		pygame.draw.rect(screen,COLORS.GREY,(190,650,90,40))
		screen.blit(CLEAR_BUTTON,(200,655))

		pygame.draw.rect(screen,COLORS.GREY,(50,650,130,40))
		screen.blit(font_recipe,(55,655))
		
		pygame.draw.rect(screen,COLORS.GREY,(290,650,150,40))

		pygame.draw.rect(screen,COLORS.GREY,(450,650,130,40))
		screen.blit(font_library,(455,655))

		pygame.draw.rect(screen,COLORS.GREY,(590,650,80,40))
		screen.blit(CLEAR_BUTTON,(595,655))

		pygame.draw.rect(screen,COLORS.GREY,(680,650,505,40))

		pygame.draw.rect(screen,COLORS.GREY,(1100,10,90,30))
		screen.blit(reset_button,(1115,13))

		pygame.draw.rect(screen,COLORS.GREY,(900,500,195,95))
		screen.blit(font_data_point,(905,520))
		pygame.draw.circle(screen,COLORS.RED,(1048,533),7)
		screen.blit(font_note,(905,500))
		screen.blit(font_recipe,(905,545))
		pygame.draw.line(screen,COLORS.BLACK,(1020,557),(1080,557),4)
		screen.blit(font_library,(905,570))
		pygame.draw.line(screen,COLORS.BLUE,(1020,582),(1080,582),4)

		screen.blit(TITLE,(250,610))
		screen.blit(init_value,(40,595))
		screen.blit(name_ox,(35,40))
		screen.blit(name_oy,(1095,600))

		if 50 <= x_mouse <=1100 and 50 <= y_mouse <= 600:
			text_mouse = font.render("(" + "x=" + str((x_mouse -50)) + "," + "y = " + str(abs(y_mouse-600)) + ")",True,COLORS.BLACK)
			screen.blit(text_mouse, (x_mouse + 10, y_mouse))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if 50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600:
					point = [x_mouse - 50,abs(y_mouse - 600)]
					points.append(point)
					x.append(float((x_mouse-50)/10))
					y.append(float(abs(y_mouse - 600)/10))

				if 50 <= x_mouse <= 180  and 650 <= y_mouse <= 690:
					try:
						(x1,y1,x2,y2,a,b)  = calc_linear_ressgrion(x,y)
						save_value = [x1,y1,x2,y2]
						list_value_result.append(save_value)
						calc_sum_error = calc_error(points,a,b)
						list_distance.append(calc_sum_error)
						
						if points == []:
							list_value_result = []
							list_error_lr.append(error_lr)
						
					except:
						list_error_lr.append(error_lr)

				if 900 <= x_mouse <= 1095 and 500 <= y_mouse <= 595:
					error_note = "Error: Don't write in the comments"
					list_error_note.append(error_note)
					points = []
	
				if 190 <= x_mouse <= 280  and 650 <= y_mouse <= 690:
					list_value_result = []
					list_distance = []

				if 450 <= x_mouse <= 580 and 650 <= y_mouse <= 690:
					try:
						a,b,c,d,e,f = lr(x,y)
						consts = [a,b,c,d]
						list_value.append(consts)
						calc_sum_error = calc_error(points,e,f)
						list_distance.append(calc_sum_error)
						if points == []:
							list_value = []
							list_error_lr.append(error_lr)

					except:
						list_error_lr.append(error_lr)

				if 590 <= x_mouse <= 780 and 650 <= y_mouse <= 690:
					list_value = []
					list_distance = []
				if 1100 <= x_mouse <= 1190 and 10 <= y_mouse <= 40:
					list_value = []
					list_distance = []
					list_value_result = []
					list_distance = []
					points = []
					list_error_lr = []
					list_error_note = []

					
		for i in range(len(points)):
			pygame.draw.circle(screen,COLORS.RED,(points[i][0] + 50 ,600 - points[i][1]),7)

		for i in range(len(list_value_result)):
			pygame.draw.line(screen,COLORS.BLACK,(list_value_result[i][0]*10 + 50, 600 - list_value_result[i][1]*10),(list_value_result[i][2]*10 + 50 ,600 - list_value_result[i][3]*10),4)

		error = 0
		for i in range(len(list_distance)):
			error += list_distance[i]

		error_button = font.render("Error = " + str(int(error)),True,COLORS.BLACK)
		screen.blit(error_button,(295,655))


		for i in range(len(list_error_lr)):
			error_new = font_new.render(str(list_error_lr[i]),True,COLORS.RED)
			screen.blit(error_new,(685,655))
		
		for i in range(len(list_error_note)):
			error_note = font_new.render(str(list_error_note[i]),True,COLORS.RED)
			screen.blit(error_note,(685,655))

		for i in range(len(list_error_data)):
			error_data = font_new.render(str(list_error_data[i]),True,COLORS.RED)
			screen.blit(error_data,(685,655))

		for i in range(len(list_value)):
			pygame.draw.line(screen,COLORS.BLUE,(list_value[i][0]*10 + 50,600 - list_value[i][1]*10),(list_value[i][2]*10 + 50,600 - list_value[i][3]*10),4)

		pygame.display.flip()
	pygame.quit()
	

def main():
	pygame.init()
	screen = pygame.display.set_mode((1200,700))
	COLORS = color()
	clock = pygame.time.Clock()

	running = True

	error_lr = "Error: No data for linear regression"
	font = pygame.font.SysFont('sans',20)
	font_new = pygame.font.SysFont('san',40)
	ox = font.render("▲",True,COLORS.BLACK)
	oy = font.render("►",True,COLORS.BLACK)
	CLEAR_BUTTON = font.render("Clear line",True,COLORS.BLACK)
	TITLE = font_new.render("Graph illustrating linear regression algorithm",True,COLORS.BLACK)
	init_value = font.render("0",True,COLORS.BLACK)
	name_ox = font.render("x",True,COLORS.BLACK)
	name_oy = font.render("y",True,COLORS.BLACK)
	reset_button = font.render("RESET",True,COLORS.BLACK)
	font_note = font.render("Note",True,COLORS.BLACK) 
	font_recipe = font.render("Predict recipe",True,COLORS.BLACK)
	font_library = font.render("Predict library",True,COLORS.BLACK)
	font_data_point = font.render("Data point",True,COLORS.BLACK)
	
	points = []
	x = []
	y = []
	list_value = []
	list_distance = []
	list_error_lr = []
	list_value_result = []
	list_error_note = []
	list_error_data = []
	
	init(running,screen,clock,COLORS,ox,oy,points,x,y,list_value,CLEAR_BUTTON,font,list_distance,
		TITLE,init_value,name_ox,name_oy,font_new,error_lr,list_error_lr,list_value_result,reset_button,font_note,
		font_recipe,font_library,list_error_note,list_error_data,font_data_point)
	
main()
						