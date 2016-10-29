import Transformer
matrix = [[1, 2, 9, 2,
           2, 6, 3, 5,
           6, 5, 6, 7],
          [1, 2, 4, 4,
           5, 4, 2, 1,
           3, 3, 9, 0],
          [1, 2, 3, 0,
           5, 6, 2, 2,
           3, 7, 7, 0]]
threematrix = Transformer.reformatMatrix(matrix, len(matrix[0])/3)
twomatrix = Transformer.grayscaleTransformMatrix(Transformer.averageTransform, threematrix)
for i in range(len(twomatrix)):
    gridmatrix = Transformer.desequentialize(twomatrix[i], 2)
    print gridmatrix
    print ""