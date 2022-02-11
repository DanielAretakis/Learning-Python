from datetime import date

idade = int(input('Qual seu ano de nascimento? '))
atual = date.today()
ano = atual.year
if ano - idade <= 9:
    print('Você está na categoria MIRIM')
elif ano - idade <= 14:
    print('Você está na categoria INFANTIL')
elif ano - idade <= 19:
    print('Você está na categoria JUNIOR')
elif ano - idade == 20:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria MASTER')