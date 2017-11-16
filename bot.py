import pygame


MARGIN = 6
ARESTA = 30
BLACK = (0,0,0);
BLUE = (0,191,255);
PINK = (255,105,180);
RED = (204, 0, 0);
PURPLE = (148,0,211);

ELIXIR = pygame.image.load('images/elixir.png')

class robot():
	def __init__(self,sequence,output):
		self.xspeed = 0
		self.yspeed = 1
		self.x = 273
		self.y = 21
		self.counter = 18;
		self.sequence = sequence;
		self.output = output;
	def get_coords(self):
		return (self.x,self.y)
	def move(self):
		self.x +=self.xspeed *2;
		self.y +=self.yspeed *2;
		self.counter-=1;
	def write(self,color):
		self.sequence.append(color);
	def change_speed(self,grid):
		if(self.counter == 0):
			self.counter = 18;
			(self.xspeed,self.yspeed) = grid.get_speed(self);
	def get_speed(self):
		spd = (self.xspeed,self.yspeed)
		return spd
	def draw(self,screen):
		spacing = 15;
		x = self.x - 15;
		y = self.y - 15;
		w = 1
		screen.blit(ELIXIR,(x,y))
		for item in self.sequence:
			spacing+=30;
			if item == 0:
				pygame.draw.circle(screen,BLUE,(spacing,570),12,0)
			elif item == 1:
				pygame.draw.circle(screen,PINK,(spacing,570),12,0)
			elif item == 2:
				pygame.draw.circle(screen,PURPLE,(spacing,570),12,0)
			elif item == 3:
				pygame.draw.circle(screen,RED,(spacing,570),12,0)
