from PyQt5.QtCore import QThread, pyqtSignal

from Operators.Crossing import EdgeCrosser
from Operators.Mutation import DisplacementMutator
from Operators.Selection import TournamentSelector
from Population import Evolution, Population

class EvolutionProcessor(QThread):
    generationProcessed = pyqtSignal(Population)
    generationProcessingFailed = pyqtSignal(Exception)

    def __init__(self, parent = None):
        QThread.__init__(self, parent)

        self.problemMap = None
        self.population = None
        self.selector = None
        self.crosser = None
        self.mutator = None

    def setProblemMap(self, problemMap):
        self.problemMap = problemMap

    def setPopulation(self, population):
        self.population = population

    def setCrosserParameters(self, parentsCount, useDepthSearch):
        self.crosser = EdgeCrosser(parentsCount, useDepthSearch)

    def setMutatorParameters(self, probability):
        self.mutator = DisplacementMutator(probability)

    def setSelectorParameters(self, tournamentSize, elitismFactor):
        self.selector = TournamentSelector(tournamentSize, elitismFactor)

    def run(self):
        evolution = Evolution(self.problemMap, self.population, self.selector, self.crosser, self.mutator)
        try:
            newPopulation = evolution.evolve()
        except Exception as e:
            self.generationProcessingFailed.emit(e)
            return

        self.generationProcessed.emit(newPopulation)
        return
