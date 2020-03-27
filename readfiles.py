import networkx as nx



def readNetwork(filename):

    net = {}
    f = open(filename, "r")
    nr = int(f.readline())
    net['nrNodes'] = nr
    matAdiacenta = []
    nrEdges = 0
    degrees = []
    for i in range(nr):
        matAdiacenta.append([])
        line = f.readline()
        elements = line.split(' ')
        for j in range(nr):
            matAdiacenta[i].append(int(elements[j]))
    net['mat'] = matAdiacenta

    f.close()

    for i in range(nr):
        k = 0
        for j in range(nr):
            if (matAdiacenta[i][j] == 1):
                k += 1
            if (j > i and matAdiacenta[i][j] ==1):
                nrEdges += 1

        degrees.append(k)


    net['degrees'] = degrees
    net['nrEdges'] = nrEdges
    return net


# citire fisier tip GML

def readNetworkGML(filename):
    net={}
    f = nx.read_gml(filename,label="id")
    n = len(f.nodes())
    net['nrNodes'] = n
    matAdiacenta = []

    print(f.nodes)
    print(f.edges)

    for i in range(n):
        line = [0 for j in range(n)]
        matAdiacenta.append(line)

    all_nodes = list(f.nodes())

    for edge in f.edges():
        # print(all_nodes.index(edge[0]))
        # print(all_nodes.index(edge[1]))
        matAdiacenta[all_nodes.index(edge[0])][all_nodes.index(edge[-1])] = 1

    net['mat'] = matAdiacenta
    nrEdges=0
    degrees=[]

    for i in range(n):
        k = 0
        for j in range(n):
            if (matAdiacenta[i][j] == 1):
                k += 1
            if (j > i):
                nrEdges += 1

        degrees.append(k)

    net['degrees'] = degrees
    net['nrEdges'] = nrEdges
    return net












