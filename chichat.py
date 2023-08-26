import openai
from dotenv import load_dotenv

import streamlit as st

prompt=st.text_input(label="Enter prompt: ")

load_dotenv()
def main():
  st.header("Learn whether your input text is chit-chat or not!")
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You will be provided with statements, and your task is to tell whether they are conversational chit-chat or not. Answer with 'it's chitchat' if the statement is chit-chat and answer with 'it's not chi-chat' if the statement is not chit-chat."
      },
      {
        "role": "user",
        "content": prompt
      },

    ],
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  st.write(response.choices[0].message["content"])

if __name__=='__main__':
  main()
