import strings as strings
import app_controls as ac
import streamlit as st
import llm_helper as llm_helper

def show_chat():
# Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = llm_helper.system_message

    # Display chat messages from history on app rerun
    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if query := st.chat_input("Type here..."):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(query)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": query})

        # Get model response
        response = llm_helper.get_model_response(query, st.session_state.messages)

        # Display model response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)

        # Add model response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    if len(st.session_state.messages)>ac.memory_len:
        st.session_state.messages.pop(2)
        st.session_state.messages.pop(1)