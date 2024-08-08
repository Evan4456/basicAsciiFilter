from skimage import data, color
import math

image = data.astronaut()

grey_scalled_image = color.rgb2gray(rocket)

print(grey_scalled_rocket[0][0])

ascii_key = ['  ', '..', ';;', 'cc','oo', '??', 'PP', '00', '@@','&&']

image_len = 300
image_width = 451

filename = 'output_image.txt'

f = open(filename, 'w')

for i in range(int(image_len / 4)):
    for j in range(int(image_width / 4) ):
        avg = 0
        for x in range(4):
            for y in range(4):
                avg += grey_scalled_image[i * 4 + x][j * 4 + y]
        print(avg)
        avg  = (avg / 16) * 10
        print(avg)
        f.write(ascii_key[9 - math.floor(avg)])
    f.write("\n")
