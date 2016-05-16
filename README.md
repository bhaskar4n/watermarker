watermarker
===========
### To fix this error,please add truetype font path 
```python
 File "watermark.py", line 58, in <module>
    font = ImageFont.truetype("DroidSansMono.ttf",txtsize)
  File "/usr/lib/python2.7/dist-packages/PIL/ImageFont.py", line 228, in truetype
    return FreeTypeFont(font, size, index, encoding)
  File "/usr/lib/python2.7/dist-packages/PIL/ImageFont.py", line 131, in __init__
    self.font = core.getfont(font, size, index, encoding)
IOError: cannot open resource
```
##note: linux users, please add truetype font path 
``` python
font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansMono.ttf",txtsize)
```
##### water marker for images

requirements: python 2.7 and PIL(Python image library)

create a folder(images) to  put all your images inside the folder (Don't change the name of the folder)

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/one.PNG"/>

images inside the folder(images)

<img src ="https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/two.PNG"/>

if you want to add logo watermark. create logo folder(don't change name of the folder)

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/15.PNG"/>

logo image inside the logo folder

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/16.PNG"/>

next double click the watermark.py python file and enter the choice

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/10.PNG"/>

processing 

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/five.PNG"/>

water marked images folder created to store the water marked images

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/six.PNG"/>

sample water marked image with text only 

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/seven.PNG"/>

sample water marked image with logo only

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/11.PNG"/>

sample water marked image with both logo and text

<img src = "https://raw.githubusercontent.com/bhaskar4n/watermarker/master/screen%20shots/12.PNG"/>


for more sample images click water_marked_samples folder

Reference : http://www.pythonware.com/media/data/pil-handbook.pdf
