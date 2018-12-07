import sentimentAnalyzer
import musicGenerator

def begin():
    print("Welcome to the text-music program: representing articles discretely through music.\n")
    filePath = input("Please paste file path to your article \".txt\" file and press enter.\n")
    sentiment = sentimentAnalyzer.doAnalysis(filePath)
    musicGenerator.genMusic(sentiment)

begin()
