import getpass
#points
def RPS():
    Rock = "Rock"
    Paper = "Paper"
    Scissors = "Scissors"
#start
    print("Welcome to RPS!")
    print("Choose either Rock, Paper, or Scissors")
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock")
    print("WARNING!!!TYPE YOUR ANSWER WITH THE FIRST LETTER AS A CAPITAL")
    
    print("Player1, Rock, Paper, or Scissor?")
    Player1 = getpass.getpass(prompt="Player1: ").strip().capitalize()
    print("Player2, Rock, Paper, or Scissor?")
    Player2 = getpass.getpass(prompt="Player2: ").strip().capitalize()

    print("Player1 chose:", Player1)
    print("Player2 chose:", Player2)

    if Player1 == Rock and Player2 == Paper:
        print("Player2 wins")
    elif Player1 == Rock and Player2 == Scissors:
        print("Player1 wins")
    elif Player1 == Paper and Player2 == Rock:
        print("Player1 wins")
    elif Player1 == Paper and Player2 == Scissors:
        print("Player2 wins")
    elif Player1 == Scissors and Player2 == Rock:
        print("Player2 wins")
    elif Player1 == Scissors and Player2 == Paper:
        print("Player1 wins")
    elif Player1 == Rock and Player2 == Rock:
        print("tie")
    elif Player1 == Scissors and Player2 == Scissors:
        print("tie")
    elif Player1 == Paper and Player2 == Paper:
        print("tie")
    else:
        print("That is not valid")



if __name__ == '__main__':
    RPS() 