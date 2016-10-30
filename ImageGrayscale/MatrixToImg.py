from PIL import Image
import numpy

def reformatRGBMatrix(rgbMatrix):
    newMatrix = numpy.zeros((32, 32, 3), dtype=numpy.uint8)
    for j in range(0, 32):
        for k in range(0, 32):
            newMatrix[j, k] = [rgbMatrix[32*j + k][0], rgbMatrix[32*j + k][1], rgbMatrix[32*j + k][2]]
    return newMatrix

def matrixToImageColour(rgbMatrix, filePathAndName):
    newdata = reformatRGBMatrix(rgbMatrix)
    im2 = Image.fromarray(newdata, "RGB")
    im2.save(filePathAndName)

def matrixToImageGray(grayMatrix, filePathAndName):
    im = Image.fromarray(numpy.matrix(grayMatrix))
    im.convert("RGB").save(filePathAndName)
