from chromosome import Chromosome
from ga import GA
from readfiles import readNetwork, readNetworkGML


def getNrCommunities(representation):
    nrCom = 0
    communities = [0 for i in range(len(representation) + 1)]
    for x in representation:
        communities[x] += 1
    for com in communities:
        if com != 0:
            nrCom += 1
    return nrCom


def main():
    #net = readNetwork("data/net.in")
    net = readNetworkGML("data/karate.gml")
    print(net['mat'])
    print(net['degrees'])
    print(net['nrNodes'])
    print(net['nrEdges'])

    dim = net['nrNodes']
    min = 1
    if dim <= 10:
        max = dim
    else:
        max = 10

    gaParams = {'dimPop': 200, 'nrGen': 100}
    problParams = {'min': min, 'max': max, 'nrDim': dim}

    ga = GA(net, gaParams, problParams)
    ga.initPopulation()
    ga.evaluatePopulation()
    maxFitness = -9999
    bestRepresentation = []
    evolutionFitness = []
    evolutionNrComm = []

    fileName_output = "data/karate_out.txt"
    f = open(fileName_output, 'w')
    for gen in range(gaParams['nrGen']):
        bestSolutionX = ga.bestChromosome().repres
        bestSolutionY = ga.bestChromosome().fitness

        evolutionFitness.append(bestSolutionY)
        evolutionNrComm.append(getNrCommunities(bestSolutionX))

        bestChromo = ga.bestChromosome()
        if bestChromo.fitness > maxFitness:
            maxFitness = bestChromo.fitness
            bestRepresentation = bestChromo.repres

        print("best chromosome in generation " + str(gen) + " is " + str(bestChromo.repres) + " with fitness = " + str(
            bestChromo.fitness))
        print("\n")

       # ga.oneGeneration()
        ga.oneGenerationElitism()

    f.write(" evolution of fitness in best chromosomes: ")
    for fit in evolutionFitness:
        f.write(str(fit) + " ")
    f.write("\n")

    f.write(" evolution of number of communities in best chromosomes: ")
    for nrcom in evolutionNrComm:
        f.write(str(nrcom) + " ")
    f.write("\n")

    f.write(" Best representation : " + str(bestRepresentation) + " with fitness = " + str(maxFitness) + "\n")
    f.write(" Nr of communities in best representation: " + str(getNrCommunities(bestRepresentation)) + "\n")
    for i in range(len(bestRepresentation)):
        f.write(str(i + 1) + " - " + str(bestRepresentation[i]))
        f.write("\n")

    f.close()


main()
