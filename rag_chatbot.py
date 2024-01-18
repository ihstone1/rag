import configparser
import config
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import getpass
import os
import sys
from rag_helper import fetch_papers,get_similar_vectors

os.environ["OPENAI_API_KEY"] = input("Enter your API Key: ")

paper_list = fetch_papers()

embeddings = OpenAIEmbeddings()
vector_store = embeddings.embed_documents(paper_list)
k = int(config.get_number_of_papers("Similar_papers","k"))
question = input("What is your question? If you do not want to ask another question, just say \"I'm done\" ")
while question != "I'm done":
    similar_vecs=get_similar_vectors(question,k,embeddings,vector_store)

    context = ''
    for i in range(len(similar_vecs)):
        context += paper_list[similar_vecs[i]]

    from openai import OpenAI
    import os
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=os.getenv('OPENAI_API_KEY'),
    )

    base_prompt = """You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise.
    Question: {} 
    Context: {} 
    Answer:
    """

    prompt = f'{base_prompt.format(question, context)}'

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
    ]
    )

    print(response.choices[0].message.content)
    question = input("What is your next question? If you do not want to ask another question, just say \"I'm done\" ")
