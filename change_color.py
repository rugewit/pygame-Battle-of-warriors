from PIL import Image
picture = Image.open("qwe.png")
picture = picture.convert('RGBA')
# Get the size of the image
width, height = picture.size

# Process every pixel
#pix = picture.load()
#print('start',pix[0,0])
for x in range(width):
   for y in range(height):
       current_color = picture.getpixel( (x,y) )
       R,G,B,A = current_color
       if A == 0:
           continue
       #print(current_color)
       new_color = (255,G,B)
       picture.putpixel( (x,y), new_color)
       #print(picture.getpixel( (x,y) ))
picture.save('Mikita.png')