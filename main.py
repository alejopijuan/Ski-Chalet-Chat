import requests
import json
import os


def get_available_resorts():
  url = "https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort"

  headers = {
      "X-RapidAPI-Key": "292b37741emsh8c5ef5e63f9442ep19a024jsnff83c46ee798",
      "X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers)

  available_resorts = response.json()
  return available_resorts


import openai
from openai import OpenAI

def get_url_for_mountain_conditions(mountain):
  client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": f"Given the mountain that the user wants to know the skiing conditions for: {mountain}, retrieve the correct URL from this JSON:{get_available_resorts()}. ONLY RETURN THE URL AND NOTHING ELSE.",
          }
      ],
      model="gpt-4-1106-preview",
  )
  return chat_completion.choices[0].message.content.strip()



def get_mountain_conditions(url_for_mountain):
  headers = {
    "X-RapidAPI-Key": "292b37741emsh8c5ef5e63f9442ep19a024jsnff83c46ee798",
    "X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
  }

  response = requests.get(url_for_mountain, headers=headers)
  return response.json()



url_for_mountain = get_url_for_mountain_conditions("alpine meadows")
print(url_for_mountain)
mountain_conditions = get_mountain_conditions(url_for_mountain)
print(mountain_conditions)