import pygame
from pygame.sprite import Sprite
import positionNodes as PN


def load_image(self):
    image = pygame.image.load(self)
    return image


class Player(Sprite):
    BRICK_SIZE = 15

    def __init__(self, settings, screen, maze):
        super(Player, self).__init__()
        self.screen = screen
        self.settings = settings
        self.maze = maze
        with open('images/maze.txt', 'r') as f:
            self.rows = f.readlines()

        self.deltax = self.deltay = Player.BRICK_SIZE

        self.centerx = 0
        self.centery = 0

        self.startx = 0
        self.starty = 0

        self.build()

        self.images = []
        self.images.append(load_image('images/pacman/pacmanD1.png'))
        self.images.append(load_image('images/pacman/pacmanD2.png'))
        self.images.append(load_image('images/pacman/pacmanL1.png'))
        self.images.append(load_image('images/pacman/pacmanL2.png'))
        self.images.append(load_image('images/pacman/pacmanR1.png'))
        self.images.append(load_image('images/pacman/pacmanR2.png'))
        self.images.append(load_image('images/pacman/pacmanU1.png'))
        self.images.append(load_image('images/pacman/pacmanU2.png'))
        self.index = self.settings.pac_man_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.fitness = 0

        self.setFITNESS()

    def build(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'P':
                    self.centerx += (ncol + .25) * dx
                    self.centery += (nrow + .75) * dy

                    self.startx = self.centerx
                    self.starty = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.centery = self.starty
        self.centerx = self.startx

    def update(self, maze):
        self.animate()

    def moveUP(self):
        r = int((self.rect.centerx + 10) / 15)
        d = int((self.rect.centery + 10) / 15)
        l = int((self.rect.centerx - 10) / 15)
        u = int((self.rect.centery - 10) / 15)

        if (self.rows[u-1][r] != 'X') and (self.rows[u-1][l] != 'X'):
            self.centery -= self.settings.pac_man_speedfactor

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def moveRIGHT(self):
        r = int((self.rect.centerx + 10) / 15)
        d = int((self.rect.centery + 10) / 15)
        l = int((self.rect.centerx - 10) / 15)
        u = int((self.rect.centery - 10) / 15)

        if (self.rows[u][r+1] != 'X') and (self.rows[d][r+1] != 'X'):
            self.centerx += self.settings.pac_man_speedfactor

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def moveDOWN(self):
        r = int((self.rect.centerx + 10) / 15)
        d = int((self.rect.centery + 10) / 15)
        l = int((self.rect.centerx - 10) / 15)
        u = int((self.rect.centery - 10) / 15)

        if (self.rows[d+1][r] != 'X') and (self.rows[d+1][l] != 'X'):
            self.centery += self.settings.pac_man_speedfactor

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def moveLEFT(self):
        r = int((self.rect.centerx + 10) / 15)
        d = int((self.rect.centery + 10) / 15)
        l = int((self.rect.centerx - 10) / 15)
        u = int((self.rect.centery - 10) / 15)

        if (self.rows[u][l-1] != 'X') and (self.rows[d][l-1] != 'X'):
            self.centerx -= self.settings.pac_man_speedfactor

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def animate(self):
        self.index += 1
        if self.index == 2:
            self.index = 0
        if self.index == 4:
            self.index = 2
        if self.index == 6:
            self.index = 4
        if self.index >= 8:
            self.index = 6
        self.image = self.images[self.index]

    def displayEND(self):
        print(self.centery)
        print(self.centerx)
        print(self.fitness)

    def setFITNESS(self):
        if self.centery == 101.25:
            if self.centerx == 33.75:
                self.fitness = PN.a1

            if self.centerx == 78.75:
                self.fitness = PN.a2

            if self.centerx == 123.75:
                self.fitness = PN.a3

            if self.centerx == 168.75:
                self.fitness = PN.a4

            if self.centerx == 213.75:
                self.fitness = PN.a5

            if self.centerx == 258.75:
                self.fitness = PN.a6

            if self.centerx == 303.75:
                self.fitness = PN.a7

            if self.centerx == 348.75:
                self.fitness = PN.a8

            if self.centerx == 393.75:
                self.fitness = PN.a9

            if self.centerx == 438.75:
                self.fitness = PN.a10

            if self.centerx == 483.75:
                self.fitness = PN.a11

            if self.centerx == 528.75:
                self.fitness = PN.a12

            if self.centerx == 573.75:
                self.fitness = PN.a13

            if self.centerx == 618.75:
                self.fitness = PN.a14

            if self.centerx == 663.75:
                self.fitness = PN.a15

            if self.centerx == 708.75:
                self.fitness = PN.a16

        if self.centery == 146.25:
            if self.centerx == 33.75:
                self.fitness = PN.b1

            if self.centerx == 78.75:
                self.fitness = PN.b2

            if self.centerx == 123.75:
                self.fitness = PN.b3

            if self.centerx == 168.75:
                self.fitness = PN.b4

            if self.centerx == 213.75:
                self.fitness = PN.b5

            if self.centerx == 258.75:
                self.fitness = PN.b6

            if self.centerx == 303.75:
                self.fitness = PN.b7

            if self.centerx == 348.75:
                self.fitness = PN.b8

            if self.centerx == 393.75:
                self.fitness = PN.b9

            if self.centerx == 438.75:
                self.fitness = PN.b10

            if self.centerx == 483.75:
                self.fitness = PN.b11

            if self.centerx == 528.75:
                self.fitness = PN.b12

            if self.centerx == 573.75:
                self.fitness = PN.b13

            if self.centerx == 618.75:
                self.fitness = PN.b14

            if self.centerx == 663.75:
                self.fitness = PN.b15

            if self.centerx == 708.75:
                self.fitness = PN.b16

        if self.centery == 191.25:
            if self.centerx == 33.75:
                self.fitness = PN.c1

            if self.centerx == 78.75:
                self.fitness = PN.c2

            if self.centerx == 123.75:
                self.fitness = PN.c3

            if self.centerx == 168.75:
                self.fitness = PN.c4

            if self.centerx == 213.75:
                self.fitness = PN.c5

            if self.centerx == 258.75:
                self.fitness = PN.c6

            if self.centerx == 303.75:
                self.fitness = PN.c7

            if self.centerx == 348.75:
                self.fitness = PN.c8

            if self.centerx == 393.75:
                self.fitness = PN.c9

            if self.centerx == 438.75:
                self.fitness = PN.c10

            if self.centerx == 483.75:
                self.fitness = PN.c11

            if self.centerx == 528.75:
                self.fitness = PN.c12

            if self.centerx == 573.75:
                self.fitness = PN.c13

            if self.centerx == 618.75:
                self.fitness = PN.c14

            if self.centerx == 663.75:
                self.fitness = PN.c15

            if self.centerx == 708.75:
                self.fitness = PN.c16

        if self.centery == 236.25:
            if self.centerx == 33.75:
                self.fitness = PN.d1

            if self.centerx == 78.75:
                self.fitness = PN.d2

            if self.centerx == 123.75:
                self.fitness = PN.d3

            if self.centerx == 168.75:
                self.fitness = PN.d4

            if self.centerx == 213.75:
                self.fitness = PN.d5

            if self.centerx == 258.75:
                self.fitness = PN.d6

            if self.centerx == 303.75:
                self.fitness = PN.d7

            if self.centerx == 348.75:
                self.fitness = PN.d8

            if self.centerx == 393.75:
                self.fitness = PN.d9

            if self.centerx == 438.75:
                self.fitness = PN.d10

            if self.centerx == 483.75:
                self.fitness = PN.d11

            if self.centerx == 528.75:
                self.fitness = PN.d12

            if self.centerx == 573.75:
                self.fitness = PN.d13

            if self.centerx == 618.75:
                self.fitness = PN.d14

            if self.centerx == 663.75:
                self.fitness = PN.d15

            if self.centerx == 708.75:
                self.fitness = PN.d16

        if self.centery == 281.25:
            if self.centerx == 33.75:
                self.fitness = PN.e1

            if self.centerx == 78.75:
                self.fitness = PN.e2

            if self.centerx == 123.75:
                self.fitness = PN.e3

            if self.centerx == 168.75:
                self.fitness = PN.e4

            if self.centerx == 213.75:
                self.fitness = PN.e5

            if self.centerx == 258.75:
                self.fitness = PN.e6

            if self.centerx == 303.75:
                self.fitness = PN.e7

            if self.centerx == 348.75:
                self.fitness = PN.e8

            if self.centerx == 393.75:
                self.fitness = PN.e9

            if self.centerx == 438.75:
                self.fitness = PN.e10

            if self.centerx == 483.75:
                self.fitness = PN.e11

            if self.centerx == 528.75:
                self.fitness = PN.e12

            if self.centerx == 573.75:
                self.fitness = PN.e13

            if self.centerx == 618.75:
                self.fitness = PN.e14

            if self.centerx == 663.75:
                self.fitness = PN.e15

            if self.centerx == 708.75:
                self.fitness = PN.e16

        if self.centery == 326.25:
            if self.centerx == 33.75:
                self.fitness = PN.f1

            if self.centerx == 78.75:
                self.fitness = PN.f2

            if self.centerx == 123.75:
                self.fitness = PN.f3

            if self.centerx == 168.75:
                self.fitness = PN.f4

            if self.centerx == 213.75:
                self.fitness = PN.f5

            if self.centerx == 258.75:
                self.fitness = PN.f6

            if self.centerx == 303.75:
                self.fitness = PN.f7

            if self.centerx == 348.75:
                self.fitness = PN.f8

            if self.centerx == 393.75:
                self.fitness = PN.f9

            if self.centerx == 438.75:
                self.fitness = PN.f10

            if self.centerx == 483.75:
                self.fitness = PN.f11

            if self.centerx == 528.75:
                self.fitness = PN.f12

            if self.centerx == 573.75:
                self.fitness = PN.f13

            if self.centerx == 618.75:
                self.fitness = PN.f14

            if self.centerx == 663.75:
                self.fitness = PN.f14

            if self.centerx == 708.75:
                self.fitness = PN.f16
