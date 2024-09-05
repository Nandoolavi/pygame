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

class animal:
    def __init__ (self, filo, cor, sexo):
        self.filo = filo
        self.cor = cor
        self.sexo = sexo

    def estudar(self):
        print (f'seu animal é um {self.filo} de cor {self.cor} e de sexo {self.sexo}')

raposa = animal('felino', 'preta', 'masculino')
raposa.estudar()