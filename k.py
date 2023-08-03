import pygame 
import math
import numpy as np
from sklearn import linear_model

#Khởi tạo lên các thuộc tính của màu sử dụng trong giao diện
class Color:
	def __init__(self,BLUE,RED,BLACK,GREY,GREEN,BACKGROUP):
		self.BLUE = BLUE
		self.RED = RED
		self.BLACK = BLACK
		self.GREY = GREY
		self.GREEN = GREEN
		self.BACKGROUP = BACKGROUP

#Hàm khởi tạo lên các màu của giao diện
def color():
	BLUE = (0,0,153)
	RED = (204,0,0)
	BLACK = (0,0,0)
	GREY = (192,192,192)
	GREEN = (0,102,0)
	BACKGROUP = (255,255,255)
	return Color(BLUE,RED,BLACK,GREY,GREEN,BACKGROUP)

#Khởi tạo lên các thuộc tính ban đầu
class Init:
	def __init__(self,screen,color,x_init,y_init):
		self.screen = screen
		self.color = color
		self.x_init = x_init
		self.y_init = y_init

class Draw_panel(Init):
	def __init__(self,screen,color,x_init,y_init,ox_max):
		super().__init__(screen,color,x_init,y_init)
		self.ox_max = ox_max

	def draw_ox_oy(self):
		pygame.draw.line(self.screen , self.color,(self.x_init , self.y_init),(self.ox_max , self.y_init),4)
		pygame.draw.line(self.screen , self.color,(self.x_init , self.y_init),(self.x_init , self.x_init),4)

class Draw_button(Init):
	def __init__(self,screen,color,x_init,y_init,x_max,Length,width,GREY):
		super().__init__(screen,color,x_init,y_init)
		self.x_max = x_max
		self.Length = Length
		self.width = width
		self.GREY = GREY

	def BACKGROUP_BUTTON(self):
		pygame.draw.rect(self.screen , self.color,(self.x_init ,self.y_init + 40, self.x_max - 195,self.width + 10))

	def button_result_1(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 5 ,self.y_init + 45,self.Length + 20,self.width))

	def button_clearn_line_1(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 130 ,self.y_init + 45,self.Length + 20,self.width))

	def button_error(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 255 ,self.y_init + 45,self.Length + 80,self.width))

	def button_result_2(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 440 ,self.y_init + 45,self.Length + 30,self.width))

	def button_clearn_line_2(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 575 ,self.y_init + 45,self.Length + 20,self.width))

	def button_reset(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 700 ,self.y_init + 45,self.Length,self.width))

	def Show_when_error(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 805 ,self.y_init + 45,self.Length + 395,self.width))

	def font_note(self):
		pygame.draw.rect(self.screen , self.GREY,(self.x_init + 1250 ,self.y_init - 120, self.Length + 80, self.width + 70))


class Name_font(Init):
	def __init__(self,screen,color,x_init,y_init,list_font):
		super().__init__(screen,color,x_init,y_init)
		self.list_font = list_font

	def show_name_button(self):
		fonts = self.list_font
 		#                           1                                      2                                        3                                         4                                     5                                6                                       7                                        8                                 9                                 10                                            11                               12                                                
		list_value = [[self.x_init - 5, self.y_init - 668], [self.x_init + 1450, self.y_init - 11], [self.x_init + 130, self.y_init + 50], [self.x_init - 10, self.y_init - 5], [self.x_init + 1450, self.y_init], [self.x_init - 15, self.y_init - 660], [self.x_init + 720 ,self.y_init + 50], [self.x_init + 1255 ,self.y_init - 120],[self.x_init + 15, self.y_init + 50],[self.x_init + 450 ,self.y_init + 50],[self.x_init + 1255,self.y_init - 95],[self.x_init + 575 ,self.y_init + 50]]
		value = [i for i in range(12)]
		for i in range(len(fonts)):
			for index in range(len(value)):
				self.screen.blit(fonts[i][index],(list_value[index][0], list_value[index][1]))

class Draw_point:
	#Khởi tạo các thuộc tính của mỗi điểm data
	def __init__(self,screen,RED,points):
		self.screen = screen
		self.RED = RED
		self.points = points

	#Vẽ các điểm data lên giao diện
	def draw_points(self):
		point = self.points
		for i in range(len(point)):
			pygame.draw.circle(self.screen,self.RED,(point[i][0] + 50 ,700 - point[i][1]),7)

#Tính đường thẳng hồi quy bằng công thức
def calc_linear_ressgrion(x,y):
	if len(x) >= 3:
		A = np.array([x]).T
		b = np.array([y]).T
		x0 = [min(x),max(x)]
		ones = np.ones((A.shape[0],1), dtype=np.int8)
		A = np.concatenate((A, ones), axis =1)
		x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
		y01 = x[1][0] + x[0][0]*x0[0]
		y02 = x[1][0] + x[0][0]*x0[1]
		return (x0[0],y01,x0[1],y02,x[0][0],x[1][0])

#Tính đường thẳng hồi quy bằng thư viện có sẵn
def lr(x,y):
	if len(x) >= 3:
		A = np.array([x]).T
		b = np.array([y]).T
		lr = linear_model.LinearRegression()
		lr.fit(A,b)
		x0  = min(x)
		y0 = x0*lr.coef_[0][0] + lr.intercept_[0]
		x = max(x)
		y = x*lr.coef_[0][0] + lr.intercept_[0]
		return (x0,y0,x,y,lr.coef_[0][0],lr.intercept_[0])

#Tính tổng lỗi sinh ra
def calc_error(points,a,b):
	init = 0
	for i in range(len(points)):
		if len(points) >= 3:
			y = points[i][0]*a + b
			init += abs(points[i][1] - y)
	return init

class Lr_recipe:
	def __init__(self,screen,BLUE,const):
		self.screen = screen
		self.BLUE = BLUE
		self.const = const
	#Vẽ đường thẳng tính bằng công thức lên giao diện
	def draw_lr_recipe(self):
		list_value_result = self.const
		for i in range(len(list_value_result)):
			pygame.draw.line(self.screen, self.BLUE, (list_value_result[i][0]*10 + 50 , 700 - list_value_result[i][1]*10),(list_value_result[i][2]*10 + 50 , 700 - list_value_result[i][3]*10),4)

class Lr_library:
	def __init__(self,screen,BLACK,const):
		self.screen = screen
		self.BLACK = BLACK
		self.const = const

	#Vẽ đường thẳng tính bằng công thức lên giao diện
	def draw_lr_library(self):
		Const = self.const
		for i in range(len(Const)):
			pygame.draw.line(self.screen, self.BLACK, (Const[i][0]*10 + 50 , 700 - Const[i][1]*10),(Const[i][2]*10 + 50 , 700 - Const[i][3]*10),4)

def Draw_interface(screen,running,clock,COLORS,x_init,y_init,x_max,length,width):
	error_lr = "Error: No data for linear regression"
	font = pygame.font.SysFont('sans',20)
	font_new = pygame.font.SysFont('san',40)
	ox = font.render("▲",True,COLORS.BLACK)
	oy = font.render("►",True,COLORS.BLACK)
	CLEAR_BUTTON_1 = font.render("Delete the line 1",True,COLORS.BLUE)
	init_value = font.render("0",True,COLORS.BLACK)
	name_ox = font.render("x",True,COLORS.BLACK)
	name_oy = font.render("y",True,COLORS.BLACK)
	reset_button = font.render("RESET",True,COLORS.GREEN)
	font_note = font.render("Note",True,COLORS.BLACK) 
	font_recipe = font.render("Predict recipe",True,COLORS.BLUE)
	font_library = font.render("Predict library",True,COLORS.BLACK)
	font_data_point = font.render("Data point",True,COLORS.BLACK)
	CLEAR_BUTTON_2 = font.render("Delete the line 2",True,COLORS.BLACK)
	error_note = "Error: Don't write in the comments"
	font_recipe_note = font.render("Predict recipe",True,COLORS.BLUE)
	font_library_note = font.render("Predict library",True,COLORS.BLACK)

	

	list_fonts = [[ox,oy,CLEAR_BUTTON_1,init_value,name_ox,name_oy,reset_button,font_note,font_recipe,font_library,font_data_point,CLEAR_BUTTON_2]]
	points = []
	value_X = []
	value_Y = []
	list_value = []
	list_distance = []
	list_error_lr = []
	list_value_result = []
	list_error_note = []
	list_error_data = []
	error_1 = []
	error_2 = []

	while running:
		clock.tick(60)
		screen.fill(COLORS.BACKGROUP)
		x_mouse,y_mouse = pygame.mouse.get_pos()

		#Hiển thị tọa độ của con chuột
		if 50 <= x_mouse <= 1500 and 50 <= y_mouse <= 700:
			text_mouse = font.render("(" + "x=" + str((x_mouse -50)) + "," + "y =" + str(abs(y_mouse-700)) + ")",True,COLORS.BLACK)
			screen.blit(text_mouse, (x_mouse + 10, y_mouse))

		#Vẽ 2 trục ox và oy
		draw_panel = Draw_panel(screen,COLORS.BLACK,x_init,y_init,x_max)
		draw_panel.draw_ox_oy()

		#Vẽ các nút bấm lên giao diện
		draw_button = Draw_button(screen,COLORS.BLACK,x_init,y_init,x_max,length,width,COLORS.GREY)
		draw_button.BACKGROUP_BUTTON()
		draw_button.button_result_1()
		draw_button.button_clearn_line_1()
		draw_button.button_error()
		draw_button.button_result_2()
		draw_button.button_clearn_line_2()
		draw_button.button_reset()
		draw_button.Show_when_error()
		draw_button.font_note()

		#1305,600
		#Note
		pygame.draw.circle(screen,COLORS.RED,(1440,620),7)
		screen.blit(font_recipe_note,(1305,630))
		pygame.draw.line(screen,COLORS.BLUE,(1410,643),(1475,643),4)
		screen.blit(font_library_note,(1305,655))
		pygame.draw.line(screen,COLORS.BLACK,(1410,666),(1475,666),4)



		#Tên các nút trong chương trình
		name_font = Name_font(screen,COLORS,x_init,y_init,list_fonts)
		name_font.show_name_button()

		#Các sự kiện trong chương trình
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			#Khi bấm chuột xuống
			if event.type == pygame.MOUSEBUTTONDOWN:

				#x_init = 50
				#y_init = 700
				#x_max = 1500
				#length = 100
				#width = 40
				
				#Khi bấm chuột vào panel
				if x_init <= x_mouse <= x_max and x_init <= y_mouse <= y_init:
					value_X.append((x_mouse-50)/10)
					value_Y.append(abs(700 - y_mouse)/10)
					point = [x_mouse - 50,(abs(y_mouse - 700))]
					points.append(point)

				#khi bấm chuột vào nút result_1
				if (x_init + 5) <= x_mouse <= (length + x_init + 25)  and (y_init + 45) <= y_mouse <= (y_init + 85):
					try:
						#Tính đường thẳng cần tìm bằng công thức
						(x1,y1,x2,y2,a,b)  = calc_linear_ressgrion(value_X,value_Y)
						save_value = [x1,y1,x2,y2]
						list_value_result.append(save_value)

						#Tính tổng số lỗi sinh ra
						calc_sum_error = calc_error(points,a,b)
						list_distance.append(calc_sum_error)
						
						#Hiển thị số lỗi khi không có data ra màn hình
						if points == []:
							list_value_result = []
							list_error_lr.append(error_lr)
						
					except:
						list_error_lr.append(error_lr)

				#Bấm vào nút Delete the line 1 để xóa đi đường thẳng màu xanh tính bằng công thức
				if (x_init + 130) <= x_mouse <= (x_init + length + 150) and (y_init + 45) <= y_mouse <= (y_init + width + 45):
					list_value_result = []
					list_distance = []

				#Tính đường thẳng bằng thư viện 
				if (x_init + 440) <= x_mouse <= (x_init + length + 485) and (y_init + 45) <= y_mouse <= (y_init + width + 45):
					try:
						a,b,c,d,e,f = lr(value_X,value_Y)
						consts = [a,b,c,d]
						list_value.append(consts)

						#Tính tổng lỗi sinh ra
						calc_sum_error = calc_error(points,e,f)
						list_distance.append(calc_sum_error)
						if points == []:
							list_value = []
							list_error_lr.append(error_lr)

					except:
						list_error_lr.append(error_lr)

				#Bấm vào nút Delete the line 2 để xóa đi đường thẳng màu đen tính bằng thư viện
				if (x_init + 575) <= x_mouse <= (x_init + length + 595) and (y_init + 45) <= y_mouse <= (y_init + width + 45):
					list_value = []
					list_distance = []

				#Nút RESET xóa đi tất
				if (x_init + 700) <= x_mouse <= (x_init + length + 700) and (y_init + 45) <= y_mouse <= (y_init + width + 45):
					points = []
					list_value_result = []
					list_distance = []
					list_value = []
					error_lr = []
					error_1.append(error_lr)
					error_2.append(error_note)

				#Lỗi khi bấm vào ghi chú
				if (x_init + 1250) <= x_mouse <= (x_init + length + 1250) and (y_init - 120) <= y_mouse <= (y_init + width - 50):
					list_error_note.append(error_note)
					points = []

		#Vẽ điểm dữ liệu lên màn hình
		draw_point = Draw_point(screen,COLORS.RED,points)
		draw_point.draw_points()

		#Hiển thị đường thẳng tính bằng công thức lên giao diện
		lr_recipe = Lr_recipe(screen,COLORS.BLUE,list_value_result)
		lr_recipe.draw_lr_recipe()

		#Hiển thị đường thẳng tính bằng thư viện lên giao diện
		lr_library = Lr_library(screen,COLORS.BLACK,list_value)
		lr_library.draw_lr_library()

		#Tính lỗi
		error = 0
		for i in range(len(list_distance)):
			error += list_distance[i]

		#Hiển thị lỗi lên giao diện
		error_button = font.render("Error = " + str(int(error)),True,COLORS.RED)
		screen.blit(error_button,(310,750))

		#Hiển thị lỗi khi không có data
		for i in range(len(list_error_lr)):
			error_new = font_new.render(str(list_error_lr[i]),True,COLORS.RED)
			screen.blit(error_new,(860,750))
		
		#Hiển thị lỗi khi bấm vào Note
		for i in range(len(list_error_note)):
			error_new = font_new.render(str(list_error_note[i]),True,COLORS.RED)
			screen.blit(error_new,(860,750))

		#Xóa đi lỗi Error: No data for linear regression 
		for i in range(len(error_1)):
			if error_1[i] == error_lr:
				pygame.draw.rect(screen,COLORS.GREY,(x_init + 805,y_init + 45,length + 395,width))

		#Xóa đi lỗi Error: Don't write in the comments  
		for i in range(len(error_2)):	
			if error_2[i] == error_note:
				pygame.draw.rect(screen,COLORS.GREY,(x_init + 805,y_init + 45,length + 395,width))


		pygame.display.flip()
	pygame.quit()

def main():
	#Khởi tạo lên tọa độ ban đầu
	x_init,y_init,x_max,length,width = 50,700,1500,100,40
	COLORS = color()
	pygame.init()
	screen = pygame.display.set_mode((1530,830))
	clock = pygame.time.Clock()
	running = True
	Draw_interface(screen,running,clock,COLORS,x_init,y_init,x_max,length,width)

main()
