from OpenGL.GL import *
import pygame

class mesh:
    def __init__(self):
        #equivalem aos dados das pontas do objeto
        self.vertices = [
                         (0.5, -0.15, 0.5), #0
                         (-0.5, -0.15, 0.5), #1
                         (0.5, 0.15, 0.5), #2
                         (-0.5, 0.15, 0.5), #3

                         (0.5, -0.5, -0.5),  # 4
                         (-0.5, -0.5, -0.5),  # 5
                         (0.5, 0.5, -0.5),  # 6
                         (-0.5, 0.5, -0.5)  # 7
                        ]

        # costrução estrutura do piano
        self.estrutura = [
                            1,0,2,3#retangulo acima das teclas
                        ]
        #desenha a forma conforme os dados anteriores
        self.draw_type = GL_LINE_LOOP

    #desenha as pontas
    def draw(self):
        for t in range(0, len(self.estrutura), 4):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.estrutura[t]])
            glVertex3fv(self.vertices[self.estrutura[t+1]])
            glVertex3fv(self.vertices[self.estrutura[t+2]])
            glVertex3fv(self.vertices[self.estrutura[t+3]])
            glEnd()

