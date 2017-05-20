#! python3
""" caption_generator.py - generates a caption, random phrase, quote, etc """
import re
import requests
from bs4 import BeautifulSoup

def get_bible_verse():
    """ gets a random verse from http://www.sandersweb.net/bible/verse.php """
    url = 'http://www.sandersweb.net/bible/verse.php'
    verse = ""

    # get the verse
    res = requests.get(url)
    res.raise_for_status()
    bible_soup = BeautifulSoup(res.text, 'html.parser')

    ref = bible_soup.select('h2')[0].getText().strip()
    content = remove_ref(bible_soup.select('.esv-text p')[0].getText().strip())

    verse = '%s [ #%s ]' % (content, ref)
    return verse

def remove_ref(content):
    """ remove the verse reference numbers from the content string """
    expression = re.compile('\d+\\xa0')
    expression2 = re.compile('\[\d+\]')
    content = ''.join(re.split(expression2, content))
    return ''.join(re.split(expression, content))
