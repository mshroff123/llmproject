import gdown
import json
import torch
from transformers import AutoModel, AutoTokenizer, MistralForCausalLM
import re

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


parsed_data = parse_jsonl_for_fields('expertqa.jsonl', ["Healthcare / Medicine", "Law"])
tokenizer = AutoTokenizer.from_pretrained("BioMistral/BioMistral-7B-DARE")
#model = AutoModel.from_pretrained("BioMistral/BioMistral-7B")
model = MistralForCausalLM.from_pretrained('BioMistral/BioMistral-7B-DARE', attn_implementation="flash_attention_2", torch_dtype=torch.float16)
model.gradient_checkpointing_enable()
model.to("cuda")
model.eval()


field_data = parsed_data['Healthcare / Medicine']
for question, answer in field_data.items():

  prompt = f"""
    Instruction: Provide a direct, concise answer to the given question. Do not generate any additional questions or tangents. Stop your response after providing the answer.

    Question: {question}

    <result>
    """


  input_ids = tokenizer.encode(prompt, return_tensors="pt", return_attention_mask=True)[0].unsqueeze(0).to("cuda")
  if tokenizer.pad_token_id is not None:
        attention_mask = input_ids.ne(tokenizer.pad_token_id).to("cuda")
  else:
        attention_mask = torch.ones_like(input_ids, dtype=torch.bool, device="cuda")

  with torch.no_grad():
    beam_output = model.generate(input_ids,
                                  attention_mask = attention_mask,  
                                  min_new_tokens=1,
                                  max_length=600,
                                  num_beams=3,
                                  repetition_penalty=1.4,
                                  early_stopping=True,
                                  eos_token_id=tokenizer.encode("<result>")[0])
    generated_text = tokenizer.decode(beam_output[0], skip_special_tokens=True)        
    result_token = "<result>"
    start_index = generated_text.find(result_token)

    if start_index != -1:
        start_index += len(result_token)
        answer_text = generated_text[start_index:].strip()
    else:
        answer_text = generated_text


  with open('biomistral.json', 'a') as f:
      json.dump({question: answer_text}, f)
      f.write('\n')