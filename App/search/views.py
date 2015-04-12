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
from django.views.generic.base import TemplateView
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


class HomePage(CreateView):
    template_name = "index.html"
    model = ContactUs
    fields = ['name', 'subject', 'message', 'email']
    success_url = "https://www.google.com"


def dataset_list_view(request):
    #returns all datasets we have.
    datasets = {}  # get datasets
    return render(
        request,
        'search_results.html',
        {"datasets": datasets})


def dataset_detail_view(request, dataset_id):
    # get the specific dataset by id
    keywords = dataset_id  # get the dataset using its id
    return render(
        request,
        'search_results.html',
        {"keywords": keywords})

# def search_view(request):
#     if request.method == 'POST':
#         keywords = request.POST['keywords']
#         print (request.POST['keywords'])

#     return render(
#         request,
#         'search_results.html',
#         {"keywords": keywords})
