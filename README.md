
1.	##1	Explore the data set and look at the format of the files.

 	 •Our first task in this project is exploring the json_schema.txt file to identify the important field that we would need 		to extract from our Json file for clustering and summarizing the document. We can open it this file by
      				o	 f = open ("CORD-19-research-challenge/json_schema.txt", 'r')
     			    	 o	x = f.readlines()
    				o	f.close()
 	 •	As it is clear in the schema text file this Json data dictionary contain 
o	“paper_ id”: which string and doesn’t have any meaning to help us to use. 
o	“metadata that contain 
	“title”:  which is the string and it might be good for using.
	“authors”: this one is a list of dictionary contain the information about authors such as first/last name, email…. That I don’t think it would important for us in this project
	“abstract”: this one also is a list of dictionary contain the:
o	 “text”, string that might be helpful for us in this project”
o	cite_spabs” is list of dictionary that contain the position of the where the cations are.
o	,”ref_spans”, as explain in the text it is the same as “cite_span” it is a list of dictionary
o	” section”: this part contains abstract text
	“body text”: this part is a list of dictionary contain the:
o	“text” which is string and conation text body of paper which it is important in our project.
o	cite_spabs” it is list of dictionary that contain the cations 
o	,”ref_spans”,” it is a list dictionary
o	“section” 
	“introduction” it is string contain introduction of the paper
	“conclusion” it is string contain conclusion of the paper
	 bib entries” which contain different BIBREF which that one also contains different string, list dictionary, integer about the information of the people and paper that cite in the citations that I think it is not important in our project.
	"ref_entries”: which contain different "FIGREF" and "TABREF” which contain string that explain the caption of the figure and table and figure and table as well.
	"back matter" this one is the same as “body_text” as explain in the text that contain list of dictionary
      
2.	Write a function to choose a set of documents in the data set, randomly choose 10 percent of the total files.

•	For this part I wrote a function which first I used glob method to get access to the file we download and unzip it from Kaggle website and recursive = True to get all 4594 ?
•	 Then I used np.random.choice to get the 10 present of the that 45944 file which would be 4594 .

3.	Write a file reader a file and tokenize the data.

•	In this part we need to have a function that take a 10 percent of the data and then tokenize it. Because the data format is Json we need to open our files and then call the Json.load for opening our Json file.  Which I opened mine with enumerate and because I got getting error “   ”  after googling I add one (i) to my enumerate but still I don’t understand it.  Then I decided to have a better view of my dataset in form of DataFrame. I choose three columns from my Json file that I thought it might be helpful for this project, which are “title”,”text” from “abstract and “text” from “body_text”. Beacuse each documents have different paragraphs and we need combine each paragraph 
I read an empty list and append the “abstract” and “body_text” ‘s text to their empty list. At the end I add all of them to my DataFrame tuples.

•	I saved the result of this reader function in df, and in rest of the code instead of calling the function I am working with this df.
		
•	The second job of this part was Tokenizing, which first I decided to make a function that I called (normalize) for consider everything that I can make the text cleaner and make it ready for tokenizing.  I used some of them from internet and lectures and some of them that repeated a lot in text by myself. After that I used both sentences and word tokenizing. First I wrote function to do sent tokenize and called the (normalize) function in it to consider all the cleaning part in tokenize as well. Finally I make word tokenize function and called the (senttokenizg) in it to consider both cleaning and sent tokenize as well. But I didn’t specific different on my text when I used sent.tokenize module but I decided to apply it on my text because I thought it might have impact but I cannot recognize it.
•	After applying all tokenize functions I update the DataFarme by using (lambda) for iterating through all 4594 columns on [“title”, “abstreact_text”,”text_body”] to tokenize them and make them ready for next step.     

4.	Write a function to take tokenized data and add it to the clustering method of your choice.

•	After tokenizing our data, we need to convert it into a format that would be ready for do clustering. Based on the lecture explaining first we need to use np.vectorize to convert it to vector and then  we need to take a list of items . In this part I totally follow The professor way and called it even in the same name. (normcorpus) is the one that get the list of the item in the vector style. Then I check the length of that which was correct (4014). After that called My TFIDF vectorising this also will convert our string formatted data into a measure of how important each word is to the instance out of the literature as a whole. Vectorising our data. We will be clustering based off the content of the body text
•	Before doing clustering I did some feature extraction to check the similarity by cosine_similarity method then based on the [“title”] part found some similarity of our text based on their tittle.
•	For doing clustering we need to find the number of the clustering in this part first I used PCA and reduce the size of our array  and then first and use cdist module to find the number of different k. Finally show it in the graph and we find the number of the k from the part of distortion that near to make smooth decrease which in my case was 10 and I used 10 as number of my cluster. This method knows as Elbow method.
•	Finally I used K-Means clustering method for clustering and  Silhouette Coefficient  to masseur the quality of the cluster. 

5.	Write a function to take clusters of documents, and summarize the documents.
•	
6.	Write the summarized clusters to a file.

Write a function to take tokenized data and add it to the clustering method of your choice:
