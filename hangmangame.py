import random
hangman = ['''
    ----
    |   |
        |
        |
        |
        |
_________''','''
    ----
    |   |
    0   |
        |
        |
        |
_________''','''
    ----
    |   |
    0   |
    |   |
        |
        |
_________''','''
    ----
    |   |
    0   |
   -|   |
        |
        |
_________''','''
    ----
    |   |
    0   |
   -|-  |
        |
        |
_________''','''
    ----
    |   |
    0   |
   -|-  |
   /    |
        |
_________''','''
    ----
    |   |
    0   |
   -|-  |
   / \  |
        |
_________''']
words = 'say see she so some take tell than that their them then there these they thing think'.split()
def random_word(wordList):
    '''
    this funtion returns a random words for an already set up list.
    '''
    random_number = random.randint (0, len(words) - 1)
    return wordList[random_number]
def display_board(hangman, missed, correct, hidden_word):
    '''
    this funtion displays the board, the hangman. it also replaces the * with correctly guessed letters.
    '''
    print(hangman[len(missed)])
    print()
    print('guessed word:', end=' ')
    for letter in missed:
            print(letter, end=' ')
            print()
            blank = '*' * len(hidden_word)
            for i in range(len(hidden_word)):
                if hidden_word[i] in correct:
                    blank = blank[:i] + hidden_word[i] + blank[i+1:]
                    for letter in hidden_word:
                        print(letter, end=' ')
                        print()
def guesses(guessed):
    '''
    this function checks the letter the player entered and sees if it is correct or if the player already tried this letter.
    '''
    while True:
            print('enter a letter')
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print('your letter:')
            elif guess in guessed:
                print ('you have already tried this letter')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('please enter a valid letter')
            else:
                return guess
    
def play_again():
    '''
    this function returns true if the player wants to play again, and restars the game right away. and then it basically checks for the guesses and if the player lost or won.
    '''
    print('want to play again? ("yes" or "no")')
    return input()
    missed = ''
    correct = ''
    hidden_word = random_word(words)
    game_over = False
    while True:
        display_board (hangman, correct, missed, hidden_word)
        guess = guesses(missed + correct)
        if guess in hidden_word:
                correct = correct + guess
                won_game = True
                for i in range(len(hidden_word)):
                    if won_game[i] not in correct:
                        won_game = False
                        break
                if won_game:
                    print('good job')
                else:
                    missed = missed + guess
                    if len(missed) == len(hangman) - 1:
                        display_board(hangman, missed, correct, hidden_word)
                        won_game = True
                        if won_game:
                            if play_again():
                                missed = ''
                                correct = ''
                                won_game = False
                                hidden_word = random_word(words)
                            else:
                                break
def main():
    hidden_word = random_word(words)
    display_board(hangman, missed, correct, hidden_word)
    guess = guesses(guessed)
    new_game = hangman
    while True:
            print('here')
            hangman.run()
            if play_again():
                new_game = hangman
            else:
                break
            
if __name__ == "__main__":
    main()
    

