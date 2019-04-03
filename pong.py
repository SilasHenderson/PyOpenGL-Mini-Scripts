

# --------------------------- Setup ------------------------------ #
import numpy 										# Libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy.random import random as rand

ballPos = numpy.array([30, 50]) 					# Variables
ballVel = numpy.array([ 6,  7])
boxPos  = numpy.array([15, 10])
boxVel  = 20

w = 40
h = 10

pygame.init() 										# Start Pygame
pygame.display.set_mode((500, 500), 
	             DOUBLEBUF|OPENGL)
gluOrtho2D(0, 500, 0, 500)

# -------------------------------  Functions -------------------------
def drawBall(pos, rad): 							# Draw Ball Fcn
	glBegin(GL_QUADS) 								# -- shape: quad
	glColor3f(.8, .4, .4) 							# -- color: blue
	for i in numpy.linspace(0, 361): 				# -- circle vertices
		glVertex2f(pos[0] + rad*numpy.cos(i),  
			       pos[1] + rad*numpy.sin(i))
	glEnd()

def drawBox(pos, w, h): 							# Draw Box Fcn
	glBegin(GL_QUADS)								# -- shape: quad
	glColor3f(.4, .4, .8)							# -- color: blue
	glVertex(pos[0] - w, pos[1] - h)    			# -- box verticies
	glVertex(pos[0] + w, pos[1] - h)
	glVertex(pos[0] + w, pos[1] + h)
	glVertex(pos[0] - w, pos[1] + h)
	glEnd()

def keyboard(): 									# Keyboard
	key = pygame.key.get_pressed();
	if key[pygame.K_LEFT]: 	boxPos[0] = boxPos[0] - boxVel
	if key[pygame.K_RIGHT]: boxPos[0] = boxPos[0] + boxVel
	if key[pygame.K_UP]:    resetFlag = 1

def text2d(position, textString, size):     
    font = pygame.font.Font (None, size)
    textSurface = font.render(textString, True, (255,255,255,255), (0,0,0,255))     
    textData = pygame.image.tostring(textSurface, "RGBA", True)     
    glRasterPos3d(*position)     
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def refresh(dt):
	pygame.display.flip()
	pygame.time.wait(dt)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

# -------------------- Loop ------------------
while 1:

	keyboard()
	ballPos = ballPos + ballVel	
	if ballPos[0] <   0:	ballVel[0] = -ballVel[0]
	if ballPos[0] > 500:    ballVel[0] = -ballVel[0]
	if ballPos[1] > 500:	ballVel[1] = -ballVel[1]

	if ballPos[1] <  20:    
		ballVel[1] = -ballVel[1]
		if abs(ballPos[0] - boxPos[0]) > w:
			text2d((50, 400, 0), 'game over: restart in 2 sec', 40)
			ballPos = [500*rand(), 500*rand()]
			refresh(2000)

	drawBall(ballPos, h)
	drawBox(boxPos, w, h)
	refresh(5)