import os, sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
txt = raw_input("enter water_marker text: ")
path = "images/"
paths = "water_marked_images"
if not os.path.exists(paths):
    os.makedirs('water_marked_images')

dirs = os.listdir(path)

for file in dirs:
    image_path=path+file
    #a = f.append(file)
    #print a
    print image_path
    im = Image.open(image_path)
    print im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Arial.ttf",72)
    
    a = font.getsize(txt)
    print "getsize",a

    draw.line((0, 0) + im.size, fill=(161,161,161))
    draw.line((0, im.size[1], im.size[0], 0), fill=(161,161,161))
    draw.text(((im.size[0]/2 - a[0]/2, im.size[1]/2)),txt,font=font,fill=(161,161,161))
    print "water_marked"

    im.save("water_marked_images/WM_"+file+".jpg")
print "saving....."
t =  time.sleep(3)
print t
    
    
    
    
