# python script that reads expertqa json file and writes to a csv file

import json
import csv
import openai

openai.api_key = 'OPENAI_API_KEY'

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
        response = openai.Completion.create(
          engine="gpt-3.5-turbo",
          prompt=question,
          max_tokens=100
        )
        writer.writerow([question, response.choices[0].text.strip()])
