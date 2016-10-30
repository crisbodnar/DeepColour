import Transformer
import cPickle
import numpy
import MatrixToImg

path = '../MachineLearning/cifar-10-python/cifar-10-batches-py'


def load_data(file_path):
    fo = open(file_path, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict['data']


def load_data_from_directory(path):
    from os import listdir
    from os.path import isfile, join

    # read the filenames of all the data batches
    all_files = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.startswith('data_')]

    list_of_files = []
    for file in all_files:
        list_of_files.append(load_data(file))

    # concatenate all the matrices
    return numpy.concatenate(list_of_files)


data = load_data_from_directory(path)

threeDData = Transformer.reformatMatrix(data[:6], len(data[0])/3)
grayData = Transformer.grayscaleTransformMatrix(Transformer.luminosityTransform, threeDData)
fTrain = open("train.txt", 'w')
fTarget = open("target.txt", 'w')
for i in range(len(grayData)):
    MatrixToImg.matrixToImageColour(threeDData[i], "image"+ str(i)+ ".jpg")
    matrixData = Transformer.desequentialize(grayData[i], 32)
    MatrixToImg.matrixToImageGray(matrixData, "image"+ str(i)+ ".gray.jpg")
   # for j in range(3, len(matrixData)-3):
    #    for k in range(3, len(matrixData[j])-3):
     #       for jSquare in range(j-3, j+4):
      #          for kSquare in range(k-3, k+4):
       #             fTrain.write(str(matrixData[jSquare][kSquare])+ " ")
        #    fTarget.write(str(threeDData[i][j*len(matrixData)+k][0])+ " "+
         #                 str(threeDData[i][j*len(matrixData)+k][1])+ " "+
          #                str(threeDData[i][j*len(matrixData)+k][2])+ "\n")
           # fTrain.write("\n")
fTarget.close()
fTrain.close()