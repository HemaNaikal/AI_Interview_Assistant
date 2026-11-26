import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant',layout ='centered')
st.title('AI Interview Assistant')
st.caption('Practice interviews with AI-generated questions and constructive feedback.')
st.caption('Launched by Hema Naikal')
st.write('Department of AI&DS')

try:
  client = Groq(api_keys=st.secrets['GROQ_API_KEY'])
  st.write("API connection successfull")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud --> App setting Secrets')
  st.stop()
