# gl Snake {Silas Henderson 2019}
# -- press keys up, down, left, right to move snake

import numpy
import pygame
from   pygame.locals import *
from   OpenGL.GL     import *                             
from   OpenGL.GLU    import *     

# -------------------------- Snake Class ----------------------------------
class Snake:                                                    
    def __init__(self):                                         # Init
        pygame.init()                                           # -- start pygame
        pygame.display.set_mode((500, 500), DOUBLEBUF|OPENGL)   # -- open window
        gluOrtho2D(0, 500, 0, 500)                              # -- set window dims
        glClearColor(.1, .1, .1, 1)                             # -- background color
        
        self.head = numpy.array([50, 50])                       # -- snake head
        self.tail = numpy.array([50, 50])                       # -- snake tail
        self.dir  = numpy.array([ 1,  0])                       # -- snake travel direction
        self.spd  = 1                                           # -- snake travel speed

    def update(self):                                           # Update
        self.spd  = self.spd  + .02                             # -- increase speed
        self.head = self.head + self.spd*self.dir               # -- move head
        self.tail = numpy.append(self.tail, self.head)          # -- add pts to tail

        glBegin(GL_LINE_STRIP)                                  # -- draw pts
        for i in range(1, numpy.size(self.tail)/2):
            glVertex3f(snake.tail[2*i], snake.tail[2*i-1] , 0)
        glEnd()

        pygame.display.flip()                                   # -- update screen
        pygame.time.wait(10)                                    # -- pause
        glClear(GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT)

    def keys(self):
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:    self.dir = numpy.array([ 0, 1])
                if event.key == pygame.K_DOWN:  self.dir = numpy.array([ 0,-1])
                if event.key == pygame.K_LEFT:  self.dir = numpy.array([-1, 0])
                if event.key == pygame.K_RIGHT: self.dir = numpy.array([ 1, 0])

    def game(self):
        while snake.head[0] > 0 and snake.head[0] < 500 and \
              snake.head[1] > 0 and snake.head[1] < 500:
            snake.update()
            snake.keys()

# -------------------------- Loop ------------------------------ 
snake = Snake()
snake.game()