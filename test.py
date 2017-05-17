# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from scipy import signal

class image(object):
    def __init__(self, filename):
        self.filename = filename
        self.img = Image.open(filename)
        self.w, self.h = self.img.size
        self.img_array = np.array(self.img)
        
    def grayscale(self): #モノクロ画像変換
        input_pix = self.img.load()
        output_image = Image.new("L", (self.w, self.h))
        output_pix = output_image.load()

        for x, y in product(range(self.w), range(self.h)):
            r, g, b = input_pix[x, y]
            output_pix[x, y] = int(r*0.2126 + g*0.7152 + b*0.0722)
        return output_image #Image型で出力

    def laplacian(self):
        img_gray_array = np.array(self.grayscale())
        laplacian_filter =np.array([[1,1,1],[1,-8,1],[1,1,1]])
        convolved = signal.convolve2d(img_gray_array, laplacian_filter, 'same')
        return Image.fromarray(np.uint8(convolved)) #Image型を出力
    
    def gausian(self): 
        img_gray_array = np.array(self.grayscale())
        gausian_filter = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
        convolved = signal.convolve2d(img_gray_array, gausian_filter, 'same')
        return Image.fromarray(np.uint8(convolved)) #Image型を出力
            
    def image_to_ascii(self, img): #Image型で渡す
        img_array = np.array(img)
        input_pixel = img.load()
        output_image = Image.new("RGBA", (self.w, self.h), (255,255,255))
        draw = ImageDraw.Draw(output_image)
        fontsize = 5
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
    output = image.image_to_ascii(image.laplacian())
    array = np.array(output)
    #sample = image.laplacian(image.grayscale())
    #plt.imshow(np.array(image.laplacian()))
    #plt.gray()
    #plt.show()
    plt.imshow(output)

