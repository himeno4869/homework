# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

class image(object):
    def __init__(self, filename):
        self.filename = filename
        self.img = Image.open(filename)
        self.w, self.h = self.img.size
        
    def grayscale(self):
        input_pix = self.img.load()
        output_image = Image.new("L", (self.w, self.h))
        output_pix = output_image.load()

        for x, y in product(range(self.w), range(self.h)):
            r, g, b = input_pix[x, y]
            output_pix[x, y] = int(r*0.2126 + g*0.7152 + b*0.0722)
        return output_image
            
    def image_to_ascii(self, img):
        img_array = np.array(img)
        input_pixel = img.load()
        output_image = Image.new("RGBA", (self.w, self.h), (255,255,255))
        draw = ImageDraw.Draw(output_image)
        fontsize = 8
        character = ''
        for y in range(0, self.h, fontsize):
            line = []
            for x in range(0, self.w, fontsize):
                r, g, b = input_pixel[x, y]
                gray = r*0.2126 + g*0.7152 + b*0.0722
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
        return output_image
    

if __name__ == "__main__":
    filename = 'utaeroastrologo.png'
    image = image(filename)
    output = image.image_to_ascii(image.img)
    array = np.array(output)
    plt.imshow(array)


