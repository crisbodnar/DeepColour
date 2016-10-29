#applies lightness transformation
def lightnessTransform(red, green, blue):
    return (max(red, green, blue) + min(red, green, blue))/2

#applies average transformation
def averageTransform(red, green, blue):
    return (red + green + blue)/3

#applies luminosity transformation
def luminosityTransform(red, green, blue):
    return int(0.21*red + 0.72*green + 0.07*blue)

#applies the chosen transformation to the chosen matrix
def grayscaleTransformMatrix(transformMethod, imageMatrix):
    finalMatrix = [[]for i in range(len(imageMatrix))]
    for i in range(len(imageMatrix)):
        for j in range(len(imageMatrix[i])):
            finalMatrix[i].append(transformMethod(imageMatrix[i][j][0], imageMatrix[i][j][1], imageMatrix[i][j][2]))
    return finalMatrix

#returns the 3D version of the 2D image matrix
def reformatMatrix(twoDMatrix, nrPixels):
    threeDMatrix = [[[] for i in range(0, nrPixels)] for i in range(len(twoDMatrix))]
    for i in range(len(twoDMatrix)):
        for j in range(0, nrPixels):
            threeDMatrix[i][j].append(twoDMatrix[i][j])
            threeDMatrix[i][j].append(twoDMatrix[i][j+nrPixels])
            threeDMatrix[i][j].append(twoDMatrix[i][j+(nrPixels*2)])
    return threeDMatrix

#makes a grayscale image matrix from a sequentialized greyscale image matrix (1D -> 2D)
def desequentialize(sqImage, nrPixels):
    matrixImage = [[] for i in range(0, nrPixels)]
    for i in range(0, nrPixels*nrPixels):
        matrixImage[i/nrPixels].append(sqImage[i])
    return matrixImage
