#Número por extenso

lista = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco' , 'seis', 'sete' , 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:  '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
    print(f'Você digitou o número {lista[n]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Desejá continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break