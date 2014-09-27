# -*- coding: utf-8 -*-
# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *     

#
# PROBLEM 1
#
       
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def simulationDelayedDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,mutProb, steps,numTrials):
        finalPopulation = []
        for trial in range(numTrials):
            population = 0
            viruses = [ResistantVirus(maxBirthProb, clearProb,resistances,mutProb) for i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            
            for timestep in range(steps):
                population=patient.update()
            
            patient.addPrescription("guttagonol")
            for timestep in range(steps,steps+150):
                population=patient.update()
            finalPopulation.append(population)
        return finalPopulation
        
        
    def makeHist(finalPopulation,steps,numTrials):
        pylab.figure()
        pylab.title(str(steps) + " delay drug treatment's final population with " + str(numTrials) +"Trials")
        pylab.xlabel("Total virus population")
        pylab.ylabel("Times this total population accurs")
        pylab.hist(finalPopulation,bins = 20)
        xmin,xmax = pylab.xlim()
        ymin,ymax = pylab.ylim()
        pylab.show()
        
    makeHist(simulationDelayedDrug(100,1000,0.1,0.05,{"guttagonol": False},0.005,300,numTrials),300,numTrials)   
    makeHist(simulationDelayedDrug(100,1000,0.1,0.05,{"guttagonol": False},0.005,150,numTrials),150,numTrials)
    makeHist(simulationDelayedDrug(100,1000,0.1,0.05,{"guttagonol": False},0.005,75,numTrials),75,numTrials)
    makeHist(simulationDelayedDrug(100,1000,0.1,0.05,{"guttagonol": False},0.005,0,numTrials),0,numTrials)
#simulationDelayedTreatment(300)
  




# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def simulationTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,mutProb, steps,numTrials):
        finalPopulation = []
        for trial in range(numTrials):
            population = 0
            viruses = [ResistantVirus(maxBirthProb, clearProb,resistances,mutProb) for i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            
            for timestep in range(150):
                population=patient.update()
            
            patient.addPrescription("guttagonol")
            
            for timestep in range(150,steps+150):
                population=patient.update()
            
            patient.addPrescription("grimpex")
                
            for timestep in range(150+steps,steps+300):
                population=patient.update()
                
            finalPopulation.append(population)
        
        return finalPopulation
    
    def makeHist2(finalPopulation,steps,numTrials):
        pylab.figure()
        pylab.title(str(steps) + " after using guttagonol treatment's final population with " + str(numTrials) +"Trials")
        pylab.xlabel("Total virus population")
        pylab.ylabel("Times this total population occurs")
        pylab.hist(finalPopulation,bins = 40)
        xmin,xmax = pylab.xlim()
        ymin,ymax = pylab.ylim()
        pylab.show()
    
    makeHist2(simulationTwoDrugs(100,1000,0.1,0.05,{"guttagonol": False, 'grimpex': False},0.005,300,numTrials),300,numTrials)   
    makeHist2(simulationTwoDrugs(100,1000,0.1,0.05,{"guttagonol": False, 'grimpex': False},0.005,150,numTrials),150,numTrials)
    makeHist2(simulationTwoDrugs(100,1000,0.1,0.05,{"guttagonol": False, 'grimpex': False},0.005,75,numTrials),75,numTrials)
    makeHist2(simulationTwoDrugs(100,1000,0.1,0.05,{"guttagonol": False, 'grimpex': False},0.005,0,numTrials),0,numTrials)
#simulationTwoDrugsDelayedTreatment(300) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
