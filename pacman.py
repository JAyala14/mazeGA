import pygame

import pygame.gfxdraw
import random

from maze import Maze
from eventloop import EventLoop
from player import Player
from settings import Settings


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((735, 400))
        pygame.display.set_caption("Pac-man")
        self.settings = Settings()

        self.maze = Maze(self.screen, 'images/maze.txt', 'images/cube0.png', 'images/gate0.png', 'images/dot0.png')

        self.player = Player(self.settings, self.screen, self.maze)

        self.inputs = []

        for i in range(41):
            randomNUMBER = random.randint(0,3)
            self.inputs.append(randomNUMBER)


    def play(self):
        clock = pygame.time.Clock()
        eloop = EventLoop(finished=False)

        eloop.movePLAYER(self.player, self.inputs)
        self.player.setFITNESS()
        self.player.displayEND()

        while not eloop.finished:
            eloop.check_events(self.settings, self.player, self.maze, self.inputs)

            self.player.update(self.maze)

            self.display_game()
            clock.tick(500)

    def display_game(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.player.blitme()

        pygame.display.flip()


game = Game()
game.play()
