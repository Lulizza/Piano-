import pygame
from OpenGL.GLU import *
from math import *

class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 2, 6)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.look = pygame.math.Vector3(0, 0, 0)
        self.yaw = 0.0
        self.pitch = 20.0
        self.distance = 6.0
        self.speed = 1.5
        self.zoom_speed = 0.2

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.yaw -= self.speed
        if keys[pygame.K_RIGHT]:
            self.yaw += self.speed
        if keys[pygame.K_UP]:
            self.pitch += self.speed
        if keys[pygame.K_DOWN]:
            self.pitch -= self.speed
        if keys[pygame.K_w]:
            self.distance -= self.zoom_speed
        if keys[pygame.K_s]:
            self.distance += self.zoom_speed
            
        if self.pitch > 89.0: self.pitch = 89.0
        if self.pitch < -89.0: self.pitch = -89.0
        if self.distance < 1.0: self.distance = 1.0

        self.eye.x = self.look.x + self.distance * cos(radians(self.pitch)) * sin(radians(self.yaw))
        self.eye.y = self.look.y + self.distance * sin(radians(self.pitch))
        self.eye.z = self.look.z + self.distance * cos(radians(self.pitch)) * cos(radians(self.yaw))

        gluLookAt(self.eye.x, self.eye.y, self.eye.z, 
                  self.look.x, self.look.y, self.look.z, 
                  self.up.x, self.up.y, self.up.z)