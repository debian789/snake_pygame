import pygame
import util
from pygame.sprite import  Sprite
from pygame import *



class Snake(Sprite):
    def __init__(self, escenario):
        Sprite.__init__(self)
        self.cargar_imagenes()
        self.imagen = self.normal
        self.rect = self.imagen.get_rect()
       # self.rect.centery = 50  # escenario.HEIGHT / 2
        # self.rect.centerx = 50  # escenario.WIDTH / 2
        self.rect.centerx = escenario.pantalla()["width"] / 2
        self.rect.centery = escenario.pantalla()["height"] / 2 
        self.velocidad = 5
        self.UpDown = True
        self.LeftRight = True
        self.control = True
        
        
         
        
        
        
        
        
    def cargar_imagenes(self):
        self.normal = util.cargar_imagen('snake.png')
        
        
       
        
    def actualizar(self, teclas, tick):
        # teclas = pygame.key.get_pressed()
        
        if self.control:
            if self.UpDown:
                self.rect.centerx -= tick / 2
                print self.rect 
            else:
                self.rect.centerx += tick / 2
        else:
            if self.LeftRight:
                self.rect.centery -= tick / 2
            else:
                self.rect.centery += tick / 2
         
            
        
        
        if teclas[K_LEFT]:
            self.UpDown = True
            self.control = True
             # self.rect.centerx -= tick  # (-1, 0)
        elif teclas[K_RIGHT]:
            self.UpDown = False
            self.control = True
             # self.rect.centerx += tick  # 1 * self.velocidad  # (+1, 0)
        elif teclas[K_UP]:
            self.LeftRight = True
            self.control = False
           # self.rect.centery -= tick  # 1 * self.velocidad  # (0, -1)
        elif teclas[K_DOWN]:
            self.LeftRight = False
            self.control = False
            # self.rect.centery += tick  # 1 * self.velocidad  # (0, +1)
            
#         if teclas[K_LEFT]:
#              self.rect.centerx -= 1 * self.velocidad  # (-1, 0)
#         elif teclas[K_RIGHT]:
#              self.rect.centerx += 1 * self.velocidad  # (+1, 0)
#         elif teclas[K_UP]:
#             self.rect.centery -= 1 * self.velocidad  # (0, -1)
#         elif teclas[K_DOWN]:
#             self.rect.centery += 1 * self.velocidad  # (0, +1)
            
            
