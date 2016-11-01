import MatrixImgConvertor
#from PIL import Image

matrix = []
f = open("color2d2.txt", "r")

lines = f.readlines()
matrix = [[int(number) for number in line.split()] for line in lines]
MatrixImgConvertor.matrixToImageColour(matrix, "image2.jpg")
f.close()
