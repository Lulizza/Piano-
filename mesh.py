from OpenGL.GL import *

class mesh:
    def __init__(self):
        self.vertices = []
        self.materials = {} 
        self.material_settings = {} 
        self.draw_type = GL_TRIANGLES
        self.default_diffuse = [0.8, 0.8, 0.8, 1.0]
        self.default_specular = [1.0, 1.0, 1.0, 1.0]
        self.default_shininess = 50.0

    def set_material_color(self, mat_name, diffuse, specular=[1.0, 1.0, 1.0, 1.0], shininess=50.0, texture_id=None, is_reflective=False):
        self.material_settings[mat_name] = {
            "diffuse": diffuse,
            "specular": specular,
            "shininess": shininess,
            "texture_id": texture_id,
            "is_reflective": is_reflective # SALVAMOS AQUI
        }

    def draw(self):
        for mat_name, triangles in self.materials.items():
            settings = self.material_settings.get(mat_name, {
                "diffuse": self.default_diffuse,
                "specular": self.default_specular,
                "shininess": self.default_shininess,
                "texture_id": None,
                "is_reflective": False
            })

            glMaterialfv(GL_FRONT, GL_DIFFUSE, settings["diffuse"])
            glMaterialfv(GL_FRONT, GL_SPECULAR, settings["specular"])
            glMaterialf(GL_FRONT, GL_SHININESS, settings["shininess"])

            tex_id = settings["texture_id"]
            reflective = settings["is_reflective"]

            if tex_id is not None:
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, tex_id)
                
                if reflective:
                    glEnable(GL_TEXTURE_GEN_S)
                    glEnable(GL_TEXTURE_GEN_T)
                    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
                    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
                    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_ADD) 
            else:
                glDisable(GL_TEXTURE_2D)

            glBegin(self.draw_type)
            for vertex_data in triangles:
                if isinstance(vertex_data, tuple):
                    v_idx, vt_idx, vn_idx = vertex_data
                    
                    if vn_idx != -1 and hasattr(self, 'raw_normals'):
                        glNormal3fv(self.raw_normals[vn_idx])
                    
                    if vt_idx != -1 and hasattr(self, 'raw_uvs') and not reflective:
                        glTexCoord2fv(self.raw_uvs[vt_idx])
                    
                    glVertex3fv(self.vertices[v_idx])
                else:
                    glVertex3fv(self.vertices[vertex_data])
            glEnd()

            if tex_id is not None:
                if reflective:
                    glDisable(GL_TEXTURE_GEN_S)
                    glDisable(GL_TEXTURE_GEN_T)
                    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
                glBindTexture(GL_TEXTURE_2D, 0)
            glDisable(GL_TEXTURE_2D)