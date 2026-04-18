import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from loadMesh import LoadMesh
from mesh import *

pygame.init()

mesh = LoadMesh("Pianin.obj", GL_TRIANGLES)

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

eye = [0, 0, 0]

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)

def init_camera():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 1,- -2)
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glRotatef(1, 10, 0, 1)
    init_camera()
    glPushMatrix()
    mesh.draw()
    glPopMatrix()

done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        eye[2] += 1
    if keys[pygame.K_UP]:
        eye[2] -= 1
    if keys[pygame.K_LEFT]:
        eye[0] -= 1
    if keys[pygame.K_RIGHT]:
        eye[0] += 1
    display()
    pygame.display.flip()
    pygame.time.wait(60);
pygame.quit()