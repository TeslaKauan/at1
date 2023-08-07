

from random import randint
def numero_aleatorio():
  aleatorio=randint(1,10)
  chute=0
  while aleatorio != chute:
    chute=int(input("Digite um valor de 1 a 10: "))
    if (aleatorio == chute):
      print("Parabéns, você é muito bom!")
    else:
      print("Errou, otário.")
numero_aleatorio()