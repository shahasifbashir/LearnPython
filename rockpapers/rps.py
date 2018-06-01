#This si two player game for rock paper sciscor
import sys
print ("Welcome\n_________________________________________________")
game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
while(True):
    print("Please enter the Choice the choices are:\n1 for Rock \n2 for Paper\n3 for Scissors")
    player1= int(input("Player 1 Please enter your choice : "))
    player2= int(input("Player 2 Please enter your choice : "))
    dif= player1-player2
    if dif in [-1, 2]:
        print('player 1 wins.')
    elif dif in [-2, 1]:
        print('player 2 wins.')
    else:
        print('Draw.Please continue.')
        print('')
    player1 = int(input("Press 1 to continue : "))
    if(player1==1):
        print("\n\n")
    else:
        print("Thank you for playing")
        sys.exit()
