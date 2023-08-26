import openai
from dotenv import load_dotenv
load_dotenv()
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with statements, and your task is to tell whether they are conversational chit-chat or not. Answer with 'it's chitchat' if the statement is chit-chat and answer with 'it's not chi-chat' if the statement is not chit-chat."
    },
    {
      "role": "user",
      "content": "Awesome."
    },

  ],
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message)
