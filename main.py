import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from loadMesh import LoadMesh

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0.1, 0.1, 0.1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Pianin de Cauda')

def load_texture(filename):
    try:
        texture_surface = pygame.image.load(filename)
        texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
        width = texture_surface.get_width()
        height = texture_surface.get_height()

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        return tex_id
    except:
        print(f"Não foi possível carregar a textura: {filename}")
        return None

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 5.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.9, 0.9, 0.9, 1.0])

def initialise():
    glClearColor(*background_color)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    setup_lighting()

piano = LoadMesh("Pianin.obj")

# Configurando as cores baseadas nas partes do .obj
piano.set_material_color("Teclas_Brancas", diffuse=[0.9, 0.9, 0.9, 1.0]) # Branco
piano.set_material_color("Teclas_Pretas", diffuse=[0.05, 0.05, 0.05, 1.0], shininess=100.0) # Preto
piano.set_material_color("Piano", diffuse=[0.25, 0.12, 0.05, 1.0]) # Marrom escuro 
piano.set_material_color("Madeira_interna", diffuse=[0.6, 0.4, 0.2, 1.0]) # Marrom claro
piano.set_material_color("strings.001", diffuse=[0.8, 0.7, 0.2, 1.0], shininess=80.0) # Dourado

done = False
initialise()
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    glTranslate(0, -1, -5)
    glRotatef(pygame.time.get_ticks() / 50, 0, 1, 0)
    
    piano.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()