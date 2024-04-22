import streamlit as st

def rps_game(player1, player2):
    if player1 == "Rock" and player2 == "Paper":
        return "Player2 wins"
    elif player1 == "Rock" and player2 == "Scissors":
        return "Player1 wins"
    elif player1 == "Paper" and player2 == "Rock":
        return "Player1 wins"
    elif player1 == "Paper" and player2 == "Scissors":
        return "Player2 wins"
    elif player1 == "Scissors" and player2 == "Rock":
        return "Player2 wins"
    elif player1 == "Scissors" and player2 == "Paper":
        return "Player1 wins"
    else:
        return "It's a tie"

def main():
    st.title("Rock, Paper, Scissors Game")

    st.write("Welcome to RPS!")
    st.write("Choose either Rock, Paper, or Scissors")
    st.write("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock")

    player1_choice = st.selectbox("Player 1", ["Rock", "Paper", "Scissors"])
    player2_choice = st.selectbox("Player 2", ["Rock", "Paper", "Scissors"])

    if st.button("Play"):
        result = rps_game(player1_choice, player2_choice)
        st.write("Player 1 chose:", player1_choice)
        st.write("Player 2 chose:", player2_choice)
        st.write(result)

if __name__ == "__main__":
    main()
