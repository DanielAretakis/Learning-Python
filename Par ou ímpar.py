from random import randint

c = 0
while True:
    n = int(input('Digite um valor: '))
    e = ' '
    while e not in 'PI':
        e = input('Você quer par ou ímpar?[P/I] ').upper().strip()[0]
    pc = randint(1, 10)
    if (n+pc) % 2 == 0:
        r = 'DEU PAR'
    if (n+pc) % 2 != 0:
        r = 'DEU ÍMPAR'
    if e == 'P':
        print(f'Você jogou {n} e eu {pc}, total de {n + pc}, {r}')
        if (n+pc) % 2 == 0:
            print('Você venceu! Vamos denovo!')
            c += 1
        if (n+pc) % 2 != 0:
            break
    if e == 'I':
        print(f'Você jogou {n} e eu {pc}, total de {n+pc}, {r}')
        if (n+pc) % 2 != 0:
            print('Você venceu! Vamos denovo!')
            c += 1
        if (n+pc) % 2 == 0:
            break
print(f'GAME OVER! você venceu {c} vezes')
