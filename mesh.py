from OpenGL.GL import *

class mesh:
    def __init__(self):
        self.vertices = []
        self.draw_type = GL_TRIANGLES
        
        self.materials = {} 
        self.material_settings = {} 

        self.default_diffuse = [0.8, 0.8, 0.8, 1.0]
        self.default_specular = [1.0, 1.0, 1.0, 1.0]
        self.default_shininess = 50.0

    def set_material_color(self, mat_name, diffuse, specular=[1.0, 1.0, 1.0, 1.0], shininess=50.0, texture_id=None):
        self.material_settings[mat_name] = {
            "diffuse": diffuse,
            "specular": specular,
            "shininess": shininess,
            "texture_id": texture_id
        }

    def draw(self):
        for mat_name, triangles in self.materials.items():
            
            settings = self.material_settings.get(mat_name, {
                "diffuse": self.default_diffuse,
                "specular": self.default_specular,
                "shininess": self.default_shininess,
                "texture_id": None
            })

            glMaterialfv(GL_FRONT, GL_DIFFUSE, settings["diffuse"])
            glMaterialfv(GL_FRONT, GL_SPECULAR, settings["specular"])
            glMaterialf(GL_FRONT, GL_SHININESS, settings["shininess"])

            tex_id = settings["texture_id"]
            if tex_id is not None:
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, tex_id)
            else:
                glDisable(GL_TEXTURE_2D)

            glBegin(self.draw_type)
            for vertex_data in triangles:
                if isinstance(vertex_data, tuple):
                    v_idx, vt_idx, vn_idx = vertex_data
                    
                    if vn_idx != -1 and hasattr(self, 'raw_normals'):
                        glNormal3fv(self.raw_normals[vn_idx])
                    
                    if vt_idx != -1 and hasattr(self, 'raw_uvs'):
                        glTexCoord2fv(self.raw_uvs[vt_idx])
                    
                    glVertex3fv(self.vertices[v_idx])
                else:
                    glVertex3fv(self.vertices[vertex_data])
            glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)