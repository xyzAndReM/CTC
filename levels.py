import pygame
import bot
import os
import glob
MARGIN = 6
ARESTA = 30
BLACK = (0,0,0);
BLUE = (0,191,255);
PINK = (255,105,180);
RED = (204, 0, 0);
PURPLE = (148,0,211);


class level():
	def __init__(self,bots,text):
		self.bots = bots
		self.text = text
	def set_text(self,text):
		self.text = text;
	def set_bots(self,bots):
		self.bots = bots;
	def set_outputs(self,outputs):
		self.outputs = outputs;
class game_levels():
	def __init__(self):
		self.stages = [];
	'''STAGE NUMBER 1:'''
	def get_levels(self):
		files = os.listdir("stages/")
		sequences = [];
		print(files)
		for fle in files:
			fle = "stages/"+fle;
			with open(fle) as f:
				text = f.readlines()
				text = [x.strip() for x in text]
				missao = text[0];
				n_robots = int(text[1])
				for i in range(n_robots):
					sequences.append( list(map(int, text[2+i].split())) )
				outputs = list(map(int,text[2+n_robots].split()))

				bots = bots_creation(n_robots,sequences,outputs);
				fase = level(bots,missao);
				self.stages.append(fase);

def bots_creation(n_robots,sequences,outputs):
	robots = [];
	for i in range(n_robots):
		rob = bot.robot(sequences[i],outputs[i]);
		robots.append(rob)
	print(robots)
	return robots

a = game_levels();
a.get_levels()


