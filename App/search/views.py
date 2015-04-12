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
from django.views.generic.edit import CreateView
from django.shortcuts import render
from mails.models import ContactUs

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

def extract_entities(content):
    entities = []
    for sent in nltk.sent_tokenize(content):
    	for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        	if isinstance(chunk, nltk.tree.Tree):               
                    entities.append(' '.join(c[0] for c in chunk.leaves()))
    return entities


class HomePage(CreateView):
    template_name = "index.html"
    model = ContactUs
    fields = ['name', 'subject', 'message', 'email']
    success_url = "https://www.google.com"


def list_keywords(request):
    keywords = ['ahmed', 'sa3d', 'hi']  # get the dataset using its id
    return render(
        request,
        'search_results.html',
        {"keywords": keywords})


def dataset_detail_view(request, dataset_name):
    # get the specific dataset by id
    fname = os.path.join(os.path.dirname(__file__), 'data/HTMLs/',dataset_name+".html")
    with open(fname) as f:
    	content = f.read()
	soup = BeautifulSoup(content)
	txt = soup.find(id="description")
	description = ""
	keywords = ""
	if txt is not None:
	    description = re.sub("Expand$","",txt.get_text().strip()).strip()
    new_entity=extract_entities(description)
    keywords =set(new_entity)   # get the dataset using its id
    return render(
        request,
        'search_results.html',
        {"keywords": keywords,
        "dataset_name": dataset_name})



# def search_view(request):
#     if request.method == 'POST':
#         keywords = request.POST['keywords']
#         print (request.POST['keywords'])

#     return render(
#         request,
#         'search_results.html',
#         {"keywords": keywords})
