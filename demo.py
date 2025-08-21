import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()
llm=ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("groq_api_key"),
    model_name="llama-3.3-70b-versatile"
)
prompt=ChatPromptTemplate.from_messages(
    [("system","You are an assistant who needs to convert a given task which is {human_input} into numerous subtasks seperated by -> with proper guidance.The subtasks should be short without any details.Also display progress log")]
    # ("human","{human_input}")]
)
chain=prompt| llm

st.set_page_config(page_title="Chatbot Demo")
st.title("CHATBOT DEMO")

a=st.text_area("Enter the query:")
if st.button("Submit"):
  with st.spinner("Processing"):
    inputs={
        'human_input':a

    }
    result=chain.invoke(inputs)
    st.success("Query processed successfully!!")
    st.write(result.content)