# AI Resume Screening System with LangChain & LangSmith

## Overview

This project is an AI-powered Resume Screening System built using LangChain and OpenAI.

The system evaluates resumes against a job description and provides:

* Skill extraction
* Resume-job matching
* Candidate scoring
* Explainable feedback

It also integrates LangSmith tracing for debugging and monitoring LLM pipelines.

---

## Features

* Resume parsing
* Skill extraction
* AI-powered matching
* Candidate fit scoring
* Explainable AI output
* LangSmith tracing
* Modular LangChain architecture

---

## Tech Stack

* Python
* LangChain
* LangSmith
* OpenAI GPT
* LCEL
* Prompt Engineering

---

## Project Structure

```bash
prompts/
chains/
data/
main.py
requirements.txt
README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## LangSmith Tracing

Enable tracing in `.env`

```env
LANGCHAIN_TRACING_V2=true
```

---

## Sample Outputs

### Strong Candidate

Score: 92

### Average Candidate

Score: 65

### Weak Candidate

Score: 22

---

## Learning Outcomes

* LangChain pipelines
* Prompt engineering
* Explainable AI
* LLM tracing
* AI recruitment systems

---

## Future Improvements

* Streamlit deployment
* PDF resume support
* Vector database integration
* Multi-job evaluation
* Advanced ATS scoring

