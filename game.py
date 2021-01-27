import random

question = input('do you want to play with a second player or computer: ')

if question == 'second player':
    first_player = input('player 1:') 
    second_player = input('player 2:')
    if first_player == 'rock' and second_player == 'paper':
        print('second player wins')
    elif first_player == 'rock' and second_player == 'scissors':
        print('first player wins')
    elif first_player == 'paper' and second_player == 'scissors':
        print('second player wins')
    elif first_player and second_player =="paper" or first_player and second_player =="scissors" or first_player and second_player =="rock":
        print('draw')

    else:
        print('second player wins')

if question == "computer":
    options = ['rock', 'paper', 'scissors']
    answer = random.choice(options)
    first_player = input('player:')
    print (f'computer:{answer}')

    if first_player == 'rock' and answer == 'paper':
        print('computer wins')
    elif first_player == 'rock' and answer == 'scissors':
        print('player wins')
    elif first_player == 'paper' and answer == 'scissors':
        print('computer wins')
    elif first_player == None or answer == None:
        print('empty fields')
    elif first_player and answer =="paper" or first_player and answer =="scissors" or first_player and answer =="rock":
        print('draw')

    else:
        print('computer wins')
