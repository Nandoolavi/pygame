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

from pygame.locals import *
import pygame 

WIDTH = 500
HEIGHT = 400
FPS = 60

BLACK = (13, 13, 13)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Título game")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sceen.fill(BLACK)
    pygame.display.flip()

pygame.quit()