# -*- coding: utf-8 -*-
"""Assignment-1 Text Pre-processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rjcYJ_UqukNUOj0AqMUg3z77-UoO-CjK

### Python Library Used: NLTK
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import re
import operator
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from nltk import trigrams
from nltk.stem.porter import *
from nltk.stem.wordnet import WordNetLemmatizer

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

plt.style.use('seaborn')

# One time download
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

'''
from google.colab import drive
drive.mount('/content/drive')

cd drive/My\ Drive/IR\ Assignment
'''



f = open("wiki_02", "r", encoding='utf8')
response = f.read()


"""## Corpus Statistics"""

'''
removes all non-ASCII characters from the text
'''
def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)

'''
Build a regular expression which can find all the characters “< >” in the first incidence in a text, and after that
using sub function replace all the text between those symbols with an empty string
'''
def parse_html_tags(text):
    """Remove html tags from a string"""
    
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

text = remove_non_ascii(response)

corpus = parse_html_tags(text)

# Remove punctuations from the corpus
corpus = corpus.translate(str.maketrans('', '', string.punctuation))

# split the text into tokens
tokens = nltk.word_tokenize(corpus)

"""### 1. Unigram Analysis"""

#compute frequency distribution for all the unigrams in the text

unigram_dict = {}

for token in tokens:
  if unigram_dict.get(token):
    unigram_dict[token] = unigram_dict[token] + 1
  else:
    unigram_dict[token] = 1

total_unique_ugs = len(unigram_dict)
print(total_unique_ugs)

"""(b) Plot the distribution of the unigram frequencies."""

# for k,v in unigram_dict.items():
#     print (k,v)

sorted_l = sorted(unigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig1 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Unigram Analysis', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig1.savefig('Image_1: Unigram Analysys.png')

"""(c) How many (most frequent) uni-grams are required to cover the 90% of the complete corpus."""

sorted_list = sorted(unigram_dict.items(), reverse=True, key=lambda x: x[1])

print(sorted_list)

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.9:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""### 2. Bigram Analysis

(a) Mention the total unique bigrams present in the corpus.
"""

bgs = nltk.bigrams(tokens)

fdist = nltk.FreqDist(bgs)

bigram_dict = {}

for k,v in fdist.items():
    bigram_dict[k] = v

total_unique_bgs = len(bigram_dict)
print(total_unique_bgs)

"""(b) Plot the distribution of the bigram frequencies."""

sorted_l = sorted(bigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig2 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Bigram Analysis', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig2.savefig('Image_2: Bigram Analysys.png')

"""(c) How many (most frequent) bi-grams are required to cover the 80% of the complete corpus."""

sorted_list = sorted(bigram_dict.items(), reverse=True, key=lambda x: x[1])

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.8:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""### 3. Trigram analysis:

(a) Mention the total unique trigrams present in the corpus.
"""

tgs = nltk.trigrams(tokens)

fdist = nltk.FreqDist(tgs)

trigram_dict = {}

for k,v in fdist.items():
    trigram_dict[k] = v

total_unique_tgs = len(trigram_dict)
print(total_unique_tgs)

"""(b) Plot the distribution of the trigram frequencies."""

sorted_l = sorted(trigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig3 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Trigram Analysis', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig3.savefig('Image_3: Trigram Analysys.png')

"""(c) How many (most frequent) tri-grams are required to cover the 70% of the complete corpus."""

sorted_list = sorted(trigram_dict.items(), reverse=True, key=lambda x: x[1])

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.7:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""# 4. Stemming"""

stemmer = PorterStemmer()

stemmed_tokens = [stemmer.stem(token) for token in tokens]

"""### 1. Unigram Analysis"""

#compute frequency distribution for all the unigrams in the text

unigram_dict = {}

for token in stemmed_tokens:
  if unigram_dict.get(token):
    unigram_dict[token] = unigram_dict[token] + 1
  else:
    unigram_dict[token] = 1

total_unique_ugs = len(unigram_dict)
print(total_unique_ugs)

"""(b) Plot the distribution of the unigram frequencies."""

for k,v in unigram_dict.items():
    print (k,v)

sorted_l = sorted(unigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig4 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Unigram Analysis after Stemming', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig4.savefig('Image_4: Unigram Analysys after Stemming.png')

"""(c) How many (most frequent) uni-grams are required to cover the 90% of the complete corpus."""

sorted_list = sorted(unigram_dict.items(), reverse=True, key=lambda x: x[1])

print(sorted_list)

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.9:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""### 2. Bigram Analysis

(a) Mention the total unique bigrams present in the corpus.
"""

bgs = nltk.bigrams(stemmed_tokens)

fdist = nltk.FreqDist(bgs)

bigram_dict = {}

for k,v in fdist.items():
    bigram_dict[k] = v

total_unique_bgs = len(bigram_dict)
print(total_unique_bgs)

"""(b) Plot the distribution of the bigram frequencies."""

sorted_l = sorted(bigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig5 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Bigram Analysis  after Stemming', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig5.savefig('Image_5: Bigram Analysis after Stemming.png')

"""(c) How many (most frequent) bi-grams are required to cover the 80% of the complete corpus."""

sorted_list = sorted(bigram_dict.items(), reverse=True, key=lambda x: x[1])

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.8:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""### 3. Trigram analysis:

(a) Mention the total unique trigrams present in the corpus.
"""

tgs = nltk.trigrams(stemmed_tokens)

fdist = nltk.FreqDist(tgs)

trigram_dict = {}

for k,v in fdist.items():
    trigram_dict[k] = v

total_unique_tgs = len(trigram_dict)
print(total_unique_tgs)

"""(b) Plot the distribution of the trigram frequencies."""

sorted_l = sorted(trigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig6 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Trigram Analysis after Stemming', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig6.savefig('Image_6: Trigram Analysys after Stemming.png')

"""(c) How many (most frequent) tri-grams are required to cover the 70% of the complete corpus."""

sorted_list = sorted(trigram_dict.items(), reverse=True, key=lambda x: x[1])

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.7:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""# 5. Lemmatization"""

lmtzr = WordNetLemmatizer()

lemmatized_tokens = [lmtzr.lemmatize(token) for token in tokens]

"""### 1. Unigram Analysis"""

#compute frequency distribution for all the unigrams in the text

unigram_dict = {}

for token in lemmatized_tokens:
  if unigram_dict.get(token):
    unigram_dict[token] = unigram_dict[token] + 1
  else:
    unigram_dict[token] = 1

total_unique_ugs = len(unigram_dict)
print(total_unique_ugs)

"""(b) Plot the distribution of the unigram frequencies."""

for k,v in unigram_dict.items():
    print (k,v)

sorted_l = sorted(unigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig7 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Unigram Analysis after Lemmatization', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig7.savefig('Image_7: Unigram Analysys after Lemmatization.png')

"""(c) How many (most frequent) uni-grams are required to cover the 90% of the complete corpus."""

sorted_list = sorted(unigram_dict.items(), reverse=True, key=lambda x: x[1])

print(sorted_list)

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.9:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""### 2. Bigram Analysis

(a) Mention the total unique bigrams present in the corpus.
"""

bgs = nltk.bigrams(lemmatized_tokens)

fdist = nltk.FreqDist(bgs)

bigram_dict = {}

for k,v in fdist.items():
    bigram_dict[k] = v

total_unique_bgs = len(bigram_dict)
print(total_unique_bgs)

"""(b) Plot the distribution of the bigram frequencies."""

sorted_l = sorted(bigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig8 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Bigram Analysis  after Lemmatization', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig8.savefig('Image_8: Bigram Analysis after Lemmatization.png')

"""(c) How many (most frequent) bi-grams are required to cover the 80% of the complete corpus."""

sorted_list = sorted(bigram_dict.items(), reverse=True, key=lambda x: x[1])

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.8:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""### 3. Trigram analysis:

(a) Mention the total unique trigrams present in the corpus.
"""

tgs = nltk.trigrams(lemmatized_tokens)

fdist = nltk.FreqDist(tgs)

trigram_dict = {}

for k,v in fdist.items():
    trigram_dict[k] = v

total_unique_tgs = len(trigram_dict)
print(total_unique_tgs)

"""(b) Plot the distribution of the trigram frequencies."""

sorted_l = sorted(trigram_dict.items(), key=lambda x: x[1], reverse=True)

ranks = []
freqs = []

rank = 0

for val in sorted_l:
  ranks.append(rank + 1)
  freqs.append(val[1])
  rank = rank + 1

fig9 = plt.figure()

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.title('Trigram Analysis after Lemmatization', fontsize = 20, fontweight = 'bold')

plt.grid(True)
plt.show()

fig9.savefig('Image_9: Trigram Analysys after Lemmatization.png')

"""(c) How many (most frequent) tri-grams are required to cover the 70% of the complete corpus."""

sorted_list = sorted(trigram_dict.items(), reverse=True, key=lambda x: x[1])

cnt = 1
total = sorted_list[0][1]

total_words = 0

for val in sorted_list:
  total_words = total_words + val[1]

perc = total/total_words

while perc < 0.7:
  total = total + sorted_list[cnt][1]
  cnt = cnt + 1
  perc = total/total_words

print(cnt)

"""# Collocations

## 10. Find top 20 bi-gram collocations in the text corpus using Chi-square test
"""

def chiSquare(bi, uni, word1, word2, bg, N):
  o11 = bi[bg]
  o12 = uni[word2] - o11
  o21 = uni[word1] - o11  
  o22 = N - o21 - o12 + o11

  grand_total = o11 + o12 + o21 + o22
  row1_total = o11 + o12
  row2_total = o21 + o22
  col1_total = o11 + o21
  col2_total = o12 + o22

  e11 = (row1_total * col1_total) / grand_total
  e12 = (row1_total * col2_total) / grand_total
  e21 = (row2_total * col1_total) / grand_total
  e22 = (row2_total * col2_total) / grand_total

  sum1 = ((o11 - e11)**2) / e11
  sum2 = ((o12 - e12)**2) / e12
  sum3 = ((o21 - e21)**2) / e21
  sum4 = ((o22 - e22)**2) / e22

  return sum1 + sum2 + sum3 + sum4

unigram_dict = {}

for token in tokens:
  if unigram_dict.get(token):
    unigram_dict[token] = unigram_dict[token] + 1
  else:
    unigram_dict[token] = 1

bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)

bigram_dict = {}

for k,v in fdist.items():
    bigram_dict[k] = v

chi_dict = {}

ls = list(bigram_dict.keys())

for item in ls:
  chi = chiSquare(bigram_dict, unigram_dict, item[0], item[1], item, len(tokens))
  chi_dict[item] = chi

sorted_list = sorted(chi_dict.items(), reverse=True, key=lambda x: x[1])

top20 = sorted_list[:20]

print(top20)

for item in top20:
  print(item[0])