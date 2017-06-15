#main

from generateMovieQuote import generateMovieQuote
from textToImage import textToImage
from postImageToTwitter import postImageToTwitter,authenticateCredentials

def main():
	imagePath = "image.png"
	text=generateMovieQuote()
	textToImage(text, imagePath,fontfullpath = "font.ttf")
	postImageToTwitter(imagePath)
	print "Success!"

main()	