# Azadeh Gilanpour - Project2- Summarization

Millions of documents are push onto the Internet every year. Hundreds of thousands of those documents are academic documents that may be meaningful. Unfortunately, no human is able to wade through the gruff to reach the meaningful documents. Most scientist only look at documents that are published at “prestigious” journals and conferences. In this project, you are going to exercise what you have learned so far in class to help scientists and interested citizes get a lay of the land when it comes to publlished academic work.

In this project, we will cooperate with classmates to summarize as much of the corona virus literature as possible. 
We want to help scientists and interested citizes get a lay of the land when it comes to publlished academic work. 

So we need to do:
1.  Select a subset of academic documents.
2.  Tokenize and cluster the documents.
3.  Summarize each cluster.

We will use a data set available from the Allen Institute for AI through Kaggle. https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge . You may need to register and get a Kaggle account to access the data.


# Six step below exlpain each job was done for this project:

All step was done in the jupyter notebook, and exh part I will explain the function and runnig style.

## 1. Explore the data set and look at the format of the files.
Our first task in this project is exploring the json_schema.txt file to identify the important field that we would need to extract from our Json file for clustering and summarizing the document. We can open it this file by blow code:
    

 - f = open ("CORD-19-research-challenge/json_schema.txt", 'r')
 - f.readlines()
 - f.close()

After Runnig that you will see  the schema text file of the Json data  that :
<![endif]-->

**“paper_ id”**: which string and doesn’t have any meaning to help us to use.

**“metadata”** that contain :
 

 - **“title”:**  which is the string and it might be good for using.
 - **“authors**”: this one is a list of dictionary contain the information about authors such as first/last name,    email…. That I don’t think it would important for us in this project
 - **“abstract”**: this one also is a list of dictionary contain the:

  -  -  -**“text”,** string that might be helpful for us in this project”

 -  - **cite_spabs”** is list of dictionary that contain the position of the where the cations are.

 -  - **”ref_spans”,** as explain in the text it is the same as “cite_span” it is a list of dictionary
 -  - **” section”:** this part contains abstract text
 - **“body text”:** this part is a list of dictionary contain the:

 -  - **“text”** which is string and conation text body of paper which it is important in our project.

 -  - **cite_spabs”** it is list of dictionary that contain the cations

 -  - ,”**ref_spans”,**” it is a list dictionary
 -  - **“section”**

 -  - **“introduction”** it is string contain introduction of the paper

 -  - **“conclusion”** it is string contain conclusion of the paper

 - **bib entries”** which contain different BIBREF which that one also contains different string, list dictionary, integer about the information of the people and paper that cite in the citations that I think it is not important in our project.

 - **"ref_entries”**: which contain different "FIGREF" and "TABREF” which contain string that explain the caption of the figure and table and figure and table as well.

 - **"back matter"** this one is the same as “body_text” as explain in the text that contain list of dictionary

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## 2. Write a function to choose a set of documents in the data set, randomly choose 10 percent of the total files.
For this part I make a function which first I used **glob** method to get access to the file we have to download it and unzip it from Kaggle website to get all *45941* files.
Then I used **np.random.choice** to get the 10 present of the that 4*5941* file which would be 4*594*

## 3.  Write a file reader a file and tokenize the data.


In this part we need to call a a function that take a 10 percent of the data and then tokenize it. Because the data format is Json we need to open our files and then call the Json.load methods for opening our Json file.  Which I opened mine with enumerate . Also because I got getting error *“ expected str, bytes or os.PathLike object, not tuple* ”  after googling I add one **(i)** to my enumerate to fix it.  Then I decided to have a better view of my dataset in form of DataFrame. I choose three columns from my Json file that I thought it might be helpful for this project, which are **“title”**,**”text” from “abstract** and “**text” from “body_text”**. Beacuse each documents have different paragraphs and we need combine each paragraph which I read an empty list and append the “abstract” and “body_text” ‘s text to their empty list. At the end I add all of them to my DataFrame tuples.

I saved the result of this reader function in df, and in rest of the code instead of calling the function I am working with this df.

The second job of this part was Tokenizing, which first I decided to make a function that I called (normalize) for consider everything that I can make the text cleaner and make it ready for tokenizing.  I used some of them from internet and lectures and some of them that I saw they repeated a lot in text by myself. After that I use word tokenizing and WordNetLemmatize. In my word tokenize function I called (nomalize ) function  to consider cleaning on it. I tried sent tokenizing as well but I couldn't find any differences so I decided to go with word to tokenizng.



## 4.  Write a function to take tokenized data and add it to the clustering method of your choice.
After tokenizing our data, we need to convert it into a format that would be ready for do clustering. Based on the lecture explaining first we need to use **np.vectorize** to convert it to vector and then we need to take a list of items . In this part I totally follow The professor way and called it even in the same name. (norm_corpus) is the one that get the list of the item in the vector style. Then I check the length of that which was correct (4594). After that used TFIDF vectorising this also will convert our string formatted data into a measure of how important each word is to the instance out of the literature as a whole. Vectorising our data. We will be clustering based off the content of the body text. I used the k- menas clustring for clustring and used Elbow method to find the number of the clustring. The code is not wrote by me I used it from interent and cite it in this project. 
This method use **PCA** to reduce the size of the array and then use cdit to find the special distant and run with different number of k as number of the clustring. I tried range of (1,50) . 



based on the explniation of the elbow method, number of the k will be choose when we are near to smooth decreased which I think here is 10. So I Used 10 as number of my clustring. 
Also after getting result and many time running clustring I got some thing that was really intersting for me.
Also I used Silhouette coefficient on my clustring result to mesuaer the quailty of each cluster.
 
When In question 3 I read the file and tokenized them and applied that cleaning and tokenizing to each coulum for each row with this commond  *df['text_abstract'] = df['text_abstract'].apply(lambda x: wordtokenizing(x))* I got real bad result in my clustring so I decided to do nit applied. But I found the reson wich was in my vectorizg that when I called my tokenizng function appied more cleaning on them. 

 
# 5.Write a function to take clusters of documents, and summarize the documents.

For this part I searched a lot from the book to the interent and even read some papers to undresand what should we have do. The thing that I usndrestod was for doing summarizng on text the we need to have some method:
Similarty Matrix --> Graph--> Ranking --> summurizng.
I tried two different type of the ranking and my summrization was different. You can see the code and result for both of them in my python code.
The first one was TextRank based on the project suggested to do and the other one was using Networkx and pageranking. The result I got from both of the was different so I decied to put both on my code. 
