from OpenGL.GL import *
import pygame

class mesh:
    def __init__(self):
        #equivalem aos dados das pontas do objeto
        self.vertices = [
                        #retangulo acima das teclas
                         (0.5, -0.05, 0.5), #0 direita baixo
                         (-0.5, -0.05, 0.5), #1 esquerda baixo
                         (0.5, 0.15, 0.5), #2 direita cima
                         (-0.5, 0.15, 0.5), #3 esquerda cima

                        #base para as teclas
                         (0.5, -0.05, 0.70),  # 4 direta
                         (-0.5, -0.05, 0.70),  # 5 esquerda

                         (-0.5, -0.10, 0.5), #6 esquerda
                         (0.5, -0.10, 0.5), #7 direita
                         (-0.5, -0.10, 0.70), #8 esquerda
                         (0.5, -0.10, 0.70), #9 direita




                        ]

        # costrução estrutura do piano
        self.estrutura = [
                            1,0,2,3, #retangulo acima das teclas
                            1,0,4,5,  #base para as teclas
                            6,8,9,7, #profundidade da base
                            

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

