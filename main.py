import random
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Guess the Number", page_icon="🎯", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            text-align: center;
        }
        .stTextInput, .stNumberInput, .stButton {
            width: 100%;
            font-size: 18px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Instructions
st.markdown("<h1 style='text-align: center; color: #333;'>🎯 Guess the Number Game 🎯</h1>", unsafe_allow_html=True)
st.write("**Try to guess the secret number between 1 and 100!**")

# Initialize Session State
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# User Input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, format="%d")

# Guess Button
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again. ⬆")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again. ⬇")
    else:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts! 🎉")
        st.balloons()
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0