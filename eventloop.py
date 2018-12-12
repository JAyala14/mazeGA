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

    def movePLAYER(self, player, inputs):
        for x in inputs:
            if x == 0:
                player.moveUP()
                player.index = 6
            if x == 1:
                player.moveRIGHT()
                player.index = 4
            if x == 2:
                player.moveDOWN()
                player.index = 0
            if x == 3:
                player.moveLEFT()
                player.index = 2


    def check_keydown_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()
