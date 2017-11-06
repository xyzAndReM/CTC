import pygame

class start_button():
	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.color = (255,140,0)
		self.size = size
	def draw(self,screen):
		pygame.draw.rect(screen, self.color,(self.x,self.y,self.size,self.size),2)
		pygame.draw.polygon(screen, self.color,( (self.x + 0.1*self.size ,self.y + 0.1*self.size ),(self.x + 0.1*self.size ,self.y + 0.9*self.size ),(self.x + 0.9*self.size ,self.y + 0.5*self.size )   ), 0)

class control_panel():
	def __init__(self,x,y,size):
		self.x = x;
		self.y = y;
		self.buttons = []
		start = start_button(x,y,size)
		self.buttons.append(start)
	def draw(self,screen):
		for i in self.buttons:
			i.draw(screen)
