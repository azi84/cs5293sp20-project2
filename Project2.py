
import pandas as pd
import glob
import json
import numpy as np 
import spacy
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from nltk.tokenize import sent_tokenize, word_tokenize
# random functions
def get_random():
    files = glob.glob(r'CORD-19-research-challenge/**/pdf_json/*.json', recursive=True)
    random_files = np.random.choice(files, int(len(files)*.1))
    return random_files
  # Write a file reader a file and tokenize the data.

def reader ():
    File = get_random()
    dataframe = {"title": [],"text_abstract":[], "text_body": []}
    dataframe = pd.DataFrame.from_dict(dataframe)
    for i,file in enumerate (File):
        tuples = {"title": None, "text_abstract": None,"text_body": None}
        with open(file) as json_data:
            
            data = json.load(json_data)
        
            tuples['title']=data['metadata']['title']
               
            abstract_text= []
            body_text = []
        
            for a in data['abstract']:
                abstract_text.append(a['text'])
                
       
            for b in data['body_text']:
                body_text.append(b['text'])
            

            body = "\n ".join(body_text)
            abstract = "\n". join(abstract_text)
            tuples["text_abstract"] = abstract
            tuples['text_body']=body 
            dataframe = dataframe.append(tuples, ignore_index=True)

    return dataframe
df = reader()  
  
