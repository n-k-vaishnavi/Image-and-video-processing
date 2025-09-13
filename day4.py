from PIL import Image,ImageDraw,ImageFont
import random
img = Image.open("joshua_hong.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Anton-Regular.ttf",30)
captions = ["Ulgo shipji anha ", "Privacy jigeum", "My name is V. I am a good boy!"]
caption = random.choice(captions)
img_width , img_height = img.size
bbox = draw.textbbox((0,0),caption,font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] -  bbox[1]
x = (img_width - text_width) / 2
y = img_height - text_height - 20
outline_range = 2
for ox in range (-outline_range,outline_range+1):
    for oy in range (-outline_range,outline_range+1):
        draw.text((x+ox , y+oy), caption , font=font, fill = "black")
draw.text((x,y),caption,font=font, fill="white")
img.save("joshua_meme.jpg")        