import numpy as np
import cv2

originalimage = cv2.imread(r"D:\University\Machine Vision Repositories\imageextractor\a high quality picture of a tree.png")

new_size = (900, 900)

resizedimage = cv2.resize(originalimage , new_size , interpolation=cv2.INTER_LINEAR)
gray_image = resizedimage

originalwidth,originalheight=900,900

width , height = 300 , 300

pic1 = np.zeros((width,height,1), np.uint8)
pic2 = np.zeros((width,height,1), np.uint8)
pic3 = np.zeros((width,height,1), np.uint8)
pic4 = np.zeros((width,height,1), np.uint8)
pic5 = np.zeros((width,height,1), np.uint8)
pic6 = np.zeros((width,height,1), np.uint8)
pic7 = np.zeros((width,height,1), np.uint8)
pic8 = np.zeros((width,height,1), np.uint8)
pic9 = np.zeros((width,height,1), np.uint8)

def getneighborhood(data, y, x) : 
    neighborhood= [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    
    neighborhood[0][0]= data[y-1,x-1,2]
    neighborhood[0][1]= data[y-1,x,2]
    neighborhood[0][2]= data[y-1,x+1,2]
    neighborhood[1][0]= data[y,x-1,2]
    neighborhood[1][1]= data[y,x,2]
    neighborhood[1][2]= data[y,x+1,2]
    neighborhood[2][0]= data[y+1,x-1,2]
    neighborhood[2][1]= data[y+1,x,2]
    neighborhood[2][2]= data[y+1,x+1,2]
    
    return neighborhood

def convert_to_grayscale(input_image, height, width):
    for y in range(height):
        for x in range(width):
            red = input_image[y,x,2]
            green = input_image[y,x,0]
            blue = input_image[y,x,1]
            grayscale_value = (red*0.299) + (green * 0.587) + (blue * 0.144)
            gray_image[y,x] = [grayscale_value] * 3
     
            
    return gray_image


grayscale_image = convert_to_grayscale(resizedimage,900,900)

for y in range(1, originalheight, 3):
    for x in range(1, originalwidth, 3):
        neighborhood = getneighborhood(grayscale_image, y, x)
        
        col = (x // 3) % 300
        row = (y // 3) % 300
        
        pic1[row, col] = neighborhood[0][0]
        pic2[row, col] = neighborhood[0][1]
        pic3[row, col] = neighborhood[0][2]
        pic4[row, col] = neighborhood[1][0]
        pic5[row, col] = neighborhood[1][1]
        pic6[row, col] = neighborhood[1][2]
        pic7[row, col] = neighborhood[2][0]
        pic8[row, col] = neighborhood[2][1]
        pic9[row, col] = neighborhood[2][2]

        
cv2.imshow("originalimage",grayscale_image)
cv2.imshow("pic1",pic1)
cv2.imshow("pic2",pic2)
cv2.imshow("pic3",pic3)
cv2.imshow("pic4",pic4)
cv2.imshow("pic5",pic5)
cv2.imshow("pic6",pic6)
cv2.imshow("pic7",pic7)
cv2.imshow("pic8",pic8)
cv2.imshow("pic9",pic9)
cv2.waitKey(0)