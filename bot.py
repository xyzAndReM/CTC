import pygame
import drawings

MARGIN = 6
ARESTA = 30

class robot():
	def __init__(self,x,y):
		self.color = (0,191,255)
		self.xspeed = 0
		self.yspeed = 1
		self.xcoord = x
		self.ycoord = y
		self.counter = 18;
		self.sequence = [];
	def get_coords(self):
		return (self.xcoord,self.ycoord)
	def move(self):
		self.xcoord +=self.xspeed *2;
		self.ycoord +=self.yspeed *2;
		self.counter-=1;
	def change_speed(self,grid):
		print(self.counter)
		if(self.counter == 0):
			self.counter = 18;
			(self.xspeed,self.yspeed) = grid.get_speed(2);
	def get_speed(self,grid):
		(a,b) = grid.get_speed(sequence[0])
		self.xspeed = a;
		self.yspeed = b;
	def draw(self,screen):
		pygame.draw.circle(screen, self.color, (self.xcoord,self.ycoord ), 10, 0)

def is_on_center(x,y):
		if( ( (x - ARESTA/2 - MARGIN)%(ARESTA + 2*MARGIN) == 0) and ( (y - ARESTA/2 - MARGIN)%(ARESTA + 2*MARGIN) == 0) ):
			return True
		else:
		 return False;