#Manipulando texto
#[] indica lista => começa em 0
#=>frase Curso em Video Python
frase = input('Digite:')
print(frase[9:13])
#[9:13] vai do 9 até o 12, o 13 não pega (ultimo valor nao pega), no caso = Vide
print(frase[9:21])
#[9:21] nao tem 21, vai até o ultimo, neste caso = Video Python
print(frase[9:21:2])
#[9:21:2] começa no 9 e para no 21, pulando de 2 em 2 = VdoPto

