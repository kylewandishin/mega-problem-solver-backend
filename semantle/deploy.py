from gensim.models import KeyedVectors
from gensim.test.utils import common_texts
from gensim.models import word2vec
from scipy import spatial
import numpy as np
import gensim.downloader
import os

# Load the model (Uncomment the line you need)
# model = gensim.downloader.load('word2vec-google-news-300')
model_path = './semantle/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

words = [w for w in model.key_to_index if w[0].islower() and "_" not in w and "." not in w]

def find_similar_words(guess, semanticscore, words_to_consider = words):
    arr = {}
    for word in words_to_consider:
        similarity = abs((np.dot(model[guess], model[word])/(np.linalg.norm(model[guess])* np.linalg.norm(model[word])) * 100) - semanticscore)
        if similarity <= 0.01:
            arr[word] = similarity
    return arr

def sort_results_by_value(result):
    return dict(sorted(result.items(), key=lambda item: item[1]))

def square_rooted(x):
    return round(np.sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),4) * 100

if __name__ == '__main__':
    print(list(find_similar_words("apple", 8.82).keys()))





