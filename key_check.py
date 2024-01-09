import databutton as db
import streamlit as st
import openai

def key_check():
    mtinfo = st.empty()
    mtinfo.info(
        """
        Hi there! My name is Abang Mohammad Firdaus.

        This app allows you to upload your data and get visual insights with just a single prompt. However, to run the app, I need your OpenAI API key. 

        If you don't have a key, you can sign up and create one [here](https://platform.openai.com/account/api-keys).

        Once set up, simply upload your data, prompt about it, and see it visualized! ✨

        """,
        icon="🤖",
    )

    # Accept user input of API key
    mt = st.empty()
    user_provided_key = mt.text_input(
        "Type your OpenAI API key here to continue:", type="password"
    )

    # Check format of API key
    if user_provided_key.startswith("sk-"):
        with st.status("Connected to OpenAI.", expanded=False) as status:
            # Clean the screen
            mt.empty()
            mtinfo.empty()
