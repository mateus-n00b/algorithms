#!/usr/bin/python
'''
Este e um programa de adivinha.
Para iniciar o jogo voce deve pensar em um numero entre 1 e 1000.
Este programa utiliza busca binaria para descobrir o numero de uma forma mais rapida.

Mateus, Setembro 2016

Versao 1.0

Licenca GPL
'''
import os,sys,time

print '''\nEste e um programa tenta adivinhar um numero que voce pensou.
Pense em um numero entre 0 e 1000...\n
Eu descobrirei em no maximo 9 tentativas!! AHAHAH
'''
time.sleep(4)
VAR = []

for x in range(1000):
    VAR += [x]

def magic(array):
    max = len(array)    
    min = 0
    guess = (max+min)/2 
        
    rep = ''
    while(max >= min):        
        rep = raw_input("Voce pensou em %d? (sim/(ma)ior/(me)nor) " % (guess))            
        if rep == 'ma':            
            min = guess + 1            
        elif rep == 'me':
            max = guess-1
        else:
            print "Eu nao sou linear!\nObserve o numero de tentativas!"
            sys.exit()
        
        guess = (max+min)/2

magic(VAR)        
