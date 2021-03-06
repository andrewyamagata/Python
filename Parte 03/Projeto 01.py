#Tuplas, variável composta entre parenteses, são imutáveis
lanche = ('hambúrger', 'suco', 'pizza', 'pudim')
print(lanche) #todos os itens
print(lanche[3]) #item na posição 4 (item 3)
print(lanche[-1])#de trás p frente
print(lanche[:2]) #vai do 0 até o 1, ignorando o ultimo elemente, neste caso o 2
print(lanche[1:3])#vai do 1 até o 2 , ignorando o ultimo elemento, neste caso o 3
print(len(lanche))
print('-'*30)
for c in lanche:
    print(f'Como {c}')
print('-'*30)
for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')
print('-'*30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-'*30)
print(sorted(lanche)) #sorted, deixar em ordem
print(lanche) #deixar na ordem natural
print('-'*30)
a = (2,5,4)
b = (5,8,1,2)
d = a + b
print(d)
print(d.count(5)) #quantas vezes o 5 aparece em d
print(d.index(5)) #em que posição o 5 está, mostra o primeiro 5 que aparece