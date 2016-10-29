import Transformer
import cPickle
import numpy

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

threeDData = Transformer.reformatMatrix(data[:1000], len(data[0])/3)
grayData = Transformer.grayscaleTransformMatrix(Transformer.luminosityTransform, threeDData)
for i in range(len(grayData)):
    matrixData = Transformer.desequentialize(grayData[i], 32)