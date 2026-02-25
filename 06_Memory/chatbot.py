"""Python file to serve as the frontend"""

import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories.streamlit import StreamlitChatMessageHistory

load_dotenv(find_dotenv())

# Create a prompt template that includes message history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI chatbot having a conversation with a human."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Create Streamlit chat message history
msgs = StreamlitChatMessageHistory(key="special_app_key")


def load_chain():
    # Initialize the LLM with model parameter
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    # Create the base chain using LCEL
    chain = prompt | llm | StrOutputParser()
    
    # Wrap the chain with message history
    conversation = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    return conversation


def initialize_session_state():
    if "chain" not in st.session_state:
        st.session_state.chain = load_chain()

    if "generated" not in st.session_state:
        st.session_state.generated = []

    if "past" not in st.session_state:
        st.session_state.past = []

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    if "widget_input" not in st.session_state:
        st.session_state.widget_input = ""


initialize_session_state()

st.set_page_config(page_title="LangChain ChatBot Demo", page_icon=":robot:")
st.header("LangChain ChatBot Demo")


def submit():
    st.session_state.user_input = st.session_state.widget_input
    st.session_state.widget_input = ""


st.text_input("You:", key="widget_input", on_change=submit)

if st.session_state.user_input:
    # Use invoke instead of run (modern LCEL approach)
    output = st.session_state.chain.invoke(
        {"input": st.session_state.user_input},
        config={"configurable": {"session_id": "streamlit_session"}}
    )
    st.session_state.past.append(st.session_state.user_input)
    st.session_state.generated.append(output)

    st.session_state.user_input = ""

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
