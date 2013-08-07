import pygame
import util
from pygame.sprite import  Sprite

from pygame.locals import *



class Comida(Sprite):
    def __init__(self, escenario):
        Sprite.__init__(self)
        self.cargar_imagenes()
        self.imagen = self.normal
        self.rect = self.imagen.get_rect()
        self.rect_colision = self.rect.inflate(-30, -10)
        self.escenario = escenario
       # self.rect.centery = 50  # escenario.HEIGHT / 2
        # self.rect.centerx = 50  # escenario.WIDTH / 2
        self.rect.centerx = 50
        self.rect.centery = 100 
           

        
    def cargar_imagenes(self):
        self.normal = util.cargar_imagen('comida.png')
        
    def comer(self):
        self.rect.centerx , self.rect.centery = util.aleatorioPosicion(self.escenario.pantalla()["width"], self.escenario.pantalla()["height"]) 
        self.kill()
        
    def colision(self, snake):
        if pygame.sprite.collide_rect(self, snake):
            return True
        else: 
            return False
            
            # self.imagen = None
        
            
        

