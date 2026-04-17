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
            (0.5, 0.15, -0.25), #10 direita cima dentro
            (-0.5, 0.15, -0.25), #11 esquerda cima dentro
            (0.5, -0.10, 0.5), #12 direita baixo fora
            (-0.5, -0.10, 0.5), #13 esquerda baixo fora
            (0.5, -0.10, -0.25), #14 direita baixo dentro
            (-0.5, -0.10, -0.25), #15 esquerda baixo dentro
                        
            #pé esquerdo do piano
            (-0.5, -0.12, 0.45), #16 esquerda cima dentro
            (-0.37, -0.12, 0.45), #17 direita cima dentro
            (-0.5, -0.12, 0.60), #18 esquerda cima fora
            (-0.37, -0.12, 0.60), #19 direita cima fora 
            (-0.47, -0.6, 0.48), #20 esquerda baixo dentro
            (-0.40, -0.6, 0.48), #21 direita baixo dentro
            (-0.47, -0.6, 0.57), #22 esquerda baixo fora
            (-0.40, -0.6, 0.57), #23 direita baixo fora

            #pé direito do piano
            (0.5, -0.12, 0.45), #24 esquerda cima dentro
            (0.37, -0.12, 0.45), #25 direita cima dentro
            (0.5, -0.12, 0.60), #26 esquerda cima fora
            (0.37, -0.12, 0.60), #27 direita cima fora
            (0.47, -0.6, 0.48), #28 esquerda baixo dentro
            (0.40, -0.6, 0.48), #29 direita baixo dentro
            (0.47, -0.6, 0.57), #30 esquerda baixo fora
            (0.40, -0.6, 0.57) #31 direita baixo fora
        ]

        # costrução estrutura do piano
        self.estrutura = [
            #corpo
            1,0,2,3,
            3,2,10,11,
            12,13,15,14,
            3,11,15,13,
            2,10,14,12,
            10, 11, 15, 14,
            0,1,13,12,
                            
            #teclas
            1,0,4,5,
            6,8,9,7,
            1,6,8,5,
            0,7,9,4,
            4,9,8,5,
            2,7,6,3,

            #pé esquerdo piano
            16,17,19,18,
            20,21,23,22,
            16,18,22,20,
            17,19,23,21,
            18,22,23,19,
            16,20,21,17,

            #pé direito piano
            24,25,27,26,
            28,29,31,30,
            24,26,30,28,
            25,27,31,29,
            24,25,29,28,
            26,27,31,30
        ]

        # separar partes
        self.partes = {
            "corpo": self.estrutura[0:28],
            "teclas": self.estrutura[28:52],
            "pes": self.estrutura[52:]
        }

        # texturas
        self.textura_madeira = None
        self.textura_tecla = None

    def draw_parte(self, indices, cor, textura):
        glBindTexture(GL_TEXTURE_2D, textura)
        glColor3f(*cor)

        for t in range(0, len(indices), 4):
            glBegin(GL_QUADS)

            glTexCoord2f(0, 0)
            glVertex3fv(self.vertices[indices[t]])

            glTexCoord2f(1, 0)
            glVertex3fv(self.vertices[indices[t+1]])

            glTexCoord2f(1, 1)
            glVertex3fv(self.vertices[indices[t+2]])

            glTexCoord2f(0, 1)
            glVertex3fv(self.vertices[indices[t+3]])

            glEnd()

    def draw(self):
        # corpo (madeira)
        self.draw_parte(self.partes["corpo"], (0.7, 0.7, 0.7), self.textura_madeira)

        # teclas (brancas)
        self.draw_parte(self.partes["teclas"], (1, 1, 1), self.textura_tecla)

        # pés
        self.draw_parte(self.partes["pes"], (0.2, 0.2, 0.2), self.textura_madeira)