#Jogo Par ou Ímpar
from random import randint
v = jogador = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o comupador {computador}. Total deu {total}')
    if tipo == 'P':
        if total % 2 ==0:
            print("Você ganhou!")
            v +=1
        else:
            print("Você Perdeu!")
            break
    if tipo == 'I':
        if total % 2 == 1:
            print("Você ganhou")
            v += 1
        else:
            print("Você Perdeu")
            break
print(f"Game over, você venceu {v} vezes")