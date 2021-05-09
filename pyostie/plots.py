import re
import nltk
import plotly
import wordcloud
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from pyostie.utils import *

try:
    stopwords = nltk.corpus.stopwords.words('english')
except Exception:
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
words = set(nltk.corpus.words.words('en'))


class draw:
    def __init__(self, text, figsize=None):
        self.text = text
        self.size = figsize

    def WC(self):
        plt.figure(figsize=self.size)
        if isinstance(self.text, str):
            cleaned_text = cleaning_text(self.text)
            wc = wordcloud.WordCloud(stopwords=stopwords,
                                     max_words=500,
                                     max_font_size=100,
                                     repeat=True)
            wc.generate(cleaned_text)
            plt.imshow(wc)
            plt.show()
        elif isinstance(self.text, list):
            cleaned_text = cleaning_text(self.text[0])
            wc = wordcloud.WordCloud(stopwords=stopwords,
                                     max_words=500,
                                     max_font_size=100,
                                     repeat=True)
            wc.generate(cleaned_text)
            plt.imshow(wc)
            plt.show()

    def count_plot(self):
        plt.figure(figsize=self.size)
        if isinstance(self.text, str):
            cleaned_text = cleaning_text(self.text)
            tokens = nltk.tokenize.word_tokenize(cleaned_text)
            fd = nltk.FreqDist(tokens)
            fd.plot(100, cumulative=False)
            plt.show()
        elif isinstance(self.text, list):
            cleaned_text = cleaning_text(self.text[0])
            tokens = nltk.tokenize.word_tokenize(cleaned_text)
            fd = nltk.FreqDist(tokens)
            fd.plot(100, cumulative=False)
            plt.show()
