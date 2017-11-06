import pygame
import operator


def draw_arrow(screen,x,y):
	coordinates = ((0, 7), (0, 23), (15, 23), (15, 30), (30, 15), (15, 0), (15,7));
	for coord in coordinates:
		tuple(map(operator.add, coord, (x,y)))
	pygame.draw.polygon(screen, (0, 0, 0), coordinates)

def draw_grid(screen):
	for i in range(21):
		k = i*30;
		pygame.draw.line(screen, (123,123,111), (200+k,0), (200+k,600), 2)
		pygame.draw.line(screen, (123,123,111), (200,k), (800,k), 2)
def draw_squaregrid(screen,grid,column,row):
	MARGIN = 5;
	pygame.draw.rect(screen, grid.color, ( (MARGIN + grid.aresta) * column + MARGIN, (MARGIN +  grid.aresta) * row + MARGIN, grid.aresta, grid.aresta))