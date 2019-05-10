import spotpy
import numpy as np
import pandas as pd
import os
import sys
from random import randint
from numpy import array


class spotpy_setup(object):
    def __init__(self):

      list_to_20 = []
      list_to_60 = []
      list_to_120_p200 = []
      list_to_120_p150 = []

      for i in np.arange(1, 60.5, 0.5):
        list_to_60.append(i)
      for i in np.arange(1, 20.5, 0.5):
        list_to_20.append(i)
      for i in np.arange(3, 120.5, 0.5):
        list_to_120_p200.append(i)
      for i in np.arange(2, 120.5, 0.5):
        list_to_120_p150.append(i)


      self.params = [
                     # Example of parameter to be calibrated, and its ranges
                     spotpy.parameter.Uniform('Par 160',0.001,0.1)
                     ] 

    def parameters(self):
      sys.stdout.flush()
      return spotpy.parameter.generate(self.params)

    def simulation(self,vector):      
      x=np.array(vector)
      # Retrieve the parameters
      # Hard code command to run calibration.py
      # Add parameters to tail of calibration.py
      command = "python calibration.py"
      for var in vector:
        command = command + " " + str(var)
      os.system(command)
      print (command)
      sys.stdout.flush()

      results_file = "/home/amangarg/vocalcord-cpuabm-v6/output/Output_Biomarkers.csv" # location of VF-ABM output
      df = pd.read_csv(results_file)
      simulations = []

      # Data to calibrate- cell type(s) and time(s) (in number of ticks), e.g.
      simulations.append(df['ActivatedFibroblast'][48] + df['Fibroblast'][48])
      simulations.append(df['ActivatedMacrophage'][48] + df['Macrophage'][48])
      simulations.append(df['ActivatedNeutrophil'][48] + df['Neutrophil'][48])

      print (simulations)

      z = array(simulations)
      print(z)

      print(z[0:3])
      print(z[3:6])
      print(z[6:9])
      print(z[9:12])
      print(z[12:15])
      print(z[15:18])
      print(z[18:21])

      sys.stdout.flush()
      return simulations

    def evaluation(self):
      # Emprirical data to calibrate model with, for corresponding cell type(s) and time(s)
      observations=[3401, 3595, 1665, 1868]

      sys.stdout.flush()
      return observations

    def objectivefunction(self,simulation,evaluation):
      objectivefunction= -spotpy.objectivefunctions.rmse(evaluation,simulation)  
      print (objectivefunction)
      sys.stdout.flush()
      return objectivefunction
