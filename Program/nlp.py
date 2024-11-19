from multiprocessing import Queue
from typing import Callable
##NER, note: need to download both separately
from nltk.stem import PorterStemmer, WordNetLemmatizer
##LDA
import nltk, gensim
import numpy as np
import string
import time
import os

from sound_databases import keywords_to_ID_dict

def NER(corpus : str, keyword_dict : dict, convention : str ="stem", allow_substring : bool =False) -> list:
    keywords = set(keyword_dict.keys())
    resultant_tokens = []

    if allow_substring:
        stemmed_corpus = '_'.join(Tokenize(corpus))
        print(stemmed_corpus)
        for k in keywords:
            if k in stemmed_corpus:
                resultant_tokens.append(k)
    if not allow_substring: 
        tokens = Tokenize(corpus, type=convention)
        resultant_tokens = tokens.intersection(keywords)
    print(resultant_tokens)
    return (list({keyword_dict[t] for t in resultant_tokens}))

def TokenStripper(type : str) -> Callable:
    strip = lambda t : t.lower()
    if type == "stem":
        stemmer = PorterStemmer()
        strip = lambda t : stemmer.stem(t).strip().lower()
    if type == "lemma":
        lemmatizer = WordNetLemmatizer()
        strip = lambda t : lemmatizer.lemmatize(t).strip().lower()
    return strip

def StripWordTokens(tokens : str, type : str) -> set:
    strip = TokenStripper(type)
    return {strip(t) for t in tokens}

def Tokenize(corpus : str, type : str =None) -> set:
    corpus = corpus.translate(str.maketrans('', '', string.punctuation)) #removes punctuation
    tokens = corpus.split(' ')
    return StripWordTokens(tokens, type)

def NLProcesser(corpus_queue : Queue, sound_queue : Queue):
    #(i) Reads from queue, constantly outputting sound tokens

    #NER Loading + Params
    keyword_dict = keywords_to_ID_dict()
    convention = 'stem' #stem or lemma or None
    allow_substring = False

    if not allow_substring:
        strip = TokenStripper(convention)
        keyword_dict = {strip(key):ID for key,ID in keyword_dict.items()}
        #^ generates new dict with all keys stripped with same convention as corpus (later)
    if allow_substring:
        convention = None
    
    #LDA Loading + Params ...

    ##RUNNING
    while True:
        while not corpus_queue.empty():
            corpus = corpus_queue.get()

            # Skip empty text
            if not corpus: continue

            # NER - Named Entity Recognition
            NER_result = NER(corpus, keyword_dict, convention=convention, allow_substring=True)
            if NER_result: #ie. has data
                sound_queue.put(('NER',NER_result))
                # Token in form (Type, Data)
            
            # LDA ...
            # Cosine Similarity ...

if __name__ == "__main__":
    input = 'The lightning strikes my house and it all shuddered, I turned to punch the enemy behind me but after I slashed, I missed'
    print(input)
    print(NER(input, keywords_to_ID_dict(),allow_substring = True))

