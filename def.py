#!/usr/bin/python3
import argparse
import requests
from bs4 import BeautifulSoup

def define(word):
    url = f'https://www.dictionary.com/browse/{word}'
    html_class = 'css-kg6o37 e1q3nk1v3'
    try: 
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        return soup.find(class_=html_class).text
    except:
        return 'Definition not found'

parser = argparse.ArgumentParser()
parser.add_argument("word",help="word to define")
args = parser.parse_args()
print(define(args.word))