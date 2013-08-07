# -*- coding: utf-8 -*-
import sys, pygame
from pygame.locals import *
import util
from escenario import Escenario
from pkPersonajes.snake import Snake
from pkPersonajes.comida import Comida



def main():
	escenario = Escenario()
	escenario.screen
	serpiente = Snake(escenario)
	raton = Comida(escenario)
	temporizador = pygame.time.Clock()

	while True:
		keys = pygame.key.get_pressed()
		serpiente.actualizar(keys, temporizador.tick(60))
		
		# serpiente.actualizar(keys)
		escenario.screen.blit(escenario.fondo, (0, 0))
		escenario.screen.blit(serpiente.imagen, (serpiente.rect.centerx, serpiente.rect.centery))
		escenario.screen.blit(raton.imagen, (raton.rect.centerx, raton.rect.centery))
		
		
		if raton.colision(serpiente):
			raton.comer()
		
		pygame.display.flip()
		temporizador.tick(60)
 		util.salir(keys)	
 		
 	return 0		
 		
if __name__ == '__main__':
	pygame.init()
	main()		
