table = 'América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo'
opt = 0
while opt != 5:
    print('-='*15)
    opt = int(input('''[1] Top 5
[2] Last 4
[3] Alphabetic order
[4] A team specific position
[5] Close app
Choose an option: '''))
    print('-=' * 15)
    if opt == 1:
        for c in range(0, 5):
            print(f'Top {c+1}: {table[c]}')
    if opt == 2:
        for c in range(16, 20):
            print(f'Top {c+1}: {table[c]}')
    if opt == 3:
        print(sorted(table))
    if opt == 4:
        team = input('Which team do you want to see? ')
        print(f'{team} is at top {table.index(team) +1} in the championship')