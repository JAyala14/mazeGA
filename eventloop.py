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

        for x in inputs:
            if x == 0:
                player.moving_up = True
                player.index = 6
            if x == 1:
                player.moving_right = True
                player.index = 4
            if x == 2:
                player.moving_down = True
                player.index = 0
            if x == 3:
                player.moving_left = True
                player.index = 2


    def check_keydown_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()
