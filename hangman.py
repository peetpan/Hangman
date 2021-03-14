from random_word import RandomWords

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
print('------------------------------------------------')
r = RandomWords()
chosen_word = r.get_random_word()

# print(f'Chosen word is {chosen_word}')

op = ['_'] * len(chosen_word)
life = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print('The word which you have to guess is \n', op)
while op != chosen_word:

    print(stages[life])

    guess = (input("Enter your guess: ")).lower()

    if guess in op:
        print(f'You have already guessed {guess}')

    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            # Right
            op[i] = chosen_word[i]

    if guess not in chosen_word:
        print(f'You have guessed {guess} but it is not present in the word. You lose a life')
        life -= 1

    if life == 0:
        print('\n' + stages[0] + '\n')
        print(f"You lose. The word was '{chosen_word}'. Try again")
        break

    print('------------------------------------------------')
    print(f'{op}\n lives left: {life}')

else:
    print("You won!. Well Played")
