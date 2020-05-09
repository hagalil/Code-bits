#Program to split an image into n images by width
from PIL import Image
def split_image(image_path, n):
    image_obj = Image.open(image_path) #Image object
    file_name = image_path.split('.')[0] #takes the name of the file without the extension
    w, h = image_obj.size
    seg = w//n #Width of the segmant
    for i in range(n):
        left = seg * i
        top = 0
        right = w - (n - i - 1) * seg
        bottom = h
        im1 = image_obj.crop((left, top, right, bottom))
        im1.save("%s_split%d.jpg" % (file_name,i + 1))
    image_obj.close()
    
image_path = input("Please enter file name to split: ")
n = int(input("Please enter number of splits: "))
split_image(image_path,n)