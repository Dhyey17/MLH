import player
from Game import TicTacToe, play

print(f"1. Play Against Computer \n"
      f"2. Play Against Human \n"
      f"")
choice = int(input("Enter Your Choice:"))


class GameError(Exception):
    pass


if choice == 1:
    playerX = player.HumanPlayer("X")
    playerO = player.ComputerPlayer("O")
    t = TicTacToe()
    play(t, playerX, playerO)

elif choice == 2:
    playerX = player.HumanPlayer("X")
    playerO = player.HumanPlayer("O")
    t = TicTacToe()
    play(t, playerX, playerO)
    
else:
    try:
        raise GameError
    except GameError:
        print("You did not entered a valid choice")
