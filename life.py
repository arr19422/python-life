from math import log
import pygame
import random

class Life(object):
    def __init__(self, screen):
        self.screen = screen

    def clear(self):
        self.screen.fill((0, 0, 0))
    
    def initial(self, width, height):
        for i in range(0, 50):
            x = random.randint(0, width)
            y = random.randint(0, height)
            self.pixel(x, y, (255,255,255))

            self.pixel(x-1, y-1, (255,255,255))
            self.pixel(x+1, y-1, (255,255,255))
            self.pixel(x-2, y-2, (255,255,255))
            self.pixel(x, y-2, (255,255,255))
            self.pixel(x+2, y-2, (255,255,255))

            self.pixel(x-1, y+1, (255,255,255))
            self.pixel(x+1, y+1, (255,255,255))
            self.pixel(x-2, y+2, (255,255,255))
            self.pixel(x, y+2, (255,255,255))
            self.pixel(x+2, y+2, (255,255,255))
            pygame.display.flip()

    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()

    def render(self, width, height):
        for j in range(0, height):
            for i in range(0, width):
                color = self.prev_turn.get_at((i, j))
                if color == (255, 255, 255):
                    x = -1
                    y = -1
                    countV = 0
                    countM = 0
                    for k in range(0, 3):
                        for v in range(0, 3):
                            if (x == 0 and y == 0):
                                pass
                            else:
                                if (i + x < 0):
                                    if (j + y < 0):
                                        vecino = self.prev_turn.get_at((width-1, height-1))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                    elif (j + y > height-1):
                                        vecino = self.prev_turn.get_at((width-1, 0))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                    else:
                                        vecino = self.prev_turn.get_at((width-1, j + y))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                elif (i + x > width-1):
                                    if (j + y < 0):
                                        vecino = self.prev_turn.get_at((0, height-1))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                    elif (j + y > height-1):
                                        vecino = self.prev_turn.get_at((0, 0))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                    else:
                                        vecino = self.prev_turn.get_at((0, j + y))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1 
                                else:
                                    if (j + y < 0):
                                        vecino = self.prev_turn.get_at((i + x, height-1))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                    elif (j + y > height-1):
                                        vecino = self.prev_turn.get_at((i + x, 0))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                                    else:
                                        vecino = self.prev_turn.get_at((i + x, j + y))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                        elif vecino == (0, 0, 0):
                                            countM += 1
                            x += 1
                        x = -1
                        y += 1

                    if countV < 2:
                        self.pixel(i, j, (0, 0, 0))
                    elif countV == 2 or countV == 3:
                        self.pixel(i, j, (255, 255, 255))
                    elif countM > 3:
                        self.pixel(i, j, (0, 0, 0))
                elif color == (0, 0, 0):
                    x = -1
                    y = -1
                    countV = 0
                    for k in range(0, 3):
                        for v in range(0, 3):
                            if (x == 0 and y == 0):
                                pass
                            else:
                                if (i + x < 0):
                                    if (j + y < 0):
                                        vecino = self.prev_turn.get_at((width-1, height-1))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                    elif (j + y > height-1):
                                        vecino = self.prev_turn.get_at((width-1, 0))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                    else:
                                        vecino = self.prev_turn.get_at((width-1, j + y))
                                        if vecino == (255, 255, 255):
                                            countV += 1 
                                elif (i + x > width-1):
                                    if (j + y < 0):
                                        vecino = self.prev_turn.get_at((0, height-1))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                    elif (j + y > height-1):
                                        vecino = self.prev_turn.get_at((0, 0))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                    else:
                                        vecino = self.prev_turn.get_at((0, j + y))
                                        if vecino == (255, 255, 255):
                                            countV += 1   
                                else:
                                    if (j + y < 0):
                                        vecino = self.prev_turn.get_at((i + x, height-1))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                    elif (j + y > height-1):
                                        vecino = self.prev_turn.get_at((i + x, 0))
                                        if vecino == (255, 255, 255):
                                            countV += 1
                                    else:
                                        vecino = self.prev_turn.get_at((i + x, j + y))
                                        if vecino == (255, 255, 255):
                                            countV += 1 
                            x += 1
                        x = -1
                        y += 1

                    if countV == 3:
                        self.pixel(i, j, (255, 255, 255))

pygame.init()
width = 300
height = 300
screen = pygame.display.set_mode((width, height))

r = Life(screen)
r.clear()
r.initial(width, height)

while True:
    pygame.time.delay(1)
    r.copy()
    r.render(width, height)
    pygame.display.flip()