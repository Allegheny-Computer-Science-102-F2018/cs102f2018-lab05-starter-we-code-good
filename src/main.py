import sentimentAnalyzer.py
import musicGenerator.py

def begin():
    print("Welcome to the text-music program: representing articles discretely through music.\n")
    filePath = input("Please paste file path to your article \".txt\" file and press enter.\n")
    sentiment = doAnalysis(filePath)
    genMusic(sentiment)

#not sure what this does so I commented it out for now.

#def count_letters(article):
#    nonLetters = [" ", ".", "?", "!", "@", "#", "$", "%", "(", ")", "/", "\\", "[", "]", "-", "+"]
#    return len([letter for letter in article if letter not in nonLetters])

#def getArticleString(file):
#    with open(file, 'r') as myArticle:
#        articleString = myArticle.read()
#    return articleString

#def stringToCsv(string):
#    ourList = string.split()
#    print(ourList)

begin()
