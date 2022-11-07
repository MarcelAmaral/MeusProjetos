'''

!!! OUTROS EXERCÍCIOS !!!

'''

----------------------------------------

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
#print('A soma entre',n1,'e',n2,'vale',s)
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
----------------------------------------

n = input('digite algo')
print('numerico',n.isnumeric())
print('Alfa numerico',n.isalnum())
print('Letra',n.isalpha())
print('Maiusculo',n.isupper())
print('decimal',n.isdecimal())
----------------------------------------

n1 = int(input('Digite em que ano nós estamos,no formato aaaa'))
n2 = int(input('Digite o ano do seu nascimento,no formato aaaa'))
s = n1 - n2
print('Fazendo a subtração das datas digitadas:{0}-{1}, você tem {2}anos.'.format(n1, n2, s))
----------------------------------------

n1 = int(input('Digite um número'))
print(n1-1,n1,n1+1)

n2 = int(input('Digite um número: '))
print('O dobro do número é: ',n2*2)
print('O triplo do número é: ',n2*3)
print('A raiz quadrada do número é: ',n2**(1/2))

aluno = str(input('Digite o nome do Aluno: '))
nota1 = float(input('Digite a primeira nota do aluno'))
nota2 = float(input('Digite a segunda nota do aluno'))
media = (nota1 + nota2)/2
print('O aluno,',aluno,' tem as notas:',nota1,'e',nota2,'e a sua média é:',media,)


### MUNDO 1 - TRATANDO DADOS E FAZENDO CONTAS ###

'''#5 - NÚMERO ANTECESSOR,ELE E SUCESSOR - ***(3 FORMAS DE FAZER)***'''

n = int(input('Digite um número'))
print(n-1,n,n+1)

ou

n = int(input('Digite um número'))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

ou

n = int(input('Digite um número'))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
------------------------------

'''#6 - NÚMERO DOBRO TRIPLO E RAIZ QUADRADA'''

n2 = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
-------------------------------

'''#7 - NOTAS ALUNO E MÉDIA - MÉDIA ARITMÉTRICA'''

aluno = str(input('Digite o nome do Aluno: '))
nota1 = float(input('Digite a primeira nota do aluno'))
nota2 = float(input('Digite a segunda nota do aluno'))
media = (nota1 + nota2)/2
print('O aluno,',aluno,' tem as notas:',nota1,'e',nota2,'e a sua média é:',media,)

ou

print('A media entre {} e {} é igual a {}'.format(n1, n2, media))
--------------------------------

'''#8 - CONVERSÃO 3 METROS - CONVERSOR DE MEDIDAS'''

medida = float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))
---------------------------------

'''#9 - TABUADA'''

n = int(input('Digite um número para mostrar a tabuada dele'))

print('Valor de',n,'x 0=',n*0)
print('Valor de',n,'x 1=',n*1)
print('Valor de',n,'x 2=',n*2)
print('Valor de',n,'x 3=',n*3)
print('Valor de',n,'x 4=',n*4)
print('Valor de',n,'x 5=',n*5)
print('Valor de',n,'x 6=',n*6)
print('Valor de',n,'x 7=',n*7)
print('Valor de',n,'x 8=',n*8)
print('Valor de',n,'x 9=',n*9)
print('Valor de',n,'x 10=',n*10)

ou

n = int(input('Digite um número para ver sua tabuada'))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
---------------------------------

'''#10 - CAMBIO REIAS DOLLAR CONVERSOR DE MOEDAS'''

nome = str(input('Qual é o nome do comprador?'))
dinheiroreal = float(input('Quantos reais tem disponível para o cambio?'))
print('Após o cambio o',nome,'terá US',dinheiroreal*3.27)

ou

real = float(input('Quanto dinheiro você tem na carteira?'))
dolar = real / 3.27
print('Com R${:2f} você pode comprar US${:2f}',format(real, dolar))
---------------------------------

'''#11 - PINTURA'''

larparede = float(input('Qual é a largura da parede:'))
altparede = float(input('Qual é a altura da parede:'))
area = larparede*altparede
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(larparede, altparede, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta,'.format(tinta))
---------------------------------

'''#12 - VALOR PRODUTO CALCULANDO DESCONTO'''

preco = float(input('Qual é o valor do produto? R$:'))
novopreco = preco - (preco * 5 / 100)
print('O produto que custava {}, na promoção com desconto de 5% vai custar R${}'.format(preco, novopreco))
---------------------------------

'''#13 - SALÁRIO FUNCIONÁRIO AUMENTO DE 15%'''

salario = float(input('Digite o salário do funcionário'))
salarionovo = salario + (salario * 15 /100)
print('A salário inicial do funcionário era R$: {0}, com o aumento de 15%,\n passou a ser R$:{1}'.format(salario, salarionovo))
----------------------------------

'''#14 - CONVERSOR DE TEMPERATURA °C PARA °F'''

c = float(input('Informe a temperatura em °C'))
f = ((9 * c) / 5 ) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
-----------------------------------

'''#15 - ALUGUEL DE CARRO'''

dias = int(input('Quantos dias alugados?'))
rodado = int(input('Quantos Km rodados?'))
gastos = (dias * 60) + (rodado * 0.15)
print('O custo total de gastos é de R$:{}'.format(gastos))
-----------------------------------

### MUNDO 1 - USANDO MÓDULOS DO PYTHON ###

'''#16 - PROGRAMA QUE LEIA UM NÚMERO REAL, PELO TECLADO E MOSTRE NA TELA A PORÇÃO INTEIRA 
EX.: 6.127 = 6'''

n = float(input('Digite um número real'))
print('O número real é: {} e a sua porção inteira é: {} '.format(n, math.trunc(n)))

ou

from ctypes.wintypes import PULARGE_INTEGER
from lib2to3.pgen2.pgen import PgenGrammar
from math import trunc
from xmlrpc.client import PARSE_ERROR
n = float(input('Digite um número real'))
print('O número real é: {} e a sua porção inteira é: {} '.format(n, trunc(n)))

ou

n = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))
------------------------------

'''#17 - LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADEJACENTE DE UM TRIANGULO RETANGULO, 
CALCULE E MOSTRE A HIPOTENUSA'''

co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

ou

import math
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

ou

from math import hypot
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
-------------------------------------

'''#18 - LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO COSSENO E TANGENTE DESSE ÂNGULO'''

import math
angulo = float(input('Digite o ângulo que você deseja'))
sen = math.sin(math.radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, tan))

ou

from math import sen, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja'))
sen = sin(radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, sen))
cos = cos(radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, tan))
-------------------------------------------

'''#19 - UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. 
FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO'''

import random
n1 = str(input('nome do aluno primeiro aluno'))
n2 = str(input('nome do aluno segundo aluno'))
n3 = str(input('nome do aluno terceiro aluno'))
n4 = str(input('nome do aluno quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

ou

from random import choice
n1 = str(input('nome do aluno primeiro aluno'))
n2 = str(input('nome do aluno segundo aluno'))
n3 = str(input('nome do aluno terceiro aluno'))
n4 = str(input('nome do aluno quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
------------------------------------------

'''#20 - O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE 
TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.'''

from random import shuffle
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A sequência de apresentação será:')
print(lista)

ou

import random
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A sequência de apresentação será:')
print(lista)
-------------------------------------------

'''#21 - FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3'''

import pygame
pygame.init()
pygame.mixer.music.load('nomearquivo.mp3')#o arquivo tem q estar na pasta
pygame.mixer.music.play()
pygame.event.wait()
-------------------------------------------

'''#22 - crie um programa que leia o nome completo de uma pessoa e mostre'''

#1 o nome com todas as letras maiusculas
nome = str(input('Digite o nome completo de uma pessoa:'))
print('analisando seu nome...')'
print('Seu nome em maiúscula é {}'.format(nome.upper()))

#2 o nome com todas minusculas
nome = str(input('Digite o nome completo de uma pessoa:'))
print('analisando seu nome...')
print('Seu nome em minúscula é {}'.format(nome.lower()))

#3 quantas letras ao todo(sem considerar espaços)
nome = str(input('Digite o nome completo de uma pessoa:')).strip()
print('analisando seu nome...')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#4 quantas letras tem o primeiro nome
nome = str(input('Digite o nome completo de uma pessoa:'))
dividido = nome.split()
print(dividido)
separa = nome.split()
print('Seu primeiro é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

ou

nome = str(input('Digite o nome completo de uma pessoa:'))
print('analisando seu nome...')
print('Seu primeiro nome tem {} letra'.format(nome.find(' ')))
--------------------------

'''#23 - faça um programa que leia um numero de 0 a 9999 e mostre na tela cada 
um dos digitos separados tentar fazer com strtentar matemáticamente
undade:4
dezena:3
centena:8
milhar:1'''

num = int(input('Digite o número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
----------------------------------------------

'''#24 - crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"'''

cidade = str(input('Digite o nome de uma cidade')).strip()
print(cidade[:5].upper() == 'SANTO')
---------------------------

'''#25 - crie um programa que leia o nome de uma pessoa e diga se ela tem ''silva'' no nome'''

nome = str(input('Qual é o seu nome completo')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
----------------------------

'''#26 - Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra ''A'''''

frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))
-----------------------------

'''#27 - faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
ex.: Ana Maria de Souza
primeiro: Ana
segundo: Souza'''

n = str(input('Digite um nome completo:')).strip()
nome = n.split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O segundo nome é: {}'.format(nome[len(nome)-1]))
--------------------------

#Aula 10 - Ex1.: Carro velho e novo

tempo = int(input('Quantos anos tem o seu carro?'))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')

ou

tempo = int(input('Quantos anos tem o seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')
--------------------------

#Aula 10 - Condições Simples, Compostas e Simplificadas
# Ex2.: Nota aluno

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('SUA MÉDIA FOI BOA! PARABÉNS!')
else:
    print('ESTUDE MAIS!')

ou

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')
--------------------------

### MUNDO 1 - CONDIÇÕES EM PYTHON(IF , ELSE) ###

'''#28 - faça um programa que faça o computador pensar em um número inteiro entre 0 e 5 
e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador. 
O programa escreve na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "Pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Errou! Eu pensei no número {} e não no {}!'.format(computador, jogador))
--------------------------

'''#29 - escreva um programa que leia a velocidade de um carro
1 se ele ultrapassar 80 km/h,mostre uma mensagem dizendo que el'e foi multado.
2 A multa vai custar R$7.00 por cada km acima do limite'''

velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Vôce excedeu o limite permitido que é de 80Km/h')
    multa  = (velocidade-80) * 7
    print('Você deve pagar uma multa de R$: {:.2f}'.format(multa)) 
print('Tenha um bom dia! Diriga com segurança!')
--------------------------

'''#30 - crie um programa que leia um número inteiro qualquer e escreva se ele é par ou impar'''

numero = int(input('Me diga um número qualquer?'))
resultado = numero % 2
print('O resultado foi {}'.format(resultado))
if resultado == 0:

    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
--------------------------

'''#31 - desenvolva um programa que pergunte a distância de uma viagem em km.
1 calcule o preço do passagem, cobrando R$0.50 por km para viagens de até 200km
2 R$ 0.45 para viagens mais longas.'''

distancia = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f} Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem para esse trecho será de: R$ {:.2f}'.format(preco))

ou

distancia = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f} Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia *0.45
print('O preço da passagem para esse trecho será de: R$ {:.2f}'.format(preco))
--------------------------

'''#32 - faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
-------

'''#32 extra - analise se o ano atual é bissexto'''

from datetime import date
ano = int(input('Que ano quer analisar?Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
--------------------------

'''#33 - faça um programa que leia 3 números e mostre qual é o número menor e maior'''

a = int(input('Digite o primeiro numero:'))
b = int(input('Digite o segundo numero:'))
c = int(input('Digite o terceiro numero:'))

#Verificando quem é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
--------------------------

'''#34 - escreva um programa que pergunte o salário de um funcionário 
e calcule o valor do seu aumento.
1 para salários superiores a R$1250.00 calcule um aumento de 10%
2 para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Digite o salário do funcionário:'))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
print('O salário anterior era de R$: {:.2f} e com o aumento, passou a ser de R$: {:.2f}'.format(salario, novosalario))
--------------------------

'''#35 - desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se eles podem ou não formar um triãngulo.'''

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
--------------------------

### MUNDO 1 - Estilos de textos e cores ###

'''  Ex:. \031[0;33;44m - É o padrão para formatar as cores  '''

# Style de letra
# 0 - Nome
# 1 - Bold(normal)
# 4 - Underline(sublinhada)
# 7 - Negative(invertida)

# Text - Cor da letra
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - magenta
# 36 - ciano
# 37 - cinza

# Back - Cor de fundo
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - magenta
# 46 - iano
# 47 - cinza  

### MUNDO 2 - CONDIÇÕES ANINHADAS  ###

# AULA 12 #

'''#36 - Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra 
de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual é o valor da casa?'))
salario = float(input('Salário comprador?'))
anos = float(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario - (salario * 30 /100) 
print('Para pagar uma casa de R$:{:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')
-----------------------------------

'''#37 - escreva um programa em Python que leia um número inteiro qualquer e peça 
para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal.'''

num = int(input('Digite eum número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Digite a opção'))
if opcao == 1:
    print('{} convertido para Binário é igual {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente')
-----------------------------------

'''#38 - escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais'''

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número'))
if num1 > num2:
    print('O primeiro número: {0} é maior que o segundo: {1}'.format(num1, num2))
elif num2 > num1:
    print('O segundo número:{1} é maior que o primeiro:{0}'.format(num1, num2))
else:
    print('Os dois número: {} e {} são iguais:'.format(num1, num2))
-----------------------------------

'''#39 - faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a 
sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou 
se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou 
que passou do prazo.'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em: {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em: {}'.format(ano))
-----------------------------------

'''#40 - crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma 
mensagemno final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Parabéns! Suas notas foram {:.1f} e {:.1f}\nVocê está APROVADO com média {:.1f}.'.format(nota1, nota2, media))
elif media >= 5 and media < 7:
    print('Suas notas foram {:.1f} e {:.1f}.\nSua média foi {:.1f} e você está em recuperação!'.format(nota1, nota2, media))
elif media < 5:
    print('Que pena! Suas notas foram {:.1f} e {:.1f}.\n Sua média foi {:.1f} e você está REPROVADO.'.format(nota1, nota2, media))
-----------------------------------

'''#41 - a Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento'))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('A sua categoria é: MIRIM'.format(idade))
elif idade > 9 and idade < 15:
    print('A sua categoria é: INFANTIL'.format(idade))
elif idade > 14 and idade < 19:
    print('A sua categoria é: JÚNIOR'.format(idade))
elif idade > 19 and idade < 25:
    print('A sua categoria é: SÊNIOR'.format(idade))
elif idade >= 25:
    print('A sua categoria é: MASTER'.format(idade))

ou

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento'))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('A sua categoria é: MIRIM'.format(idade))
elif idade <= 14:
    print('A sua categoria é: INFANTIL'.format(idade))
elif idade <= 19:
    print('A sua categoria é: JÚNIOR'.format(idade))
elif idade <= 25:
    print('A sua categoria é: SÊNIOR'.format(idade))
else:
    print('A sua categoria é: MASTER'.format(idade))
-----------------------------------

'''#42 - refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
-----------------------------------

'''#43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice
de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: 
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite o peso:'))
altura = float(input('Digite a altura'))
imc = peso / ( altura ** 2)
print('O IMC dessa pessoa é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Seu peso é: {:.1f} Kg, sua altura é: {:.1f}. ABAIXO DO PESO'.format(peso, altura, imc))
elif 18.5 <= imc = 25:
    print('Seu peso é: {:.1f} Kg, sua altura é: {:.1f}. PESO IDEAL!'.format(peso, altura, imc))
elif 25 <= imc < 30:
    print('Seu peso é: {:.1f} Kg, sua altura é: {:.1f}. PESO SOBREPESO!'.format(peso, altura, imc))
elif 30 <= imc < 40:
    print('Seu peso é: {:.1f} Kg, sua altura é: {:.1f}. OBESIDADE!'.format(peso, altura, imc))
elif imc >= 40:
    print('Seu peso é: {:.1f} Kg, sua altura é: {:.1f}. OBESIDADE MÓRBIDA!'.format(peso,altura, imc))
-----------------------------------

'''#44 Elabore um programa que calcule o valor a ser pago por um produto, considerando o 
seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS MARCEL '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] à vista no cartão
[3] até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente\033[m')
print('Sua compra de R$ {:.2f} vai custar RS {:.2f} no final.'.format(preco, total))
---------------------------------

'''#45 - crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-'* 12)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=-'* 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: 
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
---------------------------------

# Mundo 2 - EXEMPLOS DE FOR

for c in range(1,6):
    print('Oi')
print('FIM')
Mensagem: Oi, Oi, Oi, Oi, Oi, FIM

for c in range(0,6):
    print(c)
print('FIM')
Mensagem: 0, 1, 2, 3, 4, 5, FIM

for c in range(6, 0, -1):
    print(c)
print('FIM')
Mensagem: 6, 5, 4, 3, 2, 1, FIM

for c in range(0, 7, 2):
    print(c)
print('FIM')
Mensagem: 0, 2, 4, 6, FIM

n = int(input('Digite um número: 3 '))
for c in range(0,n+1):
    print(c)
print('FIM')
Mensagem: 0, 1, 2, 3, FIM

i = int(input('Início: 1 '))
f = int(input('Fim: 5 '))
p = int(input('Passo: 1 '))
for c in range(i, f+1, p)
    print(c)
print('FIM')
Mensagem: 1, 2, 3, 4, 5, FIM

for c in range(0,3):
    n = int(input('Digite um valor:'))
print('FIM')
Mensagem:
Digite um valor:
Digite um valor:
Digite um valor:

s = 0 
for c in range(0,4):
    n = int(input('Digite um valor:'))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
Mensagem:
Digite um valor: 4
Digite um valor: 2
Digite um valor: 3
Digite um valor: 1
O somatório de todos os valores foi 10
---------------------------------

'''#46 - faça um programa que mostre na tela uma contagem regressiva para o estouro 
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
    print('BUM! BUM! BUMMM!')
print('FIM')
---------------------------------

'''#47 - crie um programa que mostre na tela todos os números pares que estão no intervalo enre 1 e 50.'''

for num in range(0, 51, 2):
    print(num)
print('FIM')

ou

for n in range(1,51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')

ou

for n in range(2, 51, 2):
    print(n, end=' ')
print('FIM')

----------------------------------

'''#48 - faça um programa que calcule a soma entre todos os números ímpares que são 
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + c
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

ou 

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
----------------------------------

'''#49 - refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Digite um número para fazer a tabuada:'))
for c in range(0, 11):
        print('{} x {:2} = {}'.format(num, c, num*c))
----------------------------------

'''#50 - desenvolva um programa que leia seis números inteiros e mostre apenas 
a soma daqueles que forem pares. Se o valor digitado for ímpar. Desconsidere-o.'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor '.format(c)))
    if num % 2 == 0:
        soma += num 
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
----------------------------------

'''#51 - faça um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.'''

print('=' *30)
print('     10 TERMOS DE UMA PA     ')
print('=' *30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1 ) * razao
for c in range(primeiro, decimo + razao, razao):
        print('{}'.format(c), end=' >> ')
print('ACABOU')
----------------------------------

'''#52 - faça em programa que leia um numero inteiro e diga se ele é ou não um numero primo.'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
        print('E por isso ele é PRIMO!')
else:
        print('E por isso ele NÃO É PRIMO')
----------------------------------

'''#53 - crie um programa que leia uma frase qualquer e diga se ela é um políndromo, 
desconsiderando os espaços.
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)- 1, -1, -1):
        inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
        print('Temos um palíndromo!')
else:
        print('A frase digitada não é um palíndromo!')

ou

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''.join[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
        print('Temos um palíndromo!')
else:
        print('A frase digitada não é um palíndromo!')
----------------------------------

'''#54 - crie um programa que o ano de nascimento de sete pessoas. No final mostre quantas 
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year 
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que a {}ª pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
----------------------------------

'''#55 - faça um programa que leia peso de cinco pessoas. No final, mostre qual foi o 
maior e menor peso lidos.'''

maior = 0
menor = 0
for pess in range(1,6):
    peso = float(input('Peso da {}ª pessoa:'.format(pess)))
if pess == 1:
    maior = peso
    menor = peso
else:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
----------------------------------

'''#56 - desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre:
a média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres tem menos de 20 anos'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('---------- {}ª PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
----------------------------

'''#57 - faça um programa que leia sexo de uma pessoa, mas só aceite os valores 
'M' ou 'F'. Caso esteja errado. Peça a digitação novamente até ter um valor correto'''

sexo = str(input('Informe sexo: [M/F}')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print(f'Sexo {sexo} formatado com sucesso!')
----------------------------

'''#58 - melhore o jogo do desafio 28 onde o computador vai ''pensar'' em um número 
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. mostrando no
final quantos palpites foram necessários para vencer'''

from random import randint
computador = randint(0,10) # Faz o computador "Pensar"
print('Vou pensar em um número entre 0 e 10. Tente adinhar...')
acertou = 0
palpites = 0
while not acertou:
jogador = int(input('Qual é o seu palpite?'))
palpites += 1
if jogador == computador:
    acertou = True
else:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
print(f'PARABÉNS! Você conseguiu me vencer com {palpites} tentativas!')
----------------------------

'''#59 - crie um programa que leia dois valores e mostre um menu na tela: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
seu programa deverá realizar a operação solicitada em cada caso'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segunda valor: '))

opcao = 0
while opcao != 5:
print('''        [1] Somar
[2] Multiplicar
[3] Maior 
[4] Novos números
[5] Sair do programa
''')
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    soma = n1 + n2
    print(f'A soma entre {n1} + {n2} é de {soma}')
elif opcao == 2:
    produto = n1 * n2
    print(f'O resultado entre {n1} x {n2} é de {produto}')
elif opcao == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2 
        print(f'Entre os números {n1} e {n2} o maior número é {maior}')
elif opcao == 4:
    print('Informe os novos número novamente...')
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
elif opcao == 5:
    print('Finalizando...')
    sleep(3)       
else:
    print('Opção inválida!. Tente novamente!')
print('FIM DO PROGRAMA')
----------------------------

'''#60 - faça um programa que leia um número qualquer e mostre o seu fatorial
Ex: 5!=5x4x3x2x1=120'''

from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

ou

n = int(input('Digite um número para calcular o fatorial: '))
c = n 
f = 1
print('Claculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
------------------------------

'''#61 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando 
os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA')
print('-'* 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} >> '.format(termo) , end='')
    termo += razao 
    cont += 1
print('FIM')
----------------------------

'''#62 - melhore o desafio 61. perguntando para o usuário se ele quer mostrar mais 
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos'''

print('Gerador de PA')
print('-'* 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >> '.format(termo) , end='')
        termo += razao 
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Prograssão finalizada com {} termos mostrados.'.format(total))
--------------------------------

'''#63 - escreva um programa que leia um número n inteiro qualquer e mostre na tela os 
n primeiros elementos de uma sequência de Fibonacci.
Ex.: 0 >> 1 >> 1 >> 2 >> 3 >> 5 >> 8''' 

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} >> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' >> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' >> FIM')
--------------------------------

'''#64 - crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre 
quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag = não vale como dado)'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))
---------------------------------

'''#65 - crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e menor valor valores lidos. O programa 
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resp = 'S'
soma = quant = media = maior = menor =0 
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor {}'.format(maior, menor))
print('FIM')
---------------------------------

'''#66 - Crie um programa que leia números inteiros pelo teclado. O programa 
só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas 
(desconsiderando o flag).'''

cont = soma = 0 
while True:
    num = int(input('Digite um valor (999 para parar): ')) 
    if num == 999:
        break
    cont += 1
    soma += num 
print(f'Foram digitados {cont} números e a soma entre eles é de {soma}')
print('Fim do programa')
---------------------------------

'''#67 - Faça um programa que mostre a tabuada de vários números, um de cada 
vez, para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO> Volte sempre!')
---------------------------------

'''#68 - Faça um programa que jogue par ou ímpar com o computador. O jogo só 
será interrompido quando o jogador perder, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
    else:
        print('Você Perdeu!')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
---------------------------------

'''#069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

tot18 = totH = totM20 =0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' ' 
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao Todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
---------------------------------

'''# 70 - Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto  
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} quecusta R${menor:.2f}')

ou 

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} quecusta R${menor:.2f}')
------------------------------

'''#71 - Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS '''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedúlas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco Cev! Tenha um bom dia!')
--------------------------------

'''#72 - Crie um programa que tenha uma dupla totalmente preenchida com uma contagem 
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'quatorze',
'quinze', 'dezesseis','dezessete', 'dezoito',
'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')

--------------------------------

'''73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Botafogo.'''

times = ('Palmeiras','Flamengo','Corinthians','Fluminense','Athletico-PR',
'Intenacional','Atlético','América-MG','Bragantino','Santos','São Paulo',
'Botafogo','Goiás','Ceará','Fortaleza','Cuiabá','Avai','Coritiba',
'Atlético-GO','Juventude')

print('-=' * 20)
print(f' Os 5 primeiros colocados do Brasileirão são:{times[0:5]}')
print('-=' * 20)
print(f' Os 4 últimos colocados do Brasileirão são:{times[-4:]}')
print('-=' * 20)
print(f' Listagem dos times em ordem alfabetica:{sorted(times)}')
print('-=' * 20)
print(f' O time do Botafogo está na {times.index("Botafogo")+1}ª posição')

--------------------------------
'''74: Crie um programa que vai gerar cinco números 
aleatórios e colocar em uma tupla. Depois disso, mostre a listagem 
de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10),
randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n O maior valor sorteado foi: {max(numeros)}')
print(f' O menor valor sorteado foi: {min(numeros)}')
--------------------------------

'''75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os 
em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

núm = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(f' Você digitou os valores {núm}')
print(f' O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f' O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
--------------------------------

'''76: Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
os dados em forma tabular.'''

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 4.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
--------------------------------

'''77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('APRENDE', 'PROGRAMAR','LIGUAGUEM','PYTHON','CURSO',
            'GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO',
            'PROGRAMADOR','FUTURO')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ') 
--------------------------------

'''78 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores: {listanum}')

#Maior
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...',end='')

print()

#Menor
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
--------------------------------

'''79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os 
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.'''

números = []

while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')
--------------------------------

'''80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em 
uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1 
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
--------------------------------
'''81: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    resposta = str(input('deseja contiunuar: [S/N]')).upper().strip()
    if resposta in 'Nn':
        break
print(f'Os números digitados foram: {valores}')
print(f'Foram digitados {len(valores)} números.')
valores.sort(reverse=True)
print(f'Os valores em ordem são: {valores}')
if 5 in valores:
    print(f'O número 5 está na lista!')
else:
    print(f'O número 5 não está na lista!')
print('FIM')
--------------------------------
'''82: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if resposta in 'Nn':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'Os números digitados foram: {num}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números impares digitados foram:{impares}')
--------------------------------
'''83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha pop()
        else: 
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
--------------------------------
'''84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

temp = []
prin = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso [KG]: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prin.append(temp[:])
    temp.clear()
    resposta = str(input('Deseja continuar [S/N]: '))
    if resposta in 'Nn':
        break
print('-=' * 25)
print(f'Foram cadastradas {len(prin)} pessoas')
print(f'O maior peso foi: {mai}Kg', end='')
for p in prin:
    if p[1] == mai:
        print(f' [{p[0]}] ', end='')
print()
print(f'O menor peso foi: {men}Kg', end='')
for p in prin:
    if p[1] == men:
        print(f' [{p[0]}]' ,end='')
print()
--------------------------------
'''85: Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

num = [[],[]]
valor = 0
for c in range(0,7):
    valor = int(input(f'Digite o {c}o, valor: '))
    if valor % == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
--------------------------------
'''86 Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0 , 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
--------------------------------
'''87 Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0 , 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:
            spar+= matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
--------------------------------
'''88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep
lista = []
jogos = []
print('-=' * 20)
print('{: ^40}'.format(' JOGO DA MEGA SENA '))
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print( f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< Boa Sorte! >', '-=' * 5)
--------------------------------

'''89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
de cada aluno individualmente.'''

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
--------------------------------
'''90: Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5<= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇãO'
else:
    aluno['situação'] = 'REPROVADO'
print(aluno)
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
--------------------------------
'''91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
aleatórios. Guarde esses resultados em um dicionário em Python. No final, 
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = ()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
--------------------------------
'''92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário 
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com 
quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
--------------------------------
'''93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O Campo {k} tem o valor {v}')
print('-=' * 30)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
--------------------------------
'''94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
essoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas 
foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade 
acima da média'''

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]} ',end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
--------------------------------
'''95: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um 
sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0] 
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO" Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'       No jogo{i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
--------------------------------
'''96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


# Programa principal
print('Controle de Terreno')
print('-' * 30)
l = float(input('LARGURA (m): '))
c  = float(input('COMPRIMENTO (m): '))
area(l,c)
--------------------------------
'''97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer 
como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Marcel Amaral')
escreva('Curso de Python no Youtube')
escreva('CeV')
--------------------------------
'''98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:   
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1 
    print('-' *20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: ')) 
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador = (ini, fim, pas)
--------------------------------
'''99: Faça um programa que tenha uma função chamada maior(), que receba vários 
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores 
e dizer qual deles é o maior.'''

def maior(* num):
    cont = maior = 0
    print('-' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ' end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Programa principal
maior(2, 9 , 4, 8, 1)
maior(1, 5, 9)
maior(9, 7 ,6 ,3, 1)
maior(8, 4)
maior(5, 2)
--------------------------------
'''100: Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
pares sorteados pela função anterior.'''

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
--------------------------------
'''101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o 
ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto Obrigatório.'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
--------------------------------
'''102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro 
que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando
se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    : param n: O número a ser calculado
    : param show: (opcional) Mostrar ou não a conta.
    : return: O valor do fatorial de um número n.
    """
    f = 1 
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c 
    return f

# Programa Principal
print(fatorial(5, show=True))
help(fatorial)
--------------------------------
'''103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros 
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
--------------------------------
'''104: Crie um programa que tenha a função leiaInt(), que vai funcionar de 
forma semelhante ‘a função input() do Python, só que fazendo a validação para 
aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
--------------------------------
'''105: Faça um programa que tenha uma função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas 
– A maior nota 
– A menor nota 
– A média da turma
– A situação (opcional)'''


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return?: dicionário com várias informações sobre a situação da turma.
    """  
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
--------------------------------
'''106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar 
o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se 
encerrará. Importante: use cores.'''
from time import sleep


c = ('\033[m',       # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m', # 6 - branco
    );

def ajuda(com):
    título(f'Acessando o manuel do comando \'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep (2)

def título(msg, cor=0):     
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
    
#Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
------------------------------------------------
'''Exercicio 107 até 110 está na pasta raiz'''
------------------------------------------------
'''Exercicio 111 até 112 não foram feitos'''
------------------------------------------------
'''113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também 
uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi: {n1} e o real foi: {n2}')

--------------------------------
'''114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http:www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')
--------------------------------

'''Exercicio 115 está na pasta raiz'''




