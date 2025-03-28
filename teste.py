import os

def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite um valor válido!")

def calcularPisos(larguraSala, comprimentoSala, larguraPiso, tamanhoPiso):
    areaSala = larguraSala * comprimentoSala
    areaPiso = larguraPiso * tamanhoPiso
    qntPisos = (areaSala // areaPiso)
    return int(qntPisos)

def calcularPisosComPorcentual(margemErro, qntPisos):
    porcentual = (1 + margemErro/100)
    qntPisosComMargem = qntPisos * porcentual
    return int(qntPisosComMargem)

def chamaDeNovo():
    os.system('Cls')
    exe()

def exe():
    nome = input("Olá, bem vindo(a) a loja Salmazi. Qual sua graça? ")
    print(f"Prazer, {nome}. Você disse que gostaria de comprar alguns pisos,")
    os.system('Pause')

    print("mas que não sabe quantos comprar, certo? Isso é fácil,")
    os.system('Pause')

    print("por favor, me passe algumas informações...")
    os.system('Pause')
    os.system('Cls')

    larguraSala = verificadorEntrada("Digite a largura da sala: ")
    comprimentoSala = verificadorEntrada("Digite o comprimento da sala: ")
    larguraPiso = verificadorEntrada("Digite a largura do piso: ")
    tamanhoPiso = verificadorEntrada("Digite o tamanho do piso: ")
    margemErro = verificadorEntrada("Qual a porcentagem de pisos a mais que você gostaria de comprar: ")

    qntPisos = calcularPisos(larguraSala, comprimentoSala, larguraPiso, tamanhoPiso)
    qntPisosComMargem = calcularPisosComPorcentual(margemErro, qntPisos)

    print(f"Você vai precisar de {qntPisos} pisos, com margem de erro {qntPisosComMargem}.")

    if int(qntPisos) == 0:
        resposta = str(input("Vixi, a conta não bateu... Será que as medidas estão corretas? \n Deseja digitar novamente as medidas? [S] ou [N]: ")).upper()
        if resposta == 'S':
            chamaDeNovo()
    else:
        exit()

exe()
