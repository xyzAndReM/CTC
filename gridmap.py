import pygame
import drawings
import operator

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN
Q_KEY = pygame.K_q

MARGIN = 6;
ARESTA = 30;
blue = 0;
pink = 1;


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
#-----------------------------------------------------------------
class selector_up(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence.pop(0)
			if(dado == blue):
				return (-1,0);
			elif(dado == pink):
				return (1,0)
		else:
			return bot.get_speed();

	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = (  (0+x, 15+y), (10+x, 7.5+y), (10+x, 22.5+y))
		pygame.draw.polygon(screen, (0,191,255), coordinates)
		coordinates = (  (30+x, 15+y), (20+x, 7.5+y), (20+x, 22.5+y))
		pygame.draw.polygon(screen, (255,105,180), coordinates)
		coordinates = (  (12.5+x, 5+y), (17.5+x, 5+y), (15+x, 0+y))
		#pygame.draw.polygon(screen, (0,0,0), coordinates)
class selector_down(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence.pop(0)
			if(dado == blue):
				return (+1,0);
			elif(dado == pink):
				return (-1,0)
		else:
			return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = (  (0+x, 15+y), (10+x, 7.5+y), (10+x, 22.5+y))
		pygame.draw.polygon(screen, (255,105,180), coordinates)
		coordinates = (  (30+x, 15+y), (20+x, 7.5+y), (20+x, 22.5+y))
		pygame.draw.polygon(screen, (0,191,255), coordinates)
		coordinates = (  (12.5+x, 15+y), (17.5+x, 15+y), (15+x, 0+y))
		#pygame.draw.polygon(screen, (0,0,0), coordinates)
class selector_right(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence.pop(0)
			if(dado == blue):
				return (0,+1);
			elif(dado == pink):
				return (0,-1)
		else:
			return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = (  (15+x, 0+y), (7.5+x, 10+y), (22.5+x, 10+y))
		pygame.draw.polygon(screen, (255,105,180), coordinates)
		coordinates = (  (15+x, 30+y), (7.5+x, 20+y), (22.5+x, 20+y))
		pygame.draw.polygon(screen, (0,191,255), coordinates)
		#coordinates = (  (12.5+x, 15+y), (17.5+x, 15+y), (15+x, 0+y))
class selector_left(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence.pop(0)
			if(dado == blue):
				return (0,-1);
			elif(dado == pink):
				return (0,+1)
		else:
			return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		pygame.draw.rect(screen, self.color, ( (MARGIN + self.aresta) * column + MARGIN, (MARGIN +  self.aresta) * row + MARGIN, self.aresta, self.aresta))
		coordinates = (  (15+x, 0+y), (7.5+x, 10+y), (22.5+x, 10+y))
		pygame.draw.polygon(screen, (0,191,255), coordinates)
		coordinates = (  (15+x, 30+y), (7.5+x, 20+y), (22.5+x, 20+y))
		pygame.draw.polygon(screen, (255,105,180), coordinates)




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

class simple_builder():
	def __init__(self):
		pass;
	def makegrid(self,dir):
		return grid_square(ARESTA);

class arrow_builder(simple_builder):
	def makegrid(self,dir):
		if   dir == RIGHT_KEY:
			return grid_arrow_right(ARESTA);
		elif dir == LEFT_KEY:
			return grid_arrow_left(ARESTA);
		elif dir == UP_KEY:
			return grid_arrow_up(ARESTA);
		elif dir == DOWN_KEY:
			return grid_arrow_down(ARESTA);
		else:
			return grid_square(ARESTA);
class selector_builder(simple_builder):
	def makegrid(self,dir):
		if   dir == RIGHT_KEY:
			return selector_right(ARESTA);
		elif dir == LEFT_KEY:
			return selector_left(ARESTA);
		elif dir == UP_KEY:
			return selector_up(ARESTA);
		elif dir == DOWN_KEY:
			return selector_down(ARESTA);
		else:
			return grid_square(ARESTA);






