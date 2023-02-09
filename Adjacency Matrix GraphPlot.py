#Adjacency Matrix Plot

#Adjacency Matrix
def makenodes():
    num = int(input("How many nodes: "))
    matrix = [[" " for i in range(num)] for l in range(num)]
    return matrix , num

def printmatrix(matrix):
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
                    if val == "":
                        val = " "

                    matrix[x][i] = val
                    matrix[i][x] = val

                    printmatrix(matrix)

    return matrix


matrix, num = makenodes()
populmatrix(matrix)

print("Done")
#Visual Graph
import matplotlib.pyplot as plt
import networkx as nx



def createnodes(num):
    G = nx.Graph()
    for i in range(num):
        #print("Name of the number",i+1,"node: ")
        #val = int(input())
        G.add_node(i+1)

    return G

def connectnodes(Graph,matrix):
    x = -1
    for row in matrix:
        x += 1
        for i in range(len(row)):
            if x != i:
                snode = x+1
                enode = i+1
                weights = int(matrix[x][i])
                Graph.add_edge(snode,enode,weight=weights)


    return Graph

Graph = createnodes(num)
G = connectnodes(Graph,matrix)

pos = nx.spring_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()