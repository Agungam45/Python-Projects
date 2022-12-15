import random

#List of sayings
sayings = ['Today will be a wonderful day!',
    'You are going to realize your dreams!',
    'Soon your ideas will be appreciated by others!',
    'Doors are opening because of your hard work!',
    'Your dreams are about to come true.']


def rand_quote_func(list):
    rand_idx = random.randrange(len(list))
    rand_quote = list[rand_idx]
    return  print("Your saying for today is - /n ", rand_quote)

count_sayings = 5

cont = True
# enter into a loop while the user wants to continue to play
while cont == True:
    user_response = int(input("Please select a number 1-5: "))
    if user_response <= 5 and user_response >= 1:
        rand_quote_func(sayings)
    cont = input('Would you like another inspirational saying? (y/n) ').lower()
    if cont == 'y':
        cont = True
    elif cont == 'n':
        cont = False
    else:
        print('not a valid response - please re-enter')


        print('\n')    

#print final message as the game play ends.
print('Thank you for playing, please come again.')
