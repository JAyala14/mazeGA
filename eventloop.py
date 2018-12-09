import sys

import pygame


class EventLoop:

    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'

    def check_events(self, settings, player, maze, inputs):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, player)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, player)

        for i in inputs:
            if i == 0:
                player.moving_up = True
                player.index = 6
                inputs.remove(0)
            if i == 1:
                player.moving_right = True
                player.index = 4
                inputs.remove(1)
            if i == 2:
                player.moving_down = True
                player.index = 0
                inputs.remove(2)
            if i == 3:
                player.moving_left = True
                player.index = 2
                inputs.remove(3)


    def check_keydown_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            player.moving_up = True
            player.index = 6
        elif event.key == pygame.K_DOWN:
            player.moving_down = True
            player.index = 0
        elif event.key == pygame.K_LEFT:
            player.moving_left = True
            player.index = 2
        elif event.key == pygame.K_RIGHT:
            player.moving_right = True
            player.index = 4

    def check_keyup_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            player.moving_up = False
        elif event.key == pygame.K_DOWN:
            player.moving_down = False
        elif event.key == pygame.K_LEFT:
            player.moving_left = False
        elif event.key == pygame.K_RIGHT:
            player.moving_right = False
