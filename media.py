port = float( input("Nota de português: ") )
ing = float( input("Nota de inglês: ") )
info = float (input('Nota de informática: '))

media = (port + ing + info) / 3

print("A média desse estudante foi: ",media)


if media >= 70:
    print('O aluno foi Aprovado com a média ', media, )

else:
    print('O aluno foi Reprovado com a média ', media, )