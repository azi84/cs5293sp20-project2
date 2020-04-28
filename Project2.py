
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
from nltk.stem import WordNetLemmatizer

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

#Removinf stop word
stop_words = nltk.corpus.stopwords.words('english')
stop_words
stop_words[:20]

# claening and get ready for toknizing
def normalize(txt):
    #txt = reader()
    txt = re.sub(r'[^a-zA-Z0-9\s]', ' ', str(txt), re.I|re.A)
    txt = re.sub("(^|\W)\d+($|\W)", " ", txt)   #remove whitespace and numbers
    txt = txt.replace('title', '')       #remove 'title'
    txt = re.sub('[!#?%*&$)@^(.,-=+:";]', '', txt)       #remove punctuation
    txt = re.sub(r"\b[a-zA-Z]\b",'',txt)        #remove single letters
    txt = re.sub(r'\d+', '', txt)
    txt = re.sub(r'\\b[A-Z a-z 0-9._ - ]*[@](.*?)[.]{1,3} \\b', '', txt)#remove email
    txt = txt.replace('introduction', '')       #remove 'introduction'
    txt = txt.replace('text', '')
    txt = txt.replace('background', '')         #remove 'background'
    txt = txt.replace('abstract', '') 
    txt = txt.replace('\\n', ' ')   
    txt = txt.replace('\n', ' ')
    txt = txt.replace('///', ' ') 
    txt = txt.replace("'", '')
 
# word tokenize function 
def wordtokenizing(txt):
    wordnet_lemmatizer = WordNetLemmatizer()
    word = normalize(txt)
    tokens = nltk.word_tokenize(word)
    word_tokens = [t for t in tokens if t not in stop_words]
    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
    return ' '.join(word_tokens)   
    txt = re.sub(r'^\w\w?$', '',txt) 
    txt = txt.lower()
    return txt

# tokening each of them and adding the tokenize one to the Data Frame
#lambda help us to irtertae tokenig through each row
df['title'] = df['title'].apply(lambda x: wordtokenizing(x))
df['text_abstract'] = df['text_abstract'].apply(lambda x: wordtokenizing(x))
df['text_body'] = df['text_body'].apply(lambda x: wordtokenizing(x))


tf = TfidfVectorizer(preprocessor = wordtokenizing,stop_words=stop_words)
tfidf_matrix = tf.fit_transform(norm_corpus)
tfidf_matrix.shape


km = KMeans(n_clusters=10,init='k-means++')
km.fit(tfidf_matrix)
%time
%timeit
km.labels_
df['kmeans_cluster'] = km.labels_

from sklearn.metrics import silhouette_score
score_max = -1 #this is the minimum possible score
for k in range(1,10):
    silhout= silhouette_score(tfidf_matrix,  df['kmeans_cluster'],metric='euclidean')
    print("The silhouette score for %i clusters is %0.2f" %(k,silhout))
    if silhout > score_max:
        score_max = silhout
        best_number_clusters = k
        
text_clusters = (df[['kmeans_cluster', 'text_body']]
                  .sort_values(by=['kmeans_cluster', 'text_body'], 
                               ascending=False)
topn_features = 9
ordered_centroids = km.cluster_centers_.argsort()[:, ::-1]
ordered_centroids
feature_names = tf.get_feature_names()
for cluster_num in range(10):
    key_features = [feature_names[index] 
                        for index in ordered_centroids[cluster_num, :topn_features]]
    texts =text_clusters[text_clusters['kmeans_cluster'] == cluster_num]['text_body'].values.tolist()
    print('CLUSTER #'+str(cluster_num+1))
    print('Key Features:', key_features)
    print('Text :', texts)
    print('-'*80)                 
                  .groupby('kmeans_cluster').head(20))        
