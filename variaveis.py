#linguagem = "Python"
#
#if linguagem == "C++":
#    print('C++ é uma linguagem de progamção compilada')
#elif linguagem == "Python":
#    print; ("Python é uma linguagem de programação de alto nível")
#elif linguagem == "Java":
#    print("Java é uma linguagem de programação amplamente utilizada no mercado")
#else:
#    print('não é nenhuma das opçoes') 

#x = 0
#while x != 10:
#    print(x)
#    x+=1

#x=0
#for i in range (10):
#    print(x)

#Jogadores = ['Márcio', 'laiur', 'jaksd', 'spdlf']
#Pontos = [359, 254, 235, 3565,]
#tamanho_lista = len(Jogadores)
#indice = 0
#
#print('Lista usando WHILE')
#while (indice < tamanho_lista):
#    print(Jogadores[indice], '\t: \t', Pontos[indice])
#    indice += 1

#Recordes = {'Arthur' : 100, 'erick' : 200, 'Felipe' : 400, 'Murilo' : 500, 'Victor': 600}
#
#print("\nLista usando FOR com DICTIONARY:")
#for nome, recorde in Recordes.items() :
#    print (nome, "\t:\t", recorde)

#def funcao():
#    print("Pedro 1")

#funcao()

#def sum(a, b, c):
#    print ((a + b)*c)
#
#sum(c=1, b=4, a=5)

#a = int(input("quantas anos vc ter"))

#def tabuada():
#   a = int(input('qual valor voce deseja usar'))
#   print(f'{a} X 1 =' + str(a *1))
#   print(f'{a} X 2 =' + str(a *2))
#   print(f'{a} X 3 =' + str(a *3))
#   print(f'{a} X 4 =' + str(a *4))
#   print(f'{a} X 5 =' + str(a *5))
#   print(f'{a} X 6 =' + str(a *6))
#   print(f'{a} X 7 =' + str(a *7))
#   print(f'{a} X 8 =' + str(a *8))
#   print(f'{a} X 9 =' + str(a *9))
#   print(f'{a} X 10 =' + str(a *10))
#
#tabuada()

#class animal:
#    def __init__ (self, filo, cor, sexo):
#        self.filo = filo
#        self.cor = cor
#        self.sexo = sexo
#
#    def estudar(self):
#        print (f'seu animal é um {self.filo} de cor {self.cor} e de sexo {self.sexo}')
#
#raposa = animal('felino', 'preta', 'masculino')
#raposa.estudar()

#import pygame
#from pygame.Locals import *
#
#pygame.init()
#screen = pygame.display.set_mode((600, 600))
#pygame.display.set_caption('Snake')
#
#snake = [(200, 200), (210, 200), (220,200)]
#snake_skin = pygame.Surface((10,10))
#snake_skin.fill((255,255,255)) #Branco
#
#while True:
#  for event in pygame.event.get():
#    if event.type == QUIT:
#      pygame.quit()
#      exit()
#  screen.fill((0,0,0))
#  for pos in snake:
#    screen.blit(snake_skin,pos)
#  pygame.display.update()
#  
#  UP = 0
#  RIGHT = 1
#  DOWN = 2
#  LEFT = 3
#  
#  pygame.init()
#  screen = pygame.display.set_mode((600,600))
#  pygame_skin.fill((255,255,255))
#  
#  my_direction = LEFT
#  
#  while True:
#    for event in pygame.event.get():
#      if event.type == QUIT:
#        pygame.quit()
#        exit()
#        
#    if event.type == KEYDOWN:
#      
#      if event.key == K_UP: my_direction = UP
#      if event.key == K_DOWN: my_direction = DOWN
#      if event.key == K_LEFT: my_direction = LEFT
#      if event.key == K_RIGHT: my_direction = RIGHT
#      
#for i in range(len(snake) - 1, 0, -1):
#  snake[i] = (snake[i-1][0], snake[i-1][1])
#  
#if my_direction == UP:
#    snake[0] = (snake[0][0], snake[0][1] - 10)
#import pygame
#pygame.init()
#
#screen = pygame.display.set_mode((1000,1000))
#pygame.display.set_caption("Eventos")
#
#running = True
#while running:
#    for event in pygame.event.get():
#        print(event)
#        if event.type == pygame.QUIT:
#            running = False

#import pygame
#from pygame.Locals import *
#import random
#
#def on_grid_random()
#    x = random.randint(0,59)
#    y = random.randint(0,59)
#     return (x * 10, y * 10)
#UP = 0
#RIGHT = 1
#DOWN = 2
#LEFT = 3
#
#pygame.init()
#screen = pygame.display.set_mode((600, 600))
#pygame.display.set_caption
#
#for i in range(Len  )

import pygame as pg
pg.init()
#
#screen = pygame.display.set_mode((625, 220))
#screen.fill((255, 255, 255)) # Fundo branco
#
#while True:
#
#    pygame.draw.rect(screen, (255, 0, 0), (50, 20, 120, 100))
#    pygame.draw.rect(screen, (0, 255, 0), (100, 60, 120, 100))
#    pygame.draw.rect(screen, (0, 0, 255), (150, 100, 120, 100))
#
#    pygame.draw.rect(screen, (255, 0, 0), (350, 20, 120, 100),1)
#    pygame.draw.rect(screen, (0, 255, 0), (400, 60, 120, 100),4)
#    pygame.draw.rect(screen, (0, 0, 255), (450, 100, 120, 100),8)
#
#    pygame.display.flip()
#
#    for event in  pygame.event.get():
#        if event.type == pygame.QUIT:
#            exit()
#
from math import pi

RED = (255, 0, 0)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
BLUE= (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

width = 600
height = 450
screen = pg.display.set_mode((width, height))


retangulos = [
    pg.Rect(20, 20, 100, 50),
    pg.Rect(20, 90, 50, 50),
    pg.Rect(500, 30, 80, 60)
]

while True:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    for retangulo in retangulos:
        pg.draw.rect(screen, BLUE, retangulo)

    pg.draw.rect(screen, GREEN, [115, 280, 70, 40])
    pg.draw.rect(screen, RED, [115, 280, 71, 41], 2)
    pg.draw.circle(screen, YELLOW, (325,70), 30)
    pg.draw.circle(screen, BLUE, [250, 250], 25, True)
    pg.draw.ellipse(screen, WHITE, (250, 300, 100, 100))
    pg.draw.arc(screen, RED, [430, 150, 150, 125], pi/100, 1.13*pi, 2)
    pg.draw.line(screen, BLUE, (0, height-100), (width, height-100), 5)
    pg.draw.aaline(screen, GREEN, (0, height-200), (width, height-200))
    pg.draw.lines(screen, WHITE, False, [[400, 400], [400, 20], [200, 20]], 2)
    pg.draw.polygon(screen, YELLOW, [[140, 120], [100, 200], [300, 200]])
    pg.draw.polygon(screen, GREEN, [[140, 120], [100, 200], [300,200]])
    pg.display.update()