# bouncy ball {Silas Henderson 2019}

from   OpenGL.GL     import *
from   OpenGL.GLU    import *
from   pygame.locals import *
from   numpy.random  import random
import pygame
import numpy

pygame.init()
pygame.display.set_mode((500, 500), DOUBLEBUF|OPENGL)
gluOrtho2D(0, 500, 0, 500)      
glClearColor(.05, .05, .05, 1)

def refresh(dt): 									# Refresh Fcn
	pygame.display.flip() 							# -- update
	pygame.time.wait(dt) 							# -- pause
	for event in pygame.event.get(): 				# -- check exit
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	glClear(GL_COLOR_BUFFER_BIT| 					# -- clear
		    GL_DEPTH_BUFFER_BIT)

class Ball:
	def __init__(self):
		self.pos = numpy.array([500*random(), 500*random()])
		self.vel = numpy.array([ 10*random(),  10*random()])
		self.col = (random(), random(), random())
		self.rad = 5 + 10*random()

	def step(self):
		if self.pos[0] <   0: 	self.vel[0] = -self.vel[0]
		if self.pos[0] > 500: 	self.vel[0] = -self.vel[0]
		if self.pos[1] <   0: 	self.vel[1] = -self.vel[1]
		if self.pos[1] > 500: 	self.vel[1] = -self.vel[1]
		
		self.pos = self.pos + self.vel

	def draw(self): 								
		glBegin(GL_QUADS) 								
		glColor3f(*self.col) 							
		for i in numpy.linspace(0, 361): 				
			glVertex2f(self.pos[0] + self.rad*numpy.cos(i),  
		               self.pos[1] + self.rad*numpy.sin(i))
		glEnd()

# ------------------------- Main -------------------------
balls = [Ball() for i in range(0, 20)]

while 1:
	for i in range(0, 20):
		balls[i].draw()
		balls[i].step()
	refresh(5)