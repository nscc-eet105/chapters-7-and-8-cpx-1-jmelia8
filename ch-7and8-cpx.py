#Joe Melia EET-107

from adafruit_circuitplayground import cp
import random
import time

def main():
    file = open("pattern.txt", "r")
    text = [file.read()]
    file.close()
    order = text.split(", ")
    pattern = []
    for num in order:
        pattern.append(int(num))
    
    while True:
        for pixel in pattern:
            cp.pixels[pixel] = pixel_color()
            time.sleep(0.25)
            cp.pixels[pixel] = (0, 0, 0)

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return(red, green, blue)
                      
main()
