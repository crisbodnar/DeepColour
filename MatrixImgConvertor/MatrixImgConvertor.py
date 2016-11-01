from PIL import Image
import numpy
import array

def reformatRGBMatrix(rgbMatrix):
    newMatrix = numpy.zeros((26, 26, 3), dtype=numpy.uint8)
    for j in range(0, 26):
        for k in range(0, 26):
            newMatrix[j, k] = [rgbMatrix[26*j + k][0], rgbMatrix[26*j + k][1], rgbMatrix[26*j + k][2]]
    return newMatrix

def matrixToImageColour(rgbMatrix, filePathAndName):
    newdata = reformatRGBMatrix(rgbMatrix)
    im2 = Image.fromarray(newdata, "RGB")
    im2.save(filePathAndName)

def matrixToImageGray(grayMatrix, filePathAndName):
    im = Image.fromarray(numpy.matrix(grayMatrix))
    im.convert("RGB").save(filePathAndName)

def imageGrayToMatrix(image):
    string = image.tostring()
    arr = array.array('B', string).tolist()
    matrix = []
    for i in range(0, len(arr), 3):
        matrix.append(arr[i])
    return matrix

def imageColourToMatrix(image):
    string = image.tostring()
    arr = array.array('B', string).tolist()
    matrix = [[] for i in range(len(arr)/3)]
    for i in range(0, len(arr)):
        matrix[i/3].append(arr[i])
    return matrix

def desequentialize(sqImage, nrPixels):
    matrixImage = [[] for i in range(0, nrPixels)]
    for i in range(0, nrPixels*nrPixels):
        matrixImage[i/nrPixels].append(sqImage[i])
    return matrixImage

def makeNeuralNetworkInput(grayImage):
    fInput = open("networkinput.txt", 'w')
    matrixData = desequentialize(imageGrayToMatrix(grayImage), 32)
    for j in range(3, len(matrixData) - 3):
        for k in range(3, len(matrixData[j]) - 3):
            for jSquare in range(j - 3, j + 4):
                for kSquare in range(k - 3, k + 4):
                    fInput.write(str(matrixData[jSquare][kSquare]) + " ")
            fInput.write("\n")
    fInput.close()