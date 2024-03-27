"""
- Build a Number guessing game, in which the user selects a range.
- Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
- Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
"""

import random

choice = 0
guess = -1
i = 0

range = {
    'a': '',
    'b': '',
} 

    
if __name__ == '__main__':
    
    while True:
        range['a'] = input('Enter the first number to define the range we are gonna play in: \n')
        
        if range['a'].isdigit() == False or int(range['a']) < 0:
            print('Please pick a positive number bigger than 0')
            continue
            
        else:
            pass
        
        
        while True:
            range['b'] = input('Enter the Second number to define the range we are gonna play in: \n')
        
            if range['b'].isdigit() == False or int(range['b']) < int(range['a']):
                print(f'Please pick a positive number bigger than {range["a"]}')
                
            else:
                break
        break
    
    choice = random.randrange(int(range['a']),int(range['b']))
    i = 0
    
    print("Let's start the game! Try and guess the number I have chosen\n")
    
    while True:
        i = i+1
        guess = input('Come on! Hit me with your best shot\n ')
        
        if int(guess) != int(choice):
            print(f'You almost had it! The number you picked was just a little bit {"Bigger" if int(guess) > int(choice) else "Smaller" } \n') 
            
        else:
            print(f'Congratulations! You have discovered the number I picked. It was the number {choice}')
            print(f'It only took you {i} attempts.')
            
            break