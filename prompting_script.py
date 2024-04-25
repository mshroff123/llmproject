# python script that reads expertqa json file and writes to a csv file

import os
from json_parser import parse_jsonl_for_fields
import csv
import openai

# api key, set env key with export OPENAI_API_KEY='your_api_key_here'

openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Define the fields of interest
fields_of_interest = ["Healthcare / Medicine", "Law"]

# Read the JSONL file and parse it for the fields of interest
parsed_data = parse_jsonl_for_fields('expertqa.jsonl', fields_of_interest)

# Get the questions for the fields of interest
questions = [question for field in fields_of_interest for question in parsed_data[field]]

# asking gpt3.5 and/or claude for each question
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Answer"])  # Write header
    for question in questions:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": question}
                ],
                max_tokens=100
            )
            print(response.choices[0].text.strip())
            answer = response['choices'][0]['message']['content'].strip() if response['choices'] else "No answer"
            writer.writerow([question, answer])
        except Exception as e:
            print(f"An error occurred: {e}")

