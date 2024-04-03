import json

def parse_jsonl_for_fields(file_path, fields):
    """
    Parses a JSONL file and returns dictionaries for specified fields.

    :param file_path: Path to the JSONL file.
    :param fields: List of fields to extract data for.
    :return: A dictionary where each key is a field and the value is another dictionary
             of question-answer pairs for that field.
    """
    data = {field: {} for field in fields}
    
    with open(file_path, 'r') as file:
        for line in file:
            line_data = json.loads(line)
            field = line_data.get('metadata', {}).get('field')
            question = line_data.get('question')

            for answer_key in line_data.get('answers', {}):
                revised_answer = line_data['answers'][answer_key].get('revised_answer_string')
                if field in fields and question and revised_answer:
                    data[field][question] = revised_answer
                    break # There is only one revised answer per question

            if field in fields and question and revised_answer:
                data[field][question] = revised_answer

    return data

fields_of_interest = ["Healthcare / Medicine", "Law"]
parsed_data = parse_jsonl_for_fields('expertqa.jsonl', fields_of_interest)

# Display a small part of the data to verify
for field in parsed_data:
    print(f"Field: {field}, Number of entries: {len(parsed_data[field])}")
    for question in list(parsed_data[field].keys())[:2]:  # Displaying the first two entries for brevity
        print(f"  Question: {question}")
        print(f"  Answer: {parsed_data[field][question][:100]}...")  # Displaying first 100 characters of answer
    print("\n")