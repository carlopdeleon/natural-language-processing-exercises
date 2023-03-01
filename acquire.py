import os
import numpy as np
import pandas as pd
from requests import get
import os
import json
from pydataset import data
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------------------------------------

def get_blog_articles():

    '''
    Scrapes Codeup blog articles.
    '''
    
    # Lists
    list_articles = []
    list_titles = []
    final_dictionary = []

    # URL
    url = 'https://codeup.com/blog/'
    
    # Header for user authentication
    headers = {'User-Agent': 'Codeup Data Science'}
    
    # Get
    response = get(url, headers=headers)
    
    # BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Article Titles
    articles = soup.find_all('a', class_='entry-featured-image-url')
    
    # For Loop for all hyperlinks
    for element in articles:
        list_articles.append(element['href'])

    # Parsing through each article
    for article in list_articles:
        
        list_content = []
        # Header
        headers = {'User-Agent': 'Codeup Data Science'}
        # Get content
        response1 = get(article, headers=headers)
        soup1 = BeautifulSoup(response1.content, 'html.parser')
        # Append Title
        final_dictionary.append({'title': soup1.find_all('h2')[0].text})
        
        for content in soup1.find_all("p"):
            list_content.append(content.get_text())
        
        final_dictionary.append({'content':' '.join(list_content)})
    
        
    return final_dictionary

#------------------------------------------------------------------------------------------------------------

def article_list_codeup():
    '''
    Retrieves list of links for Codeup's blog.
    '''

    # Get 
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    
    # BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')  

    # Filter for content
    article = soup.find_all('a', class_='entry-featured-image-url')

    # For Loop to save links into list
    articles = []
    for element in article:
        articles.append(element['href'])

    return articles



#------------------------------------------------------------------------------------------------------------

def get_blog_articles_json():
    
    '''
    Scrapes codeup blog artilces and saves it into a JSON file.
    '''

    # Check if JSON file exists
    file = 'blog_posts.json'
    
    if os.path.exists(file): 
        with open(file) as f:
            return json.load(f)
    
    # List of articles
    article_list = article_list_codeup()

    # Header to authentify
    headers = {'User-Agent': 'Codeup Data Science'}
    
    # Empty list for list of dictionarys
    article_info = []
    
    # Loop through each article and put contents into dictionary
    for article in article_list:
        
        response = get(article, headers=headers)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        info_dict = {'title': soup.find('h1').text,
                     'link': article,
                     'date_published': soup.find('span', class_='published').text,
                     'content': soup.find('div', class_='entry-content').text}
    
        article_info.append(info_dict)

    # Saves in to JSON    
    with open(file, 'w') as f:
        
        json.dump(article_info, f)
        
    return article_info    

#------------------------------------------------------------------------------------------------------------

def scrape_one_page(topic):
    
    '''
    Scrapes one page of the inshorts.com website and puts it into
    a dictionary that has keys of category, title, and content.
    '''

    base_url = 'https://inshorts.com/en/read/'
    
    response = get(base_url + topic)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = soup.find_all('span', itemprop='headline')
    
    summaries = soup.find_all('div', itemprop='articleBody')
    
    summary_list = []
    
    for i in range(len(titles)):
        
        temp_dict = {'category': topic,
                     'title': titles[i].text,
                     'content': summaries[i].text}
        
        summary_list.append(temp_dict)
    
    return summary_list

#------------------------------------------------------------------------------------------------------------

def get_news_articles(topic_list):
    
    '''
    Scrapes a variety of news articles. Must create a topic_list variable that contains the 
    category of the news article. Example: ['business','technology','sports']
    '''

    # Check if JSON file exists
    file = 'news_articles.json'
    
    if os.path.exists(file):
        
        with open(file) as f:
            
            return json.load(f)
    
    # Final List
    final_list = []
    
    # Loop through topics and extend
    for topic in topic_list:
        
        final_list.extend(scrape_one_page(topic))
    
    # Save into JSON
    with open(file, 'w') as f:
        
        json.dump(final_list, f)
    
    
    return final_list

#------------------------------------------------------------------------------------------------------------