import csv, sys, re

def readDict(somefile):
    words = {}
    with open(somefile, newline='') as somefile:
        reader = csv.reader(somefile, delimiter=',')
        for row in reader:
            words[row[0]] = row[1]
        return words
#end

def getFile(filename):
    data = ""
    try:
        datafile = open(filename, 'r')
        data = datafile.read()
    except FileNotFoundError:
            print ( "ERROR: File Not Found", filename )
            exit()

    data = data.lower()
    unwanted = "!`':,?/()/\\"
    for i in unwanted:
        data = data.replace(i, " ")
    return data.split()
#end

def getSentiment(words, dictionary):
    rank = 0
    real_words = 0
    for i in words:
        try:
            wordrank = int(dictionary[i])
            rank = rank + wordrank
            real_words = real_words + 1
        except KeyError:
            pass
        return rank
#end

def doAnalysis(inputfile):
    words = getFile(inputfile)
    dictionary = readDict("input/finn.csv")
    rank = getSentiment(words, dictionary)
    if rank >= 0:
        return "happy"
    elif rank < 0:
        return "sad"
#end
doAnalysis('input/article.txt')
