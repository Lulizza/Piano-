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

                        #corpo triangulo  primeiro quad
                        (0.5, 0.15, -0.25), #10 direita pra dentro
                        (-0.5, 0.15, -0.25) #11 esquerda pra dentro

                        ]

        # costrução estrutura do piano
        self.estrutura = [
                            #corpo
                            1,0,2,3, #retangulo acima das teclas
                            3,2,10,11, #corpo triangulo
                            
                            #teclas
                            1,0,4,5,  #base para as teclas
                            6,8,9,7, #profundidade da base
                            1,6,8,5,  #ligação entre a base e a profundidade esquerda
                            0,7,9,4,  #ligação entre a base e a profundidade direita
                            4,9,8,5,   #ligação entre a base e a profundidade frente
                            2,7,6,3   #ligação entre a base e a profundidade trás
                                                        
                            #
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

