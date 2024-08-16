from skimage import data, color
import math

### FILTER PARAMS

BLOCK_SIZE = 4
ASCII_KEY = ['  ', '..', ';;', 'cc','oo', '??', 'PP', '00', '@@','&&']

def ascii_to_text(image, output_filename):

    # change the file to greyscale

    image = color.rgb2gray(image)

    # get the image size

    image_len = len(image)
    image_width = len(image[0])

    # open the output file

    f = open(output_filename, 'w')

    # preform the main operation

    for i in range(int(image_len / BLOCK_SIZE)):
        for j in range(int(image_width / BLOCK_SIZE) ):
            avg = 0
            for x in range(BLOCK_SIZE):
                for y in range(BLOCK_SIZE):
                    avg += image[i * BLOCK_SIZE + x][j * BLOCK_SIZE + y]
            avg  = (avg / BLOCK_SIZE * BLOCK_SIZE) * 10
            f.write(ASCII_KEY[math.floor(avg)])
        f.write("\n")

    # close the output file

    f.close()

