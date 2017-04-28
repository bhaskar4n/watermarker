import os, sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
print "1. Text only"
print "2. Logo only"
print "3. Both text and logo"
choice = int(input("choose (1 or 2 or 3) : "))
path = "images/"
logo_path = "logo/"
paths = "water_marked_images"
if not os.path.exists(paths):
    os.makedirs('water_marked_images')

dirs = os.listdir(path)

if choice == 2:
    trans = int(input("Transparent level(default=100): "))
    dirs1 = os.listdir(logo_path)
    file = "logo".join(dirs1)
    lgo_pth = logo_path+file
    logo = Image.open(lgo_pth)
    lgo = logo.size

if choice == 1:
    txt = raw_input("enter water_marker text: ")
    txtsize = int(input("enter the text size(default=72): "))
    trans = int(input("Transparent level(default=100): "))
    
if choice ==3:
    txt = raw_input("enter water_marker text: ")
    txtsize = int(input("enter the text size(default=72): "))
    trans = int(input("Transparent level(default=100): "))
    dirs1 = os.listdir(logo_path)
    file = "logo".join(dirs1)
    lgo_pth = logo_path+file
    logo = Image.open(lgo_pth)
    lgo = logo.size
    

for file in dirs:
    image_path=path+file
    #a = f.append(file)
    #print a
    print image_path
    im = Image.open(image_path)
    print im.size
    if choice == 1:
        
        transparent = Image.new("RGBA", im.size)
        draw = ImageDraw.ImageDraw(transparent,"RGBA")
        font = ImageFont.truetype("arial.ttf",txtsize)
    
        a = font.getsize(txt)
        print "getsize",a

        draw.line((0, 0) + im.size, fill=(160,161,161))
        draw.line((0, im.size[1], im.size[0], 0), fill=(161,161,161))
        if choice == 1:
            #font = ImageFont.truetype("Arial.ttf",72)
            draw.text(((im.size[0]/2 - a[0]/2, im.size[1]/2)),txt,font=font,fill=(255,255,255))
            mask = transparent.convert("L").point(lambda x: min(x, trans))
            transparent.putalpha(mask)
            im.paste(transparent,None,transparent)
            print "water_marked"
            im.save("water_marked_images/WM_"+file+".jpg")
            

    elif choice == 2:
        
        masklogo = logo.convert("L").point(lambda x: min(x,trans))
        print "logo_water_marked"
        x = im.size[0]/2-lgo[0]/2
        y = im.size[1]/2-lgo[1]/2
        im.paste(logo,(x,y),masklogo)
        im.save("water_marked_images/WM_"+file+".jpg")

    if choice == 3:

        masklogo = logo.convert("L").point(lambda x: min(x,trans))
        print "logo_water_marked"
        x = im.size[0]/2-lgo[0]/2
        y = im.size[1]/2-lgo[1]/2
        im.paste(logo,(x,y),masklogo)
        #im.save("water_marked_images/WM_"+file+".jpg")
        transparent = Image.new("RGBA", im.size)
        draw = ImageDraw.ImageDraw(transparent,"RGBA")
        font = ImageFont.truetype("Arial.ttf",txtsize)
        a = font.getsize(txt)
        print "getsize",a

        draw.line((0, 0) + im.size, fill=(160,161,161))
        draw.line((0, im.size[1], im.size[0], 0), fill=(161,161,161))
        #if choice == 1:
            #font = ImageFont.truetype("Arial.ttf",72)
        draw.text(((im.size[0]/2 - a[0]/2, im.size[1]/2+lgo[1]/2)),txt,font=font,fill=(255,255,255))
        mask = transparent.convert("L").point(lambda x: min(x, trans))
        transparent.putalpha(mask)
        im.paste(transparent,None,transparent)
        print "water_marked"
        im.save("water_marked_images/WM_"+file+".jpg")
        
        

print "saving....."
t =  time.sleep(2)
print "finished"
    
    
    
    
