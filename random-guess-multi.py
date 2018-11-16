# encoding: utf-8
# versión en Python 2.7 [Server centOS 6] pero semi-preparado para Python 3
# (C) 2018 Alejandro Moliné

import random

global IdiomaSelec # Selected language, a global variable

#### Begin lists that hold "multi-lingual" messages
ElijNum = ["Elija un número de 1 a 10: ", "Escolha um número de 1 a 10: ", "Choose a number between 1 and 10: "]
EseNoes = ["¡Falló!","¡Errou!","Fail!"]
Mayor = ["Es mayor que ese número.", "É maior que esse número.", "It's higher than that."]
Menor = ["Es menor que ese número","É menor que esse número.","It's lower than that."]
Final = ["¡Acertó!","¡Acertou!","You're right!"]
#### End lists

def alea():
    f = random.randint(1,10)  # genera un numero aleatorio entre 1 y 10
    return f

def comparativo(alea, numero):
    if (alea > numero):
        print(Mayor[IdiomaSelec])
    else:
        print(Menor[IdiomaSelec])
    return

enigma = alea(); numero=0 # enigma: numero aleatorio, numero: ingreso del usuario.
ES = 0; PT = 1; EN = 2 # Constantes que representan idiomas. Comienzan en 0 para no dar error de subíndice.

def elegir_idioma():
    print ("\n\nElija un idioma / Escolha um idioma / Choose a language:")
    print ("\n\n1 - Español.")
    print ("2 - Português.")
    print ("3 - English.")
    print ("\n[1-3]? "),
    idioma=int(input()) # input entra string, así que lo convierto en entero por las dudas
    if idioma == 1:   
        print("** Español **")
        return ES
    elif idioma == 2: 
        print("** Português **")
        return PT
    elif idioma == 3: 
        print("** English **")
        return EN
    else: 
        print ("** Error **")
        exit()

IdiomaSelec = elegir_idioma()
while numero != enigma:
    numero = input(ElijNum[IdiomaSelec]) # Utiliza IdiomaSelec como subíndice de una lista de mensajes
    if numero != enigma:
        print (EseNoes[IdiomaSelec])
        comparativo(enigma, numero)
print (Final[IdiomaSelec])
print (enigma)
