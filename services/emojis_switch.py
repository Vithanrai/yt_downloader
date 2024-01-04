import streamlit as st
import time
import random

# List of emojis to display
emojis = ["😊", "😍", "😎", "🥳", "🚀", "🎉", "💻", "🌈"]

# Placeholder for displaying emojis
emoji_placeholder = st.empty()

# Function to update the displayed emoji
def update_emoji():
    while True:
        emoji = random.choice(emojis)
        emoji_placeholder.markdown(f"# {emoji}")
        time.sleep(2)  # Adjust the sleep duration as needed

# Run the emoji update function
update_emoji()
