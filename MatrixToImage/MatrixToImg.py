from PIL import Image
import MtI_Transformer
import numpy


def matrixToImageColour(rgbMatrix, filePathAndName):
    newdata = MtI_Transformer.reformatRGBMatrix(rgbMatrix)
    im2 = Image.fromarray(newdata, "RGB")
    im2.save(filePathAndName)

def matrixToImageGray(grayMatrix, filePathAndName)
    im = Image.fromarray(numpy.matrix(grayMatrix))
    im.convert("RGB").save(filePathAndName)
