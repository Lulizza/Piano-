import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from mesh import *

pygame.init()

screen = pygame.display.set_mode((1000, 800), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Piano 3D")

obj = mesh()

def load_texture(path):
    surf = pygame.image.load(path)
    data = pygame.image.tostring(surf, "RGB", True)
    w, h = surf.get_width(), surf.get_height()

    tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return tex

def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glLightfv(GL_LIGHT0, GL_POSITION, (0, 2, 2, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.4, 0.4, 0.4, 1))

    glClearColor(0.8, 0.8, 0.8, 1)
    gluPerspective(60, 1000/800, 0.1, 100)
    glTranslatef(0, 0, -3)

    # texturas
    obj.textura_madeira = load_texture("textures/rosewood_veneer.png")
    obj.textura_tecla = load_texture("textures/keys.png")

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    obj.draw()

init()

running = True
while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False

    display()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()