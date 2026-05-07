from OpenGL.GL import *
from mesh import mesh

class LoadMesh(mesh):
    def __init__(self, filename, draw_type=GL_TRIANGLES):
        super().__init__()
        self.filename = filename
        self.draw_type = draw_type
        self.raw_uvs = []
        self.raw_normals = []
        self.load_drawing()

    def load_drawing(self):
        current_material = "default" 
        self.materials[current_material] = []

        with open(self.filename, "r") as fp:
            for line in fp:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split()
                
                if line.startswith("v "):
                    self.vertices.append((float(parts[1]), float(parts[2]), float(parts[3])))
                
                elif line.startswith("vt "):
                    self.raw_uvs.append((float(parts[1]), float(parts[2])))
                
                elif line.startswith("vn "):
                    self.raw_normals.append((float(parts[1]), float(parts[2]), float(parts[3])))
                
                elif line.startswith("usemtl "):
                    current_material = parts[1]
                    if current_material not in self.materials:
                        self.materials[current_material] = [] 

                elif line.startswith("f "):
                    face_points = []
                    for p in parts[1:]:
                        vals = p.split('/')
                        v_idx = int(vals[0]) - 1
                        vt_idx = int(vals[1]) - 1 if len(vals) > 1 and vals[1] else -1
                        vn_idx = int(vals[2]) - 1 if len(vals) > 2 and vals[2] else -1
                        face_points.append((v_idx, vt_idx, vn_idx))

                    for i in range(1, len(face_points) - 1):
                        self.materials[current_material].append(face_points[0])
                        self.materials[current_material].append(face_points[i])
                        self.materials[current_material].append(face_points[i + 1])