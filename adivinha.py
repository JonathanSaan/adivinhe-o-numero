from time import sleep
from random import randint
import os, sys

clf = 'clear'
if os.name == 'posix': clf = 'clear'
if os.name == 'nt':clf = 'cis'
clear = lambda: os.system(clf)

def jogo():
	print('#'*20)
	print('   \033[33m  HYOKOJIRO \033[m')
	print('#'*20)
	tentativas = 0
	while True:
		tentativas += 1
		try:
			nums = randint(0, 10)
			print('\nChute o numero que estou pensando de 0 a 10.')
			resposta = int(input('resposta: '))
			print('='*50)
		except:
			print('\033[2;31mERRO! digite apenas numeros inteiros. \033[m')
		else:	
			if resposta == nums:
				print(f'\033[32mparabens!\033[m você venceu com {tentativas} tentativas!')
				while True:
					continuar = str(input('quer continuar?: [S/N] ')).lower()[0]
				
					if continuar == 's':
						print('\n\033[32;1m reiniciando...\033[m')
						sleep(1)
						clear()
						jogo()
						break
					
					elif continuar == 'n':
						print('\033[33mencerrando...\033[m')
						break
				break
			
			elif resposta < nums:
				print(f'\no numero que pensei é maior que {resposta},\033[31;1m tente novamente.\033[m')
				sleep(1)
			elif resposta > nums:
				print(f'\no numero que pensei é menor que {resposta}, \033[31;1mtente novamente.\033[m')
				sleep(1)
jogo()
