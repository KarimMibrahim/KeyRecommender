#!/usr/bin/env python
import os
import re
import urllib2
import nltk.data
import logging
from bs4 import BeautifulSoup
import numpy as np
from gensim.models import Word2Vec
from tempfile import TemporaryFile
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.feature_extraction.text import CountVectorizer

def makeFeatureVec(words, model, num_features):
    featureVec = np.zeros((num_features,),dtype="float32")
    nwords = 0.
    index2word_set = set(model.index2word)
    for word in words:
        if word in index2word_set:
            nwords = nwords + 1.
            featureVec = np.add(featureVec,model[word])
    featureVec = np.divide(featureVec,nwords)
    return featureVec


def getFeatureVectors(reviews, model, num_features):
    counter = 0.
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype="float32")
    for review in reviews:
       if counter%1000. == 0.:
           print "Review %d of %d" % (counter, len(reviews))
       reviewFeatureVecs[counter] = makeFeatureVec(review, model, \
           num_features)
       counter = counter + 1.
    return reviewFeatureVecs


if __name__ == '__main__':

    dataset_descriptions = []
    directory = os.path.join(os.path.dirname(__file__), 'data/HTMLs/')
    for file in os.listdir(directory):
        if file.endswith(".html"):
	    fname = os.path.join(os.path.dirname(__file__), 'data/HTMLs/',file)
    	    with open(fname) as f:
    		content = f.read()
	     	soup = BeautifulSoup(content)
		txt = soup.find(id="description")
		description = ""
		keywords = ""
		if txt is not None:
		    description = re.sub("Expand$","",txt.get_text().strip()).strip()
		txt = soup.find(attrs={"name": "keywords"})
		if txt is not None:
		    keywords = txt['content'].strip()
		if len(description.join(keywords))>1:
        	    dataset_descriptions.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(description.join(keywords), True)))

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = []
    for review in dataset_descriptions:
        sentences += KaggleWord2VecUtility.review_to_sentences(review, tokenizer)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
        level=logging.INFO)
    for e in sentences:
	print e
