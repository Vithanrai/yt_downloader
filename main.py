import streamlit as st
from frontend.html_template import css
import time

from services.downloader import transcribeVideoOrchestrator
from services.emojis_switch import update_emoji

import warnings 
warnings.filterwarnings("ignore")    



def main():
    st.set_page_config(page_title="YT downloader", page_icon=":fire:", layout="wide")
    st.write(css, unsafe_allow_html=True)
    
    st.title(f"Youtube Video Downloader 🌍🌎🌏")
    st.write("Download your favourite 💖 youtube videos with the click of a button")
    url = st.text_input("Enter YouTube URL:")

    if st.button("Download"):
        if url:
            st.text("Downloading your favourite video 🐱‍🏍")
            result = transcribeVideoOrchestrator(url, output_directory = "videos")
            if result == "Download Complete":
                st.write("Download Complete 😎")
            else:
                st.write("Sorry, I wasn't able to download the video 😓\n Try downloading another video 🤩")
        else:
            st.write("Please provide a URL to download ")

if __name__ == '__main__':
    main()
