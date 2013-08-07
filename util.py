# -*- coding: utf-8 -*-
import pygame, os, sys
from pygame.locals import *
from random import randint

 

def cargar_imagen(nombre, transparencia=False):
    ruta = os.path.join('imagenes', nombre)
    imagen = pygame.image.load(ruta)
    return imagen

def salir(keys):
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
        if keys[K_ESCAPE]:
            sys.exit(0)

def aleatorioPosicion(max_width, max_height):
    return randint(0, max_width), randint(0, max_height)
     
