#!/usr/bin/python
#
# -------------------------------------------------------------
# pointer - using a pointer with cursor keys
# 2013-01-05 Javier Cantero <jcantero@escomposlinux.org>
#
# LICENSE:
# Public Domain - Use what/where/how you like and remove this
# -------------------------------------------------------------

import pygame
#from pygame.locals import *

# general constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30

# keyboard
# use the arrow keys by default
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN
# but you can use another configuration, for example WASD:
#LEFT_KEY = pygame.K_a
#RIGHT_KEY = pygame.K_d
#UP_KEY = pygame.K_w
#DOWN_KEY = pygame.K_s

# game constants
HORIZONTAL_LEFT, HORIZONTAL_NOT, HORIZONTAL_RIGHT = ( -1, 0, 1 )
VERTICAL_UP, VERTICAL_NOT, VERTICAL_DOWN = ( -1, 0, 1 )

POINTER_SPEED = 5


class Game():
    def __init__(self):
        pass

    def loop(self, screen):
        # main loop variables
        clock = pygame.time.Clock()
        left_key_pressed = right_key_pressed = up_key_pressed = down_key_pressed = False
        horizontal_dir = HORIZONTAL_NOT
        vertical_dir = VERTICAL_NOT
        pointer = pygame.image.load( "pointer.png" )
        pointer_x = SCREEN_WIDTH / 2
        pointer_y = SCREEN_HEIGHT / 2

        while True:
            delta_t = clock.tick( FRAME_RATE )

            #
            #   I N P U T
            # --------------------------------------------------------------
    
            for event in pygame.event.get(): # event handling loop
    
                # handle quitting from the program
                if event.type == pygame.QUIT:
                    return # closing the window, end of the game loop
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return # closing the window, end of the game loop

                # movement keys
                elif event.type == pygame.KEYDOWN:
                    if event.key == UP_KEY:
                        up_key_pressed = True
                        vertical_dir = VERTICAL_UP
                    elif event.key == DOWN_KEY:
                        down_key_pressed = True
                        vertical_dir = VERTICAL_DOWN
                    elif event.key == LEFT_KEY:
                        left_key_pressed = True
                        horizontal_dir = HORIZONTAL_LEFT
                    elif event.key == RIGHT_KEY:
                        right_key_pressed = True
                        horizontal_dir = HORIZONTAL_RIGHT
                elif event.type == pygame.KEYUP:
                    if event.key == UP_KEY:
                        up_key_pressed = False
                        if down_key_pressed:
                            vertical_dir = VERTICAL_DOWN
                        else:
                            vertical_dir = VERTICAL_NOT
                    elif event.key == DOWN_KEY:
                        down_key_pressed = False
                        if up_key_pressed:
                            vertical_dir = VERTICAL_UP
                        else:
                            vertical_dir = VERTICAL_NOT
                    elif event.key == LEFT_KEY:
                        left_key_pressed = False
                        if right_key_pressed:
                            horizontal_dir = HORIZONTAL_RIGHT
                        else:
                            horizontal_dir = HORIZONTAL_NOT
                    elif event.key == RIGHT_KEY:
                        right_key_pressed = False
                        if left_key_pressed:
                            horizontal_dir = HORIZONTAL_LEFT
                        else:
                            horizontal_dir = HORIZONTAL_NOT

            #
            #   U P D A T E
            # --------------------------------------------------------------

            if vertical_dir == VERTICAL_UP:
                pointer_y -= POINTER_SPEED
                if pointer_y < 0:
                    pointer_y = 0
            elif vertical_dir == VERTICAL_DOWN:
                pointer_y += POINTER_SPEED
                if pointer_y > SCREEN_HEIGHT:
                    pointer_y = SCREEN_HEIGHT
            # change if for elif for 4-coordinates only movement
            if horizontal_dir == HORIZONTAL_LEFT:
                pointer_x -= POINTER_SPEED
                if pointer_x < 0:
                    pointer_x = 0
            elif horizontal_dir == HORIZONTAL_RIGHT:
                pointer_x += POINTER_SPEED
                if pointer_x > SCREEN_WIDTH:
                    pointer_x = SCREEN_WIDTH

            #
            #   R E N D E R
            # --------------------------------------------------------------
    
            # render game screen
            screen.fill( (0, 0, 0) ) # black background

            # blit the graphic elements to the screen surface
            screen.blit( pointer, (pointer_x, pointer_y) )

            # update display
            pygame.display.update()

    def quit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption( 'Pointer' )
    #pygame.mouse.set_visible( False )

    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()

