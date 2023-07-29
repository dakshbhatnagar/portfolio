import streamlit as st
import random
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


st.title('Hello World')
wins = 0
losses = 0
ties = 0

while True:
    playerChoice = input("Enter rock, paper, or scissors (or q to quit): ")

    if playerChoice.lower() == "q":
        break

    choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices)

    st.markdown("The computer chose:", computerChoice)

    if computerChoice == playerChoice:
        st.markdown("Draw!")
        ties += 1
    elif (playerChoice == "paper" and computerChoice == "rock") or \
            (playerChoice == "rock" and computerChoice == "scissors") or \
            (playerChoice == "scissors" and computerChoice == "paper"):
        st.markdown("Won!")
        wins += 1
    else:
        st.markdown("Lost!")
        losses += 1

st.markdown("Wins:", wins, "Losses:", losses, "Ties:", ties)
