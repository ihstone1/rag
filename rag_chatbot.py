import configparser
import config
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import getpass
import os
import sys
from rag_helper import fetch_papers,get_similar_vectors
from openai import OpenAI

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your API Key: ")

paper_list = fetch_papers()

embeddings = OpenAIEmbeddings()
vector_store = embeddings.embed_documents(paper_list)
k = int(config.get_number_of_papers("Similar_papers","k"))
question = input("What is your question? If you do not want to ask another question, just say \"I'm done\" ")


def main():
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    while question != "I'm done":
        similar_vecs=get_similar_vectors(question,k,embeddings,vector_store)

        context = ''.join(paper_list[i] for i in similar_vecs)

        base_prompt = """You are an assistant for question-answering tasks. 
        Use the following pieces of retrieved context to answer the question. 
        If you don't know the answer, just say that you don't know. 
        Use three sentences maximum and keep the answer concise.
        Question: {} 
        Context: {} 
        Answer:
        """

        prompt = f'{base_prompt.format(question, context)}'

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                ]
            )
            print(response.choices[0].message.content)
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
        question = input("What is your next question? If you do not want to ask another question, just say \"I'm done\" ")

if __name__ == "__main__":
    main()
