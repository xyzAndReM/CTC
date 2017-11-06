import pygame
import drawings
import operator


MARGIN = 6;
class grid_square:
	def __init__(self, aresta):
		self.color = (220,220,220)
		self.xspeed = 0
		self.yspeed = 0
		self.aresta = aresta
	def selected(self):
		if(self.color == (220,220,220)):
			self.color = (60,120,30);
		elif(self.color == (60,120,30)):
			self.color = (220,220,220);
	def draw(self,screen,column,row):
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
	def get_speed(self,dado):
		return (self.xspeed,self.yspeed);


class grid_arrow_right(grid_square):
	def __init__(self, aresta):
		self.color = (220,220,220)
		self.xspeed = 1
		self.yspeed = 0
		self.aresta = aresta
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = ( (0+x, 7+y), (0+x, 23+y), (15+x, 23+y), (15+x, 30+y), (30+x, 15+y), (15+x, 0+y), (15+x,7+y))
		pygame.draw.polygon(screen, (0, 0, 0), coordinates)

class grid_arrow_left(grid_square):
	def __init__(self, aresta):
		self.color = (220,220,220)
		self.xspeed = -1
		self.yspeed = 0
		self.aresta = aresta
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = ( (0+x, 15+y), (15+x, 30+y), (15+x, 23+y), (30+x, 23+y), (30+x, 7+y), (15+x, 7+y), (15+x,0+y))
		pygame.draw.polygon(screen, (0, 0, 0), coordinates)

class grid_arrow_up(grid_square):
	def __init__(self, aresta):
		self.color = (220,220,220)
		self.xspeed = 0
		self.yspeed = -1
		self.aresta = aresta
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = ( (15+x, 0+y), (30+x, 15+y), (23+x, 15+y), (23+x, 30+y), (7+x, 30+y), (7+x, 15+y), (0+x,15+y))
		pygame.draw.polygon(screen, (0, 0, 0), coordinates)

class grid_arrow_down(grid_square):
	def __init__(self, aresta):
		self.color = (220,220,220)
		self.xspeed = 0
		self.yspeed = 1
		self.aresta = aresta
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = ( (15+x, 30+y), (30+x, 15+y), (23+x, 15+y), (23+x, 0+y), (7+x, 0+y), (7+x,15+y), (0+x,15+y))
		pygame.draw.polygon(screen, (0, 0, 0), coordinates)



class grid_map:
	def __init__(self,aresta,n):
		self.grid = []
		self.n = n;
		for row in range(n):
			self.grid.append([])
			for column in range(n):
				x = grid_square(aresta)
				self.grid[row].append(x)
	def drawmap(self,screen):
		for row in range(self.n):
			for column in range(self.n):
				square = self.grid[row][column];
				square.draw(screen,row,column);




