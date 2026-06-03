# BERT Fine-Tuning for Sentiment Analysis

## Project Overview

This project focuses on sentiment analysis using transformer-based deep learning models. A pre-trained BERT/DistilBERT model was fine-tuned on the IMDB Movie Reviews dataset to classify reviews as positive or negative.

The project demonstrates the complete NLP pipeline including preprocessing, tokenization, model training, fine-tuning, evaluation, and performance comparison.

---

## Dataset

Dataset Used:

* IMDB Movie Reviews Dataset

Dataset Source:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

---

## Objectives

* Understand transformer-based NLP models
* Perform BERT fine-tuning for text classification
* Apply tokenization using Hugging Face tokenizer
* Evaluate model performance using classification metrics
* Compare different fine-tuning strategies

---

## Technologies Used

* Python
* Hugging Face Transformers
* PyTorch
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab

---

## Project Workflow

1. Data Collection
2. Data Preprocessing
3. Train/Validation/Test Split
4. Tokenization
5. Model Building
6. Fine-Tuning
7. Model Evaluation
8. Performance Comparison

---

## Data Preprocessing

The following preprocessing steps were performed:

* Lowercase conversion
* HTML tag removal
* Special character removal
* Extra whitespace removal
* Missing value handling
* Label encoding

---

## Model Used

* bert-base-uncased
  OR
* distilbert-base-uncased

The model was fine-tuned using Hugging Face Transformers.

---

## Training Configuration

| Parameter     | Value |
| ------------- | ----- |
| Learning Rate | 2e-5  |
| Batch Size    | 4     |
| Epochs        | 1     |
| Max Length    | 128   |
| Optimizer     | AdamW |

---

## Evaluation Metrics

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 90%+  |
| Precision | High  |
| Recall    | High  |
| F1 Score  | High  |

The transformer-based model achieved strong sentiment classification performance on movie reviews.

---

## Experiments Performed

* Frozen transformer layers
* Fine-tuning last transformer layers
* Full model fine-tuning
* DistilBERT optimization for faster training

---

## Key Learnings

* Understanding transformer architectures
* Practical implementation of BERT fine-tuning
* NLP preprocessing techniques
* Model evaluation and experimentation
* GPU-based training in Google Colab

---

## Future Improvements

* Hyperparameter tuning
* Early stopping implementation
* Learning rate scheduler
* RoBERTa fine-tuning
* Multi-class sentiment classification

---

## How to Run the Project

### Install Dependencies

```bash
pip install transformers datasets accelerate evaluate torch scikit-learn pandas matplotlib seaborn
```

### Run Notebook

Open the Jupyter Notebook or Google Colab notebook and execute all cells sequentially.

---

## Project Structure

```text
bert-imdb-sentiment-analysis/
│
├── bert_finetuning_imdb.ipynb
├── README.md
├── requirements.txt
└── dataset/
```

---

## Author

Amrutha Reddy

---

## GitHub Repository

[Add Your GitHub Repository Link Here]

---

## LinkedIn Post

[Add Your LinkedIn Post Link Here]
