from OpenGL.GL import *
import pygame

class mesh:
    def __init__(self):
        #equivalem aos dados das pontas do triangulo
        self.vertices = [
                         (0.5, -0.5, 0.5), #0
                         (-0.5, -0.5, 0.5), #1
                         (0.5, 0.5, 0.5), #2
                         (-0.5, 0.5, 0.5), #3
                        ]

        # pontas dos triangulos
        self.triangles = [0, 2, 3, 0, 3, 1]
        #desenha a forma conforme os dados anteriores
        self.draw_type = GL_LINE_LOOP

    #desenha as pontas
    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t+1]])
            glVertex3fv(self.vertices[self.triangles[t+2]])
            glEnd()
