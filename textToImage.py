# coding=utf8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#To convert text to image format
def textToImage(text, fullpath, color = "#000", bgcolor = "#FFF", fontfullpath = None, fontsize = 13, leftpadding = 3, rightpadding = 3, width = 200):
	REPLACEMENT_CHARACTER = u'\uFFFD'
	NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '

	font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize)
	text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)

	lines = []
	line = u""

	print "Text to be converted: ",text
	for word in text.split():
		if word == REPLACEMENT_CHARACTER: 
			lines.append( line[1:] ) 
			line = u""
			lines.append( u"" )
		elif font.getsize( line + ' ' + word )[0] <= (width - rightpadding - leftpadding):
			line += ' ' + word
		else: 
			lines.append( line[1:] )
			line = u""

			line += ' ' + word 

	if len(line) != 0:
		lines.append( line[1:] ) #add the last line

	line_height = font.getsize(text)[1]
	img_height = line_height * (len(lines) + 1)

	img = Image.new("RGBA", (width, img_height), bgcolor)
	draw = ImageDraw.Draw(img)

	y = 0
	for line in lines:
		draw.text( (leftpadding, y), line, color, font=font)
		y += line_height

	img.save(fullpath)
	print "Image Created!!"

# text="hello\nworld"
# textToImage(text, "image.png",fontfullpath = "font.ttf")