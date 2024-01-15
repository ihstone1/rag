import urllib
import xml.etree.ElementTree as ET
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def fetch_papers():

    """Fetches papers from the arXiv API and returns them as a list of strings."""

    url = 'http://export.arxiv.org/api/query?search_query=ti:llama&start=0&max_results=70'

    response = urllib.request.urlopen(url)

    data = response.read().decode('utf-8')

    root = ET.fromstring(data)



    papers_list = []

    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):

        title = entry.find('{http://www.w3.org/2005/Atom}title').text

        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text

        paper_info = f"Title: {title}\nSummary: {summary}\n"

        papers_list.append(paper_info)



    return papers_list



def get_similar_vectors(user_query:str,k:int,embeddings,vector_store):
    query_embeddings = embeddings.embed_query(user_query)
    similarities = []
    index = []
    for i in range(len(vector_store)):
        similarities.append(cosine_similarity([query_embeddings,vector_store[i]])[0][1])
    sorted_similarities = np.sort(similarities)
    sorted_similarities = sorted_similarities[len(vector_store)-k:]
    for i in range(k):
        index.append(np.where(similarities == sorted_similarities[-(i+1)])[0][0])
    return index