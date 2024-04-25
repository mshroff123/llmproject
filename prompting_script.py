# python script that reads expertqa json file and writes to a csv file

import json
import csv
import openai

openai.api_key = 'OPENAI_API_KEY'

# read json file
with open('expertqa.jsonl', 'r') as file:
    questions = json.load(file)


# asking gpt3.5 and/or claude for each question
for question in questions:
    response = openai.Completion.create(
      engine="gpt-3.5-turbo",
      prompt=question,
      max_tokens=100
    )
    print(response.choices[0].text.strip())
