## Integrate our code with open AI API key
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st


os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Demo with OpenAI API!')
input_text = st.text_input("search the topic you want")

# Open AI LLMS
llm=OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text))



