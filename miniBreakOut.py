# Mini-breakout GL [Silas Henderson 2019]
# -- Press left and right keyboard arrows to move box

# ---------------------------------- Setup ------------------------------ #
							# Libraries								
import pygame 						# -- pygame
from pygame.locals import *                      
from OpenGL.GL import *                             	# -- pyOpenGL
from OpenGL.GLU import *
from numpy.random import random as rand             	# -- numpy
from numpy import cos, sin, linspace, array
							# Variables
ballPos = array([30, 50]) 				# -- ball pos/vel
ballVel = array([ 6,  7])                  
boxPos  = array([15, 10])                           	# -- box pos/vel
boxVel  = 20
w 	= 40 						# -- box width/height
h 	= 10                                      	

pygame.init() 						# Start Pygame
pygame.display.set_mode((500, 500),  	    		# -- opengl window		
	              DOUBLEBUF|OPENGL)
gluOrtho2D(0, 500, 0, 500)                  		# -- 2d window

# ----------------------------  Functions ----------------------------------- #
def drawBall(pos, rad): 				# Draw Ball Fcn
	glBegin(GL_QUADS) 				# -- shape: quad
	glColor3f(.8, .4, .4) 				# -- color: blue
	for i in linspace(0, 361): 			# -- circle vertices
		glVertex2f(pos[0] + rad*cos(i),  
			   pos[1] + rad*sin(i))
	glEnd()

def drawBox(pos, w, h): 				# Draw Box Fcn
	glBegin(GL_QUADS)				# -- shape: quad
	glColor3f(.4, .4, .8)				# -- color: blue
	glVertex(pos[0] - w, pos[1] - h)    		# -- box verticies
	glVertex(pos[0] + w, pos[1] - h)
	glVertex(pos[0] + w, pos[1] + h)
	glVertex(pos[0] - w, pos[1] + h)
	glEnd()

def keyboard(): 					# Keyboard Fcn
	if pygame.key.get_pressed()[pygame.K_LEFT]:     # -- left arrow		
		boxPos[0] = boxPos[0] - boxVel
	if pygame.key.get_pressed()[pygame.K_RIGHT]: 	# -- right arrow
		boxPos[0] = boxPos[0] + boxVel
	
def text2d(position, textString, size):     		# Text Fcn
    font        = pygame.font.Font (None, size) 	# -- set font
    textSurface = font.render(textString, True,  	
    			      (150, 250, 150, 255),     # -- font color
    			      (  0,   0,   0, 255))     # -- font bg color 
    textData    = pygame.image.tostring(\
    	textSurface, "RGBA", True)     
    glRasterPos3d(*position)     
    glDrawPixels(textSurface.get_width(), 
    	         textSurface.get_height(), 
    	         GL_RGBA, GL_UNSIGNED_BYTE, textData)

def refresh(dt): 					# Refresh Fcn
	pygame.display.flip() 				# -- update
	pygame.time.wait(dt) 				# -- pause
	for event in pygame.event.get(): 		# -- check exit
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	glClear(GL_COLOR_BUFFER_BIT| 			# -- clear
		    GL_DEPTH_BUFFER_BIT)

def updateBall(ballPos, ballVel): 			# Ball Update Fcn
	ballPos = ballPos + ballVel 			# -- time step

	if ballPos[0] <   0:  ballVel[0] = -ballVel[0]  # -- bounce left
	if ballPos[0] > 500:  ballVel[0] = -ballVel[0]  # -- bounce right
	if ballPos[1] > 500:  ballVel[1] = -ballVel[1]  # -- bounce up
	if ballPos[1] <  20:  ballVel[1] = -ballVel[1]  # -- bounce low

	if abs(ballPos[0] - boxPos[0]) > w \
	 	and ballPos[1] < 20:   			# -- if miss
		text2d((50, 400, 0), 						
		  'game over: restart in 2 sec', 40)    # ---- text
		ballPos = [500*rand(), 500*rand()] 	# ---- reset ball pos
		refresh(2000)                           	
	return ballPos, ballVel

# ------------------------------ Loop --------------------------------- #
while 1:
	ballPos, ballVel = updateBall(ballPos, ballVel) # Update Ball Pos/Vel
	drawBall(ballPos, h)                            # Draw Ball
	drawBox(boxPos, w, h)                           # Draw Box
	keyboard()                                      # Get keyboard input
	refresh(5)					# Refresh
