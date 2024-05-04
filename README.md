<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">LLMPROJECT</h1>
</p>
<p align="center">
    <em>Empowering Conversations: LLM Project Enhancements</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/mshroff123/llmproject?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/mshroff123/llmproject?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/mshroff123/llmproject?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/mshroff123/llmproject?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Contributing](#-contributing)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The llmproject leverages various NLP models to  evaluate model performance within the healthcare domain. This codebase is designed to evaluate the performance of various open-source models by comparing their outputs to ExpertQA using evaluation metrics such as Smooth BLEU, BERTScore, and Cosine Similarity. The primary goal is to assess how well these models can replicate or improve upon expert-level answers to a variety of questions.


---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project architecture is quite simple. Each file within the generation_code consists of independent scripts that call OpenAI's GPT AI or build out an entire pipeline to run inference on models like Mistral. Each file being independent of the other allows for a modular design that enhances scalability and maintainability if the models were to ever be updated or further tuned. |
| 📄 | **Documentation** | Along with this ReadMe, this project contains documentation in the form of a research paper that can be found here. |
| 🔌 | **Integrations**  | Key integrations include Hugging Face Transformers for model management, NLTK for BLEU score calculation, and PyTorch for model quantization and inference. External dependencies consist of handling JSON and JSONL files with Python's built-in JSON library. |
| 🧩 | **Modularity**    | The codebase is structured with clear separation into two main directories: `generation_code` for model operations and `eval_code` for evaluation metrics. Rest of the directories contain results and outputs. |
| 📦 | **Dependencies**  | Dependencies include Python libraries such as `transformers`, `torch`, `pandas`, `nltk`, and `matplotlib` for data processing, model management, and visualization. The setup requires handling various data formats and integrating multiple machine learning and NLP models. |


---

##  Repository Structure

```sh
└── llmproject/
    ├── LLM Plots cosine_and_bert
    │   ├── bertscore_across_all_models.png
    │   ├── bertscore_across_question_type.png
    │   ├── bertscore_across_specific_field.png
    │   ├── cosine_across_all_models.png
    │   ├── cosine_across_question_type.png
    │   └── cosine_across_specific_field.png
    ├── README.md
    ├── bleu_results
    │   ├── Cleaned Evaluation Bleu Scores.ipynb
    │   ├── Evaluation for LLM Project - Madeline.ipynb
    │   ├── biomstrl_with_qtype_field_smoothed_scores.csv
    │   ├── gpt_with_qtype_field_smoothed_scores.csv
    │   ├── medchatbot_with_qtype_field_smoothed_scores.csv
    │   ├── smoothed_bleu_score_biomstrl.csv
    │   ├── smoothed_bleu_score_gpt.csv
    │   └── smoothed_bleu_score_medicalchatbot.csv
    ├── cosine_bert_with_question_types
    │   ├── biomistral_bert_score_types.csv
    │   ├── biomistral_cosine_similarity_types.csv
    │   ├── gpt_cosine_similarity.csv
    │   ├── gpt_cosine_similarity_types.csv
    │   ├── medical_chatbot_bert_score_types.csv
    │   ├── medical_chatbot_cosine_similarity_types.csv
    │   ├── mistral_bert_score_types.csv
    │   └── mistral_cosine_similarity_types.csv
    ├── cosine_bert_without_question_types
    │   ├── biomistral_bert_score.csv
    │   ├── biomistral_cosine_similarity.csv
    │   ├── gpt_bert_score 2.44.52 PM.csv
    │   ├── gpt_bert_score_types.csv
    │   ├── medical_chatbot_bert_score.csv
    │   ├── medical_chatbot_cosine_similarity.csv
    │   ├── mistral_bert_score.csv
    │   └── mistral_cosine_similarity.csv
    ├── eval_code
    │   ├── Bleu Eval Graphs.ipynb
    │   └── LLM_Evaluation_Cosine_BERT.ipynb
    ├── expertqa.jsonl
    ├── generation_code
    │   ├── biomistral.py
    │   ├── gpt.py
    │   ├── medical_chatbot.ipynb
    │   └── mistral.py
    └── model_outputs
        ├── biomistral.json
        ├── gpt.json
        ├── medical_chatbot.json
        └── mistral.json
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                           |
| [expertqa.jsonl](https://github.com/mshroff123/llmproject/blob/master/expertqa.jsonl) | Summary: Dataset from ExpertQA project. With regards to llmproject, this dataset is scraped to pull medical domain questions along with their respective expert-annotated answers as a groundtruth. |

</details>

<details closed><summary>generation_code</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                |
| ---                                                                                                                 | ---                                                                                                                                                                                                                    |
| [medical_chatbot.ipynb](https://github.com/mshroff123/llmproject/blob/master/generation_code/medical_chatbot.ipynb) | This notebook processes expertqa question-answer pairs from a JSONL file, iterates over only the healthcare questions, and employs a transformer model from huggingface to generate responses, and stores the results in `medical_chatbot.json`. |
| [gpt.py](https://github.com/mshroff123/llmproject/blob/master/generation_code/gpt.py)                               | This script handles the ingestion of JSON data, queries the GPT model for answers, and logs the responses into an output file. |
| [mistral.py](https://github.com/mshroff123/llmproject/blob/master/generation_code/mistral.py)                       | `mistral.py` processes expertqa question-answer pairs from a JSONL file, iterates over only the healthcare questions, and employs a transformer model from huggingface to generate responses, and stores the results in `mistral.json`. |
| [biomistral.py](https://github.com/mshroff123/llmproject/blob/master/generation_code/biomistral.py)                 | `biomistral.py` processes expertqa question-answer pairs from a JSONL file, iterates over only the healthcare questions, and employs a transformer model from huggingface to generate responses, and stores the results in `biomistral.json`. |

</details>

<details closed><summary>bleu_results</summary>

| File                                                                                                                                                         | Summary                                                                                                                                                                                                                |
| ---                                                                                                                                                          | ---                                                                                                                                                                                                                    |
| [Cleaned Evaluation Bleu Scores.ipynb](https://github.com/mshroff123/llmproject/blob/master/bleu_results/Cleaned Evaluation Bleu Scores.ipynb)               | Insert here                                                                  |


</details>

<details closed><summary>eval_code</summary>

| File                                                                                                                                | Summary                                                                                                                                                                         |
| ---                                                                                                                                 | ---                                                                                                                                                                             |
| [Bleu Eval Graphs.ipynb](https://github.com/mshroff123/llmproject/blob/master/eval_code/Bleu Eval Graphs.ipynb)                     | Summary: Insert Here |
| [LLM_Evaluation_Cosine_BERT.ipynb](https://github.com/mshroff123/llmproject/blob/master/eval_code/LLM_Evaluation_Cosine_BERT.ipynb) | Insert here   |

</details>


---


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/mshroff123/llmproject/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/mshroff123/llmproject/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/mshroff123/llmproject/issues)**: Submit bugs found or log feature requests for Llmproject.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/mshroff123/llmproject
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>


---

##  Acknowledgments

- MistralAI for their open-source model.
- BioMistral team for fine-tuning the Mistral-7B model on the BioASQ dataset.
- OpenAI for their GPT 3.5 model.
- Hugging Face for their Transformers library.

- Insert Papers and References here (i.e. BERTScore, BLEU Score, etc.)

---
