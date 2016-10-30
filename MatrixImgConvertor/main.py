import MatrixImgConvertor
from random import randint
#from PIL import Image

matrix = []
f = open("target2.txt", "r")

lines = f.readlines()
matrix = [[int(number) for number in line.split()] for line in lines]
MatrixImgConvertor.matrixToImageColour(matrix, "image2.jpg")
f.close()