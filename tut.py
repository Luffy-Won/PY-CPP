# The main class created first
class Game:
    # __init__ method to run the rest of the methods
    def __init__(self):
        print('Welcom to our Game collection...')
        print('Please Enter a No. to choose a Game')
        print('Enter (1) to play Even Or Odd Number')
        print('Enter (2) to play Multpication table')
        self.user_choose()
    
    # This method has to do with the chooses of the game type
    def user_choose(self):
        while True:
            user_input = input('Plase choose a Number :')
            try:
                user_input = int(user_input)
                if user_input == 1:
                    return self.Even_Odd()
                elif user_input == 2:
                    return self.multi_table()
                else:
                    print('Please Choose between 1, 2, 3')
            except ValueError:
                print('Pleas Enter a Valid Number')
            
        
    # This method to the run the game 
    def Even_Odd(self):
        print('Hello pal')
        print('Welcom to the Game .. Where I can tell if the number you entered is EVEN or ODD')
        print('If you want to exit the game press x')

        while True:
            user_number = input('Please Enter a Number: ')
            if user_number == 'x':
                print('Closing the Game')
                break

            try:
                user_number = int(user_number)
                if user_number % 2 == 0:
                    print('EVEN Number!')
                else:
                    print('ODD Number!')
            except ValueError:
                print('Please Enter a valid Number')
            print('------------------------')
            
    
    def multi_table(self):
        x = int(input('Please Enter First No. '))
        y = int(input('Please Enter Second No. '))
        print('The result is: ' + str(x * y))

game1 = Game()