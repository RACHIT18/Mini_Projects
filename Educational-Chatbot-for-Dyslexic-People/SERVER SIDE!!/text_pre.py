#!/usr/bin/python
import sys
import string
import nltk
import re
import wordninja
import spacy
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from textblob import TextBlob

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def main1():
    input_str=sys.argv[1]
    input_str = input_str.lower()
    input_str = input_str.strip()
    print(input_str)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    no_punct = ""
    for char in input_str:
        if char not in punctuations:
            no_punct = no_punct + char

    input_str=no_punct
    print(input_str)
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(input_str)
    input_str = [i for i in tokens if not i in stop_words]
    print (input_str)
    input_str2=[]
    for i in range(0,len(input_str)):
        l=[]
        l=wordninja.split(input_str[i])
        if len(l)>1:
            for j in l:
                input_str2.append(j)
        else:
            input_str2.append(l[0])
    
    input_str=input_str2

    input_str=f7(input_str)
    input_str=' '.join(input_str)

    nlp = spacy.load('en_core_web_sm') 
  
    sentence = input_str
  
    doc = nlp(sentence) 
  
    for ent in doc.ents: 
        print(ent.text, ent.label_)

    lemmatizer=WordNetLemmatizer()
    
    input_str=word_tokenize(input_str)
    print(input_str)
    for i in range(len(input_str)):
        input_str[i]=lemmatizer.lemmatize(input_str[i])
    
    input_str=' '.join(input_str)
    result = TextBlob(input_str)
    print(result.tags)

    reg_exp = "NP: {<DT>?<JJ>*<NN>}"
    rp = nltk.RegexpParser(reg_exp)
    result = rp.parse(result.tags)
    print(result)

    result.draw()
    
    print(input_str)
    return input_str


if __name__ == '__main__':
    main1()