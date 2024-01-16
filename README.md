# RAG

After installing the requirements in `requirements.txt`, simply run `python rag_chatbot.py`

You will be prompted for an OpenAI API key. Later, you will be prompted to ask a question. You can continue asking qustions as long as you want. When you are done, sumply input `I'm done`.

Note: the retrieval process involves finding the `k` nearest papers based on cosine similarity. `k` is currently set to `6`, but can be changed in `configurations.ini`.
