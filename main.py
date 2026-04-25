import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from loadMesh import LoadMesh
from mesh import *
from Camera import Camera

pygame.init()
background_color = (0.1, 0.1, 0.1, 1)

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Pianin de Cauda')

def load_texture(filename, intensity=1.0):
    try:
        texture_surface = pygame.image.load(filename).convert_alpha()
        
        if intensity < 1.0:
            pelicula = pygame.Surface(texture_surface.get_size(), pygame.SRCALPHA)
            opacidade = int((1.0 - intensity) * 255)
            pelicula.fill((0, 0, 0, opacidade))
            texture_surface.blit(pelicula, (0, 0))

        texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
        width, height = texture_surface.get_size()
        
        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        return tex_id
    except:
        return None

def setup_lighting():
    glEnable(GL_LIGHTING)
    
    # Luz Principal (Ilumina o piano de frente)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.15, 0.15, 0.15, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.4, 0.4, 0.4, 1.0])
    
    # Luz De Contorno (Separa o piano do fundo preto)
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])

def initialise():
    glClearColor(*background_color)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)
    glMatrixMode(GL_MODELVIEW)
    setup_lighting()

piano = LoadMesh("Pianin.obj")

mapa_reflexo = load_texture("textures/GrandPianoReflex.png", intensity=0.35)
piano.set_material_color("Teclas_Brancas", diffuse=[0.95, 0.95, 0.9, 1.0], specular=[0.3, 0.3, 0.3, 1.0], shininess=30.0)
piano.set_material_color("Teclas_Pretas", diffuse=[0.05, 0.05, 0.05, 1.0], specular=[0.5, 0.5, 0.5, 1.0], shininess=100.0)
piano.set_material_color("Madeira_interna", diffuse=[0.6, 0.4, 0.2, 1.0], specular=[0.1, 0.1, 0.1, 1.0], shininess=10.0)
piano.set_material_color("strings.001", diffuse=[0.5, 0.5, 0.5, 0.2], specular=[0.8, 0.8, 0.8, 1.0], shininess=80.0)
piano.set_material_color("Piano", diffuse=[0.02, 0.02, 0.02, 1.0], specular=[0.1, 0.1, 0.1, 1.0], shininess=60.0, texture_id=mapa_reflexo, is_reflective=True)
piano.set_material_color("Suporte", diffuse=[0.02, 0.02, 0.02, 1.0], specular=[0.1, 0.1, 0.1, 1.0], shininess=60.0, texture_id=mapa_reflexo, is_reflective=True)
piano.set_material_color("Pedais", diffuse=[0.8, 0.6, 0.2, 1.0], specular=[0.9, 0.8, 0.3, 1.0], shininess=80.0)

initialise()
minha_camera = Camera()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    minha_camera.update()
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 5.0, 1.0])
    glLightfv(GL_LIGHT1, GL_POSITION, [-5.0, 5.0, -5.0, 1.0])
    
    piano.draw()
    pygame.display.flip()

pygame.quit()