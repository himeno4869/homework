# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from scipy import signal

class image(object):
    
    image_shape = (256,256)    
    
    def __init__(self, filename):
        self.filename = filename
        self.img = Image.open(filename)
        self.w, self.h = self.img.size
        self.img_array = np.array(self.img)
        
    def grayscale(self): #モノクロ画像変換
        input_pix = self.img.load()
        output_image = Image.new("L", (self.w, self.h))
        output_pix = output_image.load()
        if self.img_array.shape[2] < 3:
            return self.img
        elif 3 < self.img_array.shape[2]:
            for x, y in product(range(self.w), range(self.h)):
                r, g, b, n = input_pix[x, y]
                output_pix[x, y] = int(r*0.2126 + g*0.7152 + b*0.0722)
            return output_image #Image型で出力
        else:
            for x, y in product(range(self.w), range(self.h)):
                r, g, b = input_pix[x, y]
                output_pix[x, y] = int(r*0.2126 + g*0.7152 + b*0.0722)
            return output_image #Image型で出力
            
    def resize(self,img):
        img = img.resize(self.image_shape, Image.ANTIALIAS)
        data = np.asarray(img)
        return data

    def laplacian(self): #ラプラシアンフィルター
        img_gray_array = np.array(self.grayscale()) #グレースケールにした画像を渡す
        laplacian_filter =np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        convolved = signal.convolve2d(img_gray_array, laplacian_filter, 'same')
        return Image.fromarray(np.uint8(convolved)) #Image型を出力
        
    def laplacian_55(self): #ラプラシアンフィルター5*5
        img_gray_array = np.array(self.grayscale())
        laplacian_filter =np.array([[-1,-3,-4,-3,-1], [-3,0,6,0,-3],[-4,6,20,6,-4],[-3,0,6,0,-3],[-1,-3,-4,-3,-1]])
        convolved = signal.convolve2d(img_gray_array, laplacian_filter, 'same')
        return Image.fromarray(np.uint8(convolved)) #Image型を出力
    
    def gausian(self):  #ガウシアンフィルター
        img_gray_array = np.array(self.grayscale())
        gausian_filter = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
        convolved = signal.convolve2d(img_gray_array, gausian_filter, 'same')
        return Image.fromarray(np.uint8(convolved)) #Image型を出力
            
    def gradient(self):
        img_gray_array = np.array(self.grayscale())
        gradient_filter = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        convolved = signal.convolve2d(img_gray_array, gradient_filter, 'same')
        return Image.fromarray(np.uint8(convolved)) #Image型を出力

    def image_to_ascii(self, img): #Image型で渡す
        img_array = np.array(img)
        input_pixel = img.load()
        output_image = Image.new("RGBA", (self.w, self.h), (255,255,255))
        draw = ImageDraw.Draw(output_image)
        fontsize = 6
        character = ''
        for y in range(0, self.h, fontsize):
            line = []
            for x in range(0, self.w, fontsize):
                gray = input_pixel[x, y]
                if gray > 250:
                    character = " "
                elif gray > 230:
                    character = "`"
                elif gray > 200:
                    character = ":"
                elif gray > 175:
                    character = "*"
                elif gray > 150:
                    character = "+"
                elif gray > 125:
                    character = "#"
                elif gray > 50:
                    character = "W"
                line.append(character)
            draw.text((0, y), "".join(line), fill="#000000")
            print("".join(line), end='\n')
        return output_image #Image型で出力
    

if __name__ == "__main__":
    filename = 'utaeroastrologo.png'
    image = image(filename)
    output = image.image_to_ascii(image.gradient())
    array = np.array(output)
    #plt.imshow(np.array(image.gradient()))
    #plt.gray()
    #plt.show()
    plt.imshow(output)

