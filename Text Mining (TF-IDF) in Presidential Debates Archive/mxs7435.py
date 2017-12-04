import os
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from math import *
from collections import *

corpusroot = './presidential_debates'
stemmer = PorterStemmer()

N = len(os.listdir(corpusroot))
stopWords = {}
postingsList = {} #frequency of a term in different documents
documentFrequency = {}
fileNames = {}
tfidf = [] #tf-idf table before normalization
squaredSum = [] #squared sum of the row elements of the tf-idf table to normalize the row vector

#converting a text to a list of terms through tokenizing, stopword removal and stemming
def textToTerms(text):

    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(text.lower())
    stemmed_tokens = []

    for term in tokens:
        if term not in stopWords:
            stemmed_term = stemmer.stem(term)
            stemmed_tokens.append(stemmed_term)
    return stemmed_tokens

def getweight(filename, query):
    if query not in postingsList:
        return 0.000000000000
    fileIdx = fileNames.get(filename, 0)
    #division by square root of squaredSum to return the normalized tf-idf table entry
    return tfidf[fileIdx].get(query, 0) / sqrt(squaredSum[fileIdx])

def getidf(query):
    if query in postingsList:
        return log(N / documentFrequency.get(query, 0), 10)
    return -1.000000000000

def query(query):
    terms = Counter(textToTerms(query))
    temp = 0
    for term, termFrequency in terms.items():
        terms[term] = 1 + log(termFrequency, 10)
        temp += pow(terms.get(term, 0), 2)
    for term, termFrequency in terms.items():
        terms[term] = terms.get(term, 0) / sqrt(temp)
        if term in postingsList:
            postingsList[term].sort(key=lambda x: x[1], reverse=True)

    maxSum = -1
    deep = 0
    for docIdx, filename in enumerate(os.listdir(corpusroot)):
        sum = 0
        actual = 1
        for term, termFrequency in terms.items():
            if term not in postingsList:
                continue
            match = 0
            for rank in range(0, 10):
                if rank == len(postingsList[term]):
                    break
                if postingsList[term][rank][0] == docIdx:
                    sum += ((postingsList[term][rank][1] * termFrequency) / sqrt(squaredSum[docIdx]))
                    match = 1
            if match == 0:
                    actual = 0
                    if len(postingsList[term]) > 9:
                        sum += ((postingsList[term][9][1] * termFrequency) / sqrt(squaredSum[postingsList[term][9][0]]))
        if sum > maxSum:
            maxSum = sum
            if(actual == 1):
                maxDoc = filename
            else :
                maxDoc = "fetch more"

    if maxDoc == "fetch more":
        maxSum = 0
    elif maxSum == 0:
        maxDoc = "None"
    return maxDoc, maxSum

def main():

    for w in stopwords.words('english'):
        stopWords[w] = 1

    for idx, filename in enumerate(os.listdir(corpusroot)):
        fileNames[filename] = idx
        file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
        doc = file.read()
        file.close()
        tfidf.append(Counter(textToTerms(doc)))
        for term in tfidf[-1]:
            documentFrequency[term] = documentFrequency.get(term, 0) + 1

    #convert the term frequency table to tf-idf table and build postings list of terms
    for idx, vector in enumerate(tfidf):
        temp = 0
        for term, termFrequency in vector.items():
            vector[term] = (1 + log(termFrequency, 10)) * log (N / documentFrequency.get(term, 0), 10)
            if term in postingsList:
                postingsList[term].append([idx, vector.get(term, 0)])
            else:
                postingsList[term] = [[idx, vector.get(term, 0)]]
            temp += pow(vector.get(term, 0), 2)
        squaredSum.append(temp)

if __name__ == "__main__":
    main()