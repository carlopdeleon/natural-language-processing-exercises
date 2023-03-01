
import pandas as pd
from requests import get
import unicodedata
import re
import json
from bs4 import BeautifulSoup

# ntlk imports
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

#------------------------------------------------------------------------------------------------------------

def basic_clean(string):
    '''
    Lower-cases everthing.
    Normalizes unicode characters.
    Replaces anything that is not a letter, number, or white-space or a single quote.
    '''
    
    # lower case all letters
    string = string.lower()
    
    # Normalize unicode characters
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # Replace anything that is not alphanumeric, white-space, or a single quote
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    
    return string

#------------------------------------------------------------------------------------------------------------

def tokenize(string):
    '''
    Tokenize every thing.
    '''
    
    # Tokenizer object
    tokenizer = ToktokTokenizer()
    
    # Tokenize all them words
    all_them_words = tokenizer.tokenize(string)
    
    return all_them_words

#------------------------------------------------------------------------------------------------------------

def stem(string):
    '''
    Gettting the stem of each word.
    '''
    
    # Stemmer object
    ps = nltk.porter.PorterStemmer()
    
    # Stem the words
    stems = [ps.stem(word) for word in string.split()]
    stemmed = ' '.join(stems)
    
    return stemmed

#------------------------------------------------------------------------------------------------------------

def lemmatize(string):
    '''
    Lemmatize the words.
    '''
    
    # Lemmetizer Object
    wnl = nltk.stem.WordNetLemmatizer()
    
     # Stem the words
    lemon = [wnl.lemmatize(word) for word in string.split()]
    lemons = ' '.join(lemon)
    
    return lemons

#------------------------------------------------------------------------------------------------------------

def remove_stopwords(string):
    
    '''
    Removes English stop words.
    '''
    
    # English stop words
    stopword_list = stopwords.words('english')
    
    # String that will have stop words removed.
    words = string
    
    # Remove stop words and join
    words_removed = [word for word in words.split() if word not in stopword_list]
    words_removed = ' '.join(words_removed)
    
    return words_removed
    
#------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------