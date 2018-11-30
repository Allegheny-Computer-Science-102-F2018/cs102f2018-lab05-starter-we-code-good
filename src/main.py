#Matt Jones, John Scott, Jon Mendez, Carson Quigley
import csv
def begin():
    print("Welcome to the text-music program: representing articles discretely through music.\n")
    filePath = input("Please paste file path to your article \".txt\" file and press enter.\n")
    #Sentiment = getSentimentMethod(getArticleString(filePath)) might need to tweak it so it's a csv instead of a string.
    length = count_letters(getArticleString(filePath))
    print("length: ", length)
    if length <= 2000:
        #method for generating a short melody, pass in sentiment as a variable
        print("short")
    elif length > 2000 and length <= 6000:
        #method for generating medium melody, pass in sentiment as a variable
        print("medium")
    else:
        #method for generating a long melody, pass in sentiment as a variable
        print("long")

def count_letters(article):
    nonLetters = [" ", ".", "?", "!", "@", "#", "$", "%", "(", ")", "/", "\\", "[", "]", "-", "+"]
    return len([letter for letter in article if letter not in nonLetters])

def getArticleString(file):
    with open(file, 'r') as myArticle:
        articleString = myArticle.read()
    return articleString

def stringToCsv(string):
    ourList = string.split()
    print(ourList)

begin()
