# RAG (Retrieval-Augmented Generation)
This project fetches research papers from arXiv, generates vector embeddings, and uses OpenAI's GPT-3.5 model to answer user questions based on the most relevant papers. It demonstrates a Retrieval-Augmented Generation (RAG) approach by combining information retrieval with LLM question answering.

## Features
Fetch research papers from the arXiv API.
Find relevant papers using vector embeddings and cosine similarity.
Use OpenAI's GPT-3.5 to generate concise answers based on retrieved papers.

## Installation
1. Clone the repository:

`git clone https://github.com/your-username/rag.git`

`cd rag`

2. Install dependencies:

`pip install -r requirements.txt`

3. Get your OpenAI API Key:
* Obtain it from the OpenAI Platform.

## Usage
1. Run the script:
`python rag_chatbot.py`

2. Enter your OpenAI API Key when prompted.

3. Ask questions:
* The script will fetch papers and generate answers based on your queries
* Type "I'm done" when finished.

## Configuration
The number of similar papers to retrieve (k) can be set in the configurations.ini file.
