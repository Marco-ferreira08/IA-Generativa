# -*- coding: utf-8 -*-
"""IA-Chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rHXylUGJ1rlSkEZvMRtGDF1QVT0X0X8m
"""

!pip install google-genai

import os

from google.colab import userdata

os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

from google import genai

client = genai.Client()

for model in client.models.list():
  print(model.name)

modelo = 'gemini-2.0-flash'

chat = client.chats.create(model=modelo)

resposta = chat.send_message("Oi, tudo bem?")

resposta.text

resposta = chat.send_message("Você é um assistente pessoal e você sempre responde de forma sucinta. O que é a inteligência artificial?")

resposta.text

from google.genai import types

chat_config = types.GenerateContentConfig(
    system_instruction = "Você é um assistente pessoal e você sempre responde de forma sucinta. Porém, você sempre vai explicar muito bem, afinal de não ficar nenhuma dúvida.",
)

chat = client.chats.create(model=modelo, config=chat_config)

prompt = input("Esperando prompt: ")

while prompt != "fim":
  resposta = chat.send_message(prompt)
  print("Resposta:", resposta.text)

  prompt = input("Esperando prompt: ")