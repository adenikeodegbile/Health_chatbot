# %%
!pip install streamlit ollama

# %%
import streamlit as st
import ollama

# %%
# Set the title for your app
st.title("Med-Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# %%
#React to user input
if prompt := st.chat_input("Ask about medical topics..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call the local Ollama model to get a response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(model='mistral', messages=st.session_state.messages)
            st.markdown(response['message']['content'])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response['message']['content']})

# %%
jupyter nbconvert --to script app.ipynb

# %%



