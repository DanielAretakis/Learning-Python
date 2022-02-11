from random import choice
from time import sleep

list = ['rock', 'paper', 'scissor']
machine = choice(list)
print('''Let's play rock, paper, scissor?
At the end you type your choice :)''')
print('Rock')
sleep(0.5)
print('Paper')
sleep(0.5)
print('Scissor')
player = input(': ').strip().lower()

if player == machine:
    print("A draw, let's play again?")
elif player == 'rock' and player != machine:
    if machine == 'paper':
        print('I won!!')
    elif machine == 'scissor':
        print('You won!')
elif player == 'paper' and player != machine:
    if machine == 'scissor':
        print('I won!!')
    elif machine == 'rock':
        print('You won!')
elif player == 'scissor' and player != machine:
    if machine == 'rock':
        print('I won!!')
    elif machine == 'paper':
        print('You won!')
else:
    print(f'{player} is not rock, paper or scissor')
print(f'My choice: {machine}')