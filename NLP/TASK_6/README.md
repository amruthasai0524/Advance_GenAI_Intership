# NLP Token Classification using Transformers

## Overview

This project demonstrates NLP Token Classification using Transformer models and the Hugging Face Transformers library.

The project explains:

* Token Classification
* Named Entity Recognition (NER)
* Transformer Architecture
* BERT Model
* Hugging Face Pipeline

---

## Technologies Used

* Python
* Transformers
* Hugging Face
* PyTorch
* NLP

---

## Features

* Named Entity Recognition
* Token-level prediction
* Transformer-based NLP workflow
* Beginner-friendly implementation

---

## Example Output

Input:

```python
"Elon Musk founded Tesla."
```

Output:

```python
Elon Musk → PERSON
Tesla → ORGANIZATION
```

---

## Installation

```bash
pip install transformers
pip install torch
```

---

## Run the Project

```python
from transformers import pipeline

ner_pipeline = pipeline(
    "token-classification",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    aggregation_strategy="simple"
)

text = "Elon Musk founded Tesla."

result = ner_pipeline(text)

print(result)
```

---

## Applications

* Resume Parsing
* Healthcare NLP
* Chatbots
* Information Extraction
* Financial Document Analysis

---

## Author

Amrutha Reddy
