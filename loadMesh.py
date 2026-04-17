from OpenGL.GL import *
from mesh import *
import pygame

class LoadMesh(mesh):
    def __init__(self, filename, draw_type):
        self.vertices = []
        self.triangles = []
        self.filename = filename
        self.draw_type = draw_type
        self.load_drawing()

    def load_drawing(self):
        with open(self.filename, "r") as fp:
            for line in fp:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if line.startswith("v "):
                    parts = line.split()
                    vx, vy, vz = float(parts[1]), float(parts[2]), float(parts[3])
                    self.vertices.append((vx, vy, vz))

                elif line.startswith("f "):
                    parts = line.split()[1:]

                    face = []
                    for p in parts:
                        index = int(p.split('/')[0]) - 1
                        face.append(index)

                    # triangula
                    for i in range(1, len(face) - 1):
                        self.triangles.append(face[0])
                        self.triangles.append(face[i])
                        self.triangles.append(face[i + 1])