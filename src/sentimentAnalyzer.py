#Matt Jones, John Scott, Jon Mendez, Carson Quigley
#sentiment analysis engine
import sys
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def word_feats(words):
    return dict([(word, True) for word in words])
#done

def gen_classifier():
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')

    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

    negcutoff = int(len(negfeats)*3/4)
    poscutoff = int(len(posfeats)*3/4)

    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]

    return NaiveBayesClassifier.train(trainfeats)
#done

args = sys.argv
nltk.download('movie_reviews')

inputfile = args[0]
classifier = gen_classifier()
classifier.classify(inputfile)
