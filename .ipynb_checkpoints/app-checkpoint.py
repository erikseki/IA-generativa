# libs básicas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# lib para IA Generativa 
from transformers import pipeline
from pysentimiento import create_analyzer 

# libs para NLP 
import re 
import unicodedata
import nltk 
from nltk.corpus import stopwords 

# lib para nuvem de palavras
from wordcloud import WordCloud 

# lib para pipeline de modelo + serialização de modelo
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv('comments_amazon.csv', sep=',') 
print(df.head())