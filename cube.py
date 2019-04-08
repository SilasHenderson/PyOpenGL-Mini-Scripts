# ut Cube {Silas Henderson 2019}

import pygame 							  	# pygame
from   pygame.locals import *
from   OpenGL.GL     import *                              	  	# opengl
from   OpenGL.GLU    import *
from   OpenGL.GLUT   import *  
# ----------------------- Setup ---------------------------- 
pygame.init(); 							  	# Init
glutInit();

pygame.display.set_mode((500, 500),  DOUBLEBUF|OPENGL) 		  	# Window
gluPerspective(70, 1, .01, 1000) 				  	# -- camEye
glTranslate(0, 0, - 50)                                           	# -- camPos

# ----------------------- Loop -----------------------------
while 1:														
	glRotate(1, 1, 1, 1); 		glutSolidCube(20, 20, 20);    	# rotate, render
	pygame.display.flip();  	    pygame.time.delay(10);    	# refresh, pause
	glClear(GL_COLOR_BUFFER_BIT);                             	# clear

	for event in pygame.event.get(): 				# check input
		if event.type == pygame.QUIT: pygame.quit(); quit();  	# -- close (x)
