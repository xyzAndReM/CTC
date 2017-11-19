import pygame


LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN
Q_KEY = pygame.K_q

MARGIN = 6;
ARESTA = 30;
blue = 0;
pink = 1;
purple = 2;
red = 3;

GRID = pygame.image.load('images/grid.png')
SUCCESS = pygame.image.load('images/success.png');
TELEPORTER = pygame.image.load('images/teleporter.png');

ARROW_RIGHT =  pygame.image.load('images/arrow_right.png');
ARROW_LEFT  =  pygame.image.load('images/arrow_left.png');
ARROW_UP    =  pygame.image.load('images/arrow_up.png');
ARROW_DOWN  =  pygame.image.load('images/arrow_down.png');

BLUE_STAFF = pygame.image.load('images/bluestaff2.png')
PINK_STAFF = pygame.image.load('images/pinkstaff2.png')
PURPLE_STAFF = pygame.image.load('images/purplestaff2.png')
RED_STAFF = pygame.image.load('images/redstaff2.png')

SELECTOR_UP = pygame.image.load('images/selector.png');
SELECTOR_DOWN = pygame.image.load('images/selector_down.png');
SELECTOR_LEFT = pygame.image.load('images/selector_left.png');
SELECTOR_RIGHT = pygame.image.load('images/selector_right.png');

SELECTOR2_UP = pygame.image.load('images/selector2_up.png');
SELECTOR2_DOWN = pygame.image.load('images/selector2_down.png');
SELECTOR2_LEFT = pygame.image.load('images/selector2_left.png');
SELECTOR2_RIGHT = pygame.image.load('images/selector2_right.png');


class grid_square:
	def __init__(self, aresta):
		self.image = GRID;
		self.xspeed = 0
		self.yspeed = 0
		self.aresta = aresta
		self.output = -1;
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(self.image,(x,y))
	def get_speed(self,bot):
		return (self.xspeed,self.yspeed);
class grid_fail(grid_square):
	def get_speed(self,bot):
		bot.sequence = [-1];
		return (self.xspeed,self.yspeed);
class grid_success(grid_square):
	def __init__(self, aresta):
		self.image = SUCCESS
		self.xspeed = 0
		self.yspeed = 0
		self.aresta = aresta
		self.output = 1;
	def get_speed(self,bot):
		bot.current_output = 1;
		return (self.xspeed,self.yspeed);
class teleporter(grid_square):
	def __init__(self,aresta):
		self.image = TELEPORTER
		self.xspeed = 0
		self.yspeed = 0
		self.aresta = aresta
		self.output = 0;
	def get_speed(self,bot):
		bot.x +=bot.xspeed*72;
		bot.y +=bot.yspeed*72;
		return (bot.xspeed,bot.yspeed);
class grid_arrow_right(grid_square):
	def __init__(self, aresta):
		self.image = ARROW_RIGHT
		self.xspeed = 1
		self.yspeed = 0
		self.aresta = aresta
class grid_arrow_left(grid_square):
	def __init__(self, aresta):
		self.image = ARROW_LEFT
		self.xspeed = -1
		self.yspeed = 0
		self.aresta = aresta
class grid_arrow_up(grid_square):
	def __init__(self, aresta):
		self.image = ARROW_UP
		self.xspeed = 0
		self.yspeed = -1
		self.aresta = aresta
class grid_arrow_down(grid_square):
	def __init__(self, aresta):
		self.image = ARROW_DOWN;
		self.xspeed = 0
		self.yspeed = 1
		self.aresta = aresta
#-----------------------------------------------------------------


class selector_up(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == blue):
				sequence.pop(0)
				return (+1,0);
			elif(dado == pink):
				sequence.pop(0)
				return (-1,0)
			else:
				return(0,-1);
		else:
			return (0,-1);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR_UP,(x,y))
class selector_down(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == blue):
				sequence.pop(0)
				return (-1,0);
			elif(dado == pink):
				sequence.pop(0)
				return (+1,0)
			else:
				return (0,1)
		else:
			return (0,1);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR_DOWN,(x,y))
class selector_right(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == blue):
				sequence.pop(0)
				return (0,+1);
			elif(dado == pink):
				sequence.pop(0)
				return (0,-1)
			else:
				return (1,0)
		else:
			return (1,0);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR_RIGHT,(x,y))
class selector_left(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == blue):
				sequence.pop(0)
				return (0,-1);
			elif(dado == pink):
				sequence.pop(0)
				return (0,+1)
			else:
				return (-1,0)
		else:
			return (-1,0);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR_LEFT,(x,y))
#----------------------------------------------
class selector2_up(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == purple):
				sequence.pop(0)
				return (+1,0);
			elif(dado == red):
				sequence.pop(0)
				return (-1,0)
			else:
				return(0,-1);
		else:
			return (0,-1);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR2_UP,(x,y))
class selector2_down(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == purple):
				sequence.pop(0)
				return (-1,0);
			elif(dado == red):
				sequence.pop(0)
				return (+1,0)
			else:
				return (0,1)
		else:
			return (0,1);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR2_DOWN,(x,y))
class selector2_right(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == purple):
				sequence.pop(0)
				return (0,+1);
			elif(dado == red):
				sequence.pop(0)
				return (0,-1)
			else:
				return (1,0)
		else:
			return (1,0);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR2_RIGHT,(x,y))
class selector2_left(grid_square):
	def  get_speed(self,bot):
		sequence = bot.sequence
		if(sequence):
			dado = sequence[0]
			if(dado == purple):
				sequence.pop(0)
				return (0,-1);
			elif(dado == red):
				sequence.pop(0)
				return (0,+1)
			else:
				return (-1,0)
		else:
			return (-1,0);
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(SELECTOR2_LEFT,(x,y))



class writer_blue(grid_square):
	def get_speed(self,bot):
		bot.write(0);
		return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(BLUE_STAFF,(x,y))
class writer_pink(grid_square):
	def get_speed(self,bot):
		bot.write(1);
		return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(PINK_STAFF,(x,y))
class writer_purple(grid_square):
	def get_speed(self,bot):
		bot.write(2);
		return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(PURPLE_STAFF,(x,y))
class writer_red(grid_square):
	def get_speed(self,bot):
		bot.write(3);
		return bot.get_speed();
	def draw(self,screen,column,row):
		x = column*(MARGIN+self.aresta) + MARGIN;
		y = row*(MARGIN+self.aresta) + MARGIN;
		screen.blit(RED_STAFF,(x,y))







class grid_map:
	def __init__(self,aresta,n):
		self.grid = []
		self.n = n;
		self.x = 1;
		self.y = 7;
		for row in range(n):
			self.grid.append([])
			for column in range(n):
				x = grid_fail(aresta)
				self.grid[row].append(x)
		self.grid[7][14] = grid_success(aresta)
	def change_selection(self,x,y):
		self.x = x;
		self.y = y;
	def drawmap(self,screen):
		for row in range(self.n):
			for column in range(self.n):
				square = self.grid[row][column];
				square.draw(screen,row,column);
		column = self.y;
		row = self.x;
		pygame.draw.rect(screen, (100,32,200), ( (ARESTA+MARGIN) * column + MARGIN , (ARESTA+MARGIN) * row + MARGIN  , ARESTA, ARESTA),1)
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
class selector2_builder(simple_builder):
	def makegrid(self,dir):
		if   dir == RIGHT_KEY:
			return selector2_right(ARESTA);
		elif dir == LEFT_KEY:
			return selector2_left(ARESTA);
		elif dir == UP_KEY:
			return selector2_up(ARESTA);
		elif dir == DOWN_KEY:
			return selector2_down(ARESTA);
		else:
			return grid_square(ARESTA);
class writer_builder(simple_builder):
	def makegrid(self,dir):
		if   dir == RIGHT_KEY:
			return writer_pink(ARESTA);
		elif dir == LEFT_KEY:
			return writer_blue(ARESTA);
		elif dir == UP_KEY:
			return writer_red(ARESTA);
		elif dir == DOWN_KEY:
			return writer_purple(ARESTA);
class special_builder(simple_builder):
	def makegrid(self,dir):
		if dir == UP_KEY:
			return teleporter(ARESTA);
		elif dir == DOWN_KEY:
			return grid_success(ARESTA);
		else:
			return grid_square(ARESTA);






