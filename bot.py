import pygame
import drawings

MARGIN = 6
ARESTA = 30

class robot():
	def __init__(self,x,y,sequence):
		self.color = (0,191,255)
		self.xspeed = 0
		self.yspeed = 1
		self.xcoord = x
		self.ycoord = y
		self.counter = 18;
		self.sequence = sequence;
	def get_coords(self):
		return (self.xcoord,self.ycoord)
	def move(self):
		self.xcoord +=self.xspeed *2;
		self.ycoord +=self.yspeed *2;
		self.counter-=1;
	def change_speed(self,grid):
		if(self.counter == 0):
			self.counter = 18;
			(self.xspeed,self.yspeed) = grid.get_speed(self);
	def get_speed(self):
		spd = (self.xspeed,self.yspeed)
		return spd
	def draw(self,screen):
		spacing = 15;
		pygame.draw.circle(screen, self.color, (self.xcoord,self.ycoord ), 10, 0)
		for item in self.sequence:
			spacing+=30;
			if item == 0:
				print("oi")
				pygame.draw.circle(screen,(0,191,255),(spacing,570),12,0)
			elif item == 1:
				pygame.draw.circle(screen,(255,105,180),(spacing,570),12,0)
def is_on_center(x,y):
		if( ( (x - ARESTA/2 - MARGIN)%(ARESTA + 2*MARGIN) == 0) and ( (y - ARESTA/2 - MARGIN)%(ARESTA + 2*MARGIN) == 0) ):
			return True
		else:
		 return False;