import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import time

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

prompt = st.chat_input("Say something")
if prompt:
    # Call the LLM with streaming
    config = {"configurable": {"thread_id": "abc789"}}
    input_messages = [HumanMessage(content=prompt)]
    
    def stream_response():
        for chunk in model.stream(
            input_messages,
            config=config,
        ):
            if isinstance(chunk, AIMessage):
                yield chunk.content + " "
                time.sleep(0.02)

    st.write_stream(stream_response)
