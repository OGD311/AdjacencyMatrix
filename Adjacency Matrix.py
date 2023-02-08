#Adjacency Matrix

def makenodes():
    num = int(input("How many nodes: "))
    matrix = [[" " for i in range(num)] for l in range(num)]
    return matrix

def printmatrix(matrix):
    rowp = ""
    for row in matrix:
        print(row)


def populmatrix(matrix):
    x = -1
    for row in matrix:
        x += 1
        for i in range(len(row)):
            if x != i:
                if matrix[x][i] == " ":
                    print("Value for row",x,"column",i+1)
                    val = input()
                    matrix[x][i] = val
                    matrix[i][x] = val
    
                    printmatrix(matrix)

    return matrix


populmatrix(makenodes())


