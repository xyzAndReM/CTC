#!/usr/bin/python
#
# -------------------------------------------------------------
# template - a template to start pygame programs
# 2012-10-01 Javier Cantero <jcantero@escomposlinux.org>
#
# LICENSE:
# Public Domain - Use what/where/how you like and remove this
# -------------------------------------------------------------

import pygame
import gridmap
import bot
import levels
import os




# general constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NSQUARES = 15;
ARESTA = 30;
ARESTA_CONTROL = 40;
X_CONTROL = 600;
Y_CONTROL = 100;
MARGIN = 6;
D = ARESTA+MARGIN;
STOP_COUNTER = D/18;
FRAME_RATE = 30
START_X = 273;
START_Y = 21;
'''KEYS'''
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN
Q_KEY = pygame.K_q
KEY1 = pygame.K_1
KEY2 = pygame.K_2
KEY3 = pygame.K_3
KEY4 = pygame.K_4
KEY5 = pygame.K_5
KEY6 = pygame.K_6
A_KEY = pygame.K_a
S_KEY = pygame.K_s
W_KEY = pygame.K_w
D_KEY = pygame.K_d

DIRECTION_CONTROLLER = [LEFT_KEY,RIGHT_KEY,UP_KEY,DOWN_KEY]
MOVEMENT_CONTROLLER = {A_KEY:(-1,0),W_KEY:(0,-1),S_KEY:(0,1),D_KEY:(1,0)}
BUILDER_CONTROLLER = [KEY1,KEY2,KEY3,KEY4,KEY5,KEY6]
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.music.load('sound/main1.ogg')

CHANGE = 'sound/change.wav'
EQUIP = 'sound/equip.wav'
SUCCESS = 'sound/success.wav'
START = 'sound/start.wav'
END = 'sound/end.wav'
ERROR = 'sound/error.wav'
_sound_library = {}
def play_sound(path):   
  global _sound_library
  if(path != None):
      sound = _sound_library.get(path)
      if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(path)
        _sound_library[path] = sound
      sound.play()

def delay(delta,t):
    k = 0
    print(delta)
    while k< t:
        k += delta;



 
class Game():
    def __init__(self):
        self.current_level = 0;
        self.builder = "arrow"
        self.builderSelector = {KEY1:"simple",KEY2:"arrow",KEY3:"selector",KEY4:"writer",KEY5:'selector2',KEY6:'special'}
        self.builderTable = {"simple":gridmap.simple_builder(), "arrow":gridmap.arrow_builder(),"selector":gridmap.selector_builder(),"selector2":gridmap.selector2_builder(),"writer":gridmap.writer_builder(),"special":gridmap.special_builder()};
        self.stages = levels.game_levels().get_levels()
    def start_robot(self,sequence,output):
        self.rob = bot.robot(sequence,output);
        self.robot_is_on = True;
    def loop(self, screen):
        for i in range(len(self.stages)):
            print('lvlstart')
            self.GRID_MAP = gridmap.grid_map(ARESTA,NSQUARES)
            clock = pygame.time.Clock()
            last_clicked_grid_X = 7;
            last_clicked_grid_Y = 1;
            LEVEL = self.stages[i];
            missao = pygame.image.load(LEVEL.text);
            rob = None;
            pygame.mixer.music.play(-1,0.0)
            while True:
                delta_t = clock.tick( FRAME_RATE )

                # handle input events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return # closing the window, end of the game loop
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        column = pos[1] // (ARESTA + MARGIN)
                        row = pos[0] // (ARESTA + MARGIN)
                        if( column < 15 and row < 15):
                            last_clicked_grid_X = row;
                            last_clicked_grid_Y = column;
                            self.GRID_MAP.change_selection(column,row);
                    elif event.type == pygame.KEYDOWN:
                        if (event.key in DIRECTION_CONTROLLER):
                            play_sound(EQUIP)
                            grid_maker = self.builderTable[self.builder];
                            self.GRID_MAP.grid[last_clicked_grid_X][last_clicked_grid_Y] = grid_maker.makegrid(event.key)
                        elif event.key == Q_KEY:
                            T = 0;

                            play_sound(START)
                            rob = LEVEL.create_bot()
                        elif (event.key in BUILDER_CONTROLLER):
                            play_sound(CHANGE);
                            self.builder = self.builderSelector[event.key]
                        elif (event.key in MOVEMENT_CONTROLLER):
                            movement = MOVEMENT_CONTROLLER[event.key];
                            last_clicked_grid_X += movement[0];
                            last_clicked_grid_Y += movement[1];
                            self.GRID_MAP.change_selection(last_clicked_grid_Y,last_clicked_grid_X);


                # render game screen
                screen.fill( (255, 255, 255) ) # black background
                self.GRID_MAP.drawmap(screen);

                if(rob != None):
                    rob.draw(screen)
                    (X,Y) = rob.get_coords()
                    x = X// (ARESTA + MARGIN)
                    y = Y// (ARESTA + MARGIN)
                    actual_grid = self.GRID_MAP.grid[x][y];
                    rob.move()
                    rob.change_speed(actual_grid)
                if(rob != None and rob.get_speed() == (0,0) ):
                        if(rob.validate()):
                            print('SUCCESS')
                            play_sound(SUCCESS)
                            rob = LEVEL.create_bot()
                            if(rob == None):
                                play_sound(END);
                                pygame.time.delay(4000)
                                break
                        else:
                            print('FAILURE')
                            play_sound(ERROR)
                            rob = None;
                            LEVEL.reset();

                screen.blit(missao,(600,0))
                pygame.display.update()
            # or pygame.display.flip()

    def quit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption( 'CTC projetinho' )
    #pygame.mouse.set_visible( False )
    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()

