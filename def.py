#!/usr/bin/python

import argparse
from bs4 import BeautifulSoup
import requests

parser = argparse.ArgumentParser()
parser.add_argument("word",help="word to define")
args = parser.parse_args()

source = requests.get(f'https://www.merriam-webster.com/dictionary/{args.word}').text
soup = BeautifulSoup(source, 'lxml')
try:
    wordDef = soup.find('span', class_='dtText').text
    print("{}".format(wordDef))
except Exception as e:
    print("definition not found\n")
