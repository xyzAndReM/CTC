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
	def __init__(self,sequences,outputs,text,n_robots):
		self.sequences = sequences
		self.outputs = outputs
		self.text = text
		self.counter = -1;
		self.rob = None;
		self.n_robots = n_robots
	def set_text(self,text):
		self.text = text;
	def set_sequences(self,sequences):
		self.sequences = sequences;
	def set_outputs(self,outputs):
		self.outputs = outputs;
	def get_bot(self):
		return self.rob;
	def get_text(self):
		return text;
	def reset(self):
		self.counter = -1;
	def create_bot(self):
		print('qpressed')
		self.counter +=1;
		if(self.counter < self.n_robots):
			n = self.counter;
			sequence = list(self.sequences[n])
			output = self.outputs[n]
			self.rob = bot.robot(sequence,output);
			return self.rob
		else:
			return None;
	def update_bot(self,grid,screen):
		self.rob.draw(screen)
		self.rob.move()
		self.rob.change_speed(grid)

class game_levels():
	def __init__(self):
		self.stages = [];
		self.build_levels()
	'''STAGE NUMBER 1:'''
	def build_levels(self):
		files = os.listdir("stages/")
		print(files)
		for fle in files:
			sequences = [];
			outputs = [];
			fle = "stages/"+fle;
			with open(fle) as f:
				text = f.readlines()
				text = [x.strip() for x in text]
				missao = text[0];
				n_robots = int(text[1])
				for i in range(n_robots):
					sequences.append( list(map(int, text[2+i].split())) )
					outputs.append(  list(map(int,text[2+i+n_robots].split())) )
				print(outputs)
				fase = level(sequences,outputs,missao,n_robots);
				self.stages.append(fase);
	def get_levels(self):
		return self.stages;

def bots_creation(n_robots,sequences,outputs):
	robots = [];
	for i in range(n_robots):
		print(outputs[i])
		rob = bot.robot(sequences[i],outputs[i]);
		robots.append(rob)
	print(robots)
	return robots

a = game_levels();
a.get_levels()


