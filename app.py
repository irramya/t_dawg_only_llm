import streamlit as st
import chat_ui
import strings

def main():

    st.subheader(strings.welcome, divider=True)

    chat_ui.show_chat()

if __name__ == '__main__':
    main()