def mygame():
    name = input("What is your name sir/madam?")
    
    response = 'Greetings {},'
    print(response.format(name))
    age =int(input('How old are you?'))
    if age >= 18:
        print('Welcome to the casino.')
    elif age < 18:
        print('Leave the game. Now.')
        return 
    game = input('What game would you like to play? (slots or blackjack)')
    response2 = 'Okay lets play {}'
    print(response2.format(game))
    
    if game == 'slots':
        luckyn= input('What is your lucky number?')
        print('Thats a good number. Good luck.')
        def slots():
            
            import random
            import time
            
            x = (random.randrange(1,3))
            y = (random.randrange(1,3))
            z = (random.randrange(1,3))
            print('Here are your numbers below:')
            time.sleep(3)
            print(x)
            time.sleep(1)
            print(y)
            time.sleep(1)
            print(z)
            if x == y == z:
                print('MEGA JACKPOT! YOU WIN ALL THE MONEY!')
                
            elif x == y or x == z or y == z:
                print('You win! Two numbers match!')
                
            elif x != y != z:
                print('Not even close.')
            
            restart = input('Play again? (y/n)')
            if restart == 'y':
                print('Lets get after it.')
                slots()
            if restart == 'n':
                print('Fine, I didnt want you to play anyway. Goodbye.')
                return



        print(slots())
    if game == 'blackjack':
        print('''In this game, each card will have a value of 1 through 11.
You want to get as close as you can to 21 without going over.''')
        def blackjack():
            import random
            import time

            card1 = (random.randrange(1,12))
            card2 = (random.randrange(1,12))
            card3 = (random.randrange(1,12))
            card4 = (random.randrange(1,12))
            card5 = (random.randrange(1,12))
            card6 = (random.randrange(1,12))
            time.sleep(4)
            print('your first card is', card1)
            time.sleep(1)
            print('your second card is',card2)
            total = card1 + card2
            time.sleep(1)
            print('Your total is', total)
            while total <= 21:
                anothercard = input('Would you like another card?(y/n)')
                if anothercard == 'y':
                    x = (random.randrange(1,12))
                    total = total + x
                    print('You drew a', x)
                    print('Your total is now', total)
                    if total == 21:
                        print('You just got Blackjack!')
                        break
                elif anothercard == 'n':
                    print('You stick at', total)
                    break
                    
                            
            else:
                print('You went over 21. You are at', total, 'so you lose')
               

        
            print('Now the dealer goes.')
            card1 = (random.randrange(1,12))
            card2 = (random.randrange(1,12))
            card3 = (random.randrange(1,12))
            card4 = (random.randrange(1,12))
            card5 = (random.randrange(1,12))
            card6 = (random.randrange(1,12))
            time.sleep(1)
            print('The dealers first card is', card1)
            time.sleep(1)
            print('The dealers second card is',card2)
            dtotal = card1 + card2
            time.sleep(1)
            print('The dealers total is', dtotal)
            while dtotal < 22:
                dtotal = dtotal + random.randrange(1,12)
                time.sleep(2)
                print('The dealer got another card, his total is now', dtotal)
                time.sleep(1)
                if dtotal > total and dtotal <= 21:
                    print('The dealer wins becasue he has', dtotal)
                    break
                elif total > 21 and dtotal <= 21 and dtotal >= 15:
                    print('The dealer stops at', dtotal, 'becasue you went over. He wins.')
                    break
                elif dtotal == 21:
                    print('Oh no, the dealer just got Blackjack!')
                    break
                elif dtotal == 21 and total == 21:
                    print('Its a draw at 21!')
                    break
                elif total <= 21 and dtotal > 21:
                    print('The dealer has gone over and you win!!')
                    break
                
                
                elif total > 21 and dtotal > 21:
                    print('Wow, you both lost.')
                    break
            

##            else:
##                print('The dealer has gone over 21, he is now at', dtotal, 'so he loses.')
            restart = input('Play again? (y/n)')
            if restart == 'y':
                print('Lets get after it.')
                blackjack()
            if restart == 'n':
                print('Fine, I didnt want you to play anyway. Goodbye.')
                return    
            

        print(blackjack()) 
                  
    













print(mygame())
