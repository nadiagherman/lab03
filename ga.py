from random import randint

from chromosome import Chromosome


class GA:

    def __init__(self, net, gaParam=None, problParam=None):
        self.__gaParam = gaParam
        self.__net = net
        self.__problParam = problParam
        self.__population = []


    @property
    def population(self):
        return self.__population

    @property
    def net(self):
        return self.__net

    def fctEval(self, repres, net):
        nrNodes = net['nrNodes']
        mat = net['mat']
        degrees = net['degrees']
        nrEdges = net['nrEdges']
        M = 2 * nrEdges
        Q = 0.0
        for i in range(0, nrNodes):
            for j in range(0, nrNodes):
                if repres[i] == repres[j]:
                    Q += (mat[i][j] - degrees[i] * degrees[j] / M)
        return Q * 1 / M


    def initPopulation(self):
        for _ in range(0, self.__gaParam['dimPop']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluatePopulation(self):
        for c in self.__population:
            c.fitness = self.fctEval(c.repres, self.__net)

    def bestChromosome(self):

        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def worstChromosome(self):

        worst = self.__population[0]
        for c in self.__population:
            if c.fitness < worst.fitness:
                worst = c
        return worst

    def selection(self):
        pos1 = randint(0, self.__gaParam['dimPop'] - 1)
        pos2 = randint(0, self.__gaParam['dimPop'] - 1)
        if self.__population[pos1].fitness > self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__gaParam['dimPop']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluatePopulation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__gaParam['dimPop'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluatePopulation()
