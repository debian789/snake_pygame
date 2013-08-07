# -*- coding: utf-8 -*-
import util
import pygame

WIDTH = 640
HEIGHT = 480


class Escenario():

    def __init__(self):
        self.fond = util.cargar_imagen("fondo.jpg")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self.fondo = util.cargar_imagen("fondo.jpg", transparencia=True)

        
    def pantalla(self):
        return {"width":WIDTH, "height":HEIGHT}
