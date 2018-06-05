import numpy as np
import imageio
import matplotlib.pyplot as plt



#Recieves the original image, one binary image and the depth of the information.
def binaryinRGB (original, binary, bit):
    output = np.copy(original)
    binary_n = np.zeros(binary.shape)
    #Black is represented by 0 and white by 1
    binary_n[binary == 255] = 1

    for i in range(binary.shape[0]):
        for j in range(binary.shape[1]):
            value_bit = output[i][j] >> bin
            #Verifies if the value on the depth informed is wrong
            if value_bit & 1 != binary_n[i][j]:
                #Adds 2 ^ depth to the result so the desired bit changes from 0 to 1
                if binary_n[i][j] == 1:
                    output[i][j] += 1 << bit
                #Subtracts 2 ^ depth to the result so the desired bit changes from 1 to 0
                else:
                    output[i][j] -= 1 << bit
    return output


def greyscaleinRGB ():

    pass


def rmse ():
    pass


def main ():
    original = imageio.imread("choque.jpg")
    binary = imageio.imread("boquetitos.jpg")
    grey = imageio.imread("Belchior.jpg")

    binaryout = binaryinRGB(original, binary, 1)
    greyout = greyscaleinRGB(original, grey)

    rmse()


if __name__ == '__main__':
    main()
