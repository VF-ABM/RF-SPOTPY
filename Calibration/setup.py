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
                     # spotpy.parameter.Uniform('Par 156',0.001,0.1),
                     # spotpy.parameter.Uniform('Par 164',0.1,10),
                     # spotpy.parameter.Uniform('Par 39',0.1,10),
                     # spotpy.parameter.Uniform('Par 100',0.0001,0.01)
                     # spotpy.parameter.Uniform('Par 148',0.5,40),
                     # spotpy.parameter.Uniform('Par 149',1,60),
                     # spotpy.parameter.Uniform('Par 158',0.001,0.1),
                     spotpy.parameter.Uniform('Par 160',0.001,0.1)


                     # spotpy.parameter.Uniform('Par 200',2.5,24)


                     # spotpy.parameter.Uniform('Par 105',0.00005,0.005),

                     # spotpy.parameter.Uniform('Par 148',0.5,40),
                     # spotpy.parameter.Uniform('Par 117',0.5,50),
                     # spotpy.parameter.Uniform('Par 133',0.1,10),
                     # spotpy.parameter.Uniform('Par 12',0.1,10),
                     # spotpy.parameter.Uniform('Par 42',0.1,10)

                     # spotpy.parameter.Uniform('Par 181',0.1,10),
                     # spotpy.parameter.Uniform('Par 210',0.01,60),
                     # spotpy.parameter.Uniform('Par 146',0.5,40),
                     # spotpy.parameter.Uniform('Par 203',0.1,10),
                     # spotpy.parameter.Uniform('Par 12',0.1,10),

                     # spotpy.parameter.Uniform('Par 177',2.5,100),
                     # spotpy.parameter.Uniform('Par 141',1,100),
                     # spotpy.parameter.Uniform('Par 168',2.5,100),
                     # spotpy.parameter.Uniform('Par 60',0.1,10),
                     # spotpy.parameter.Uniform('Par 103',0.1,10)
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

      results_file = "/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/output/Output_Biomarkers.csv"
      df = pd.read_csv(results_file)
      simulations = []

# simulations.append(df['ActivatedFibroblast'][48])
      # simulations.append(df['Fibroblast'][48])
      # simulations.append(df['ActivatedMacrophage'][48])
      # simulations.append(df['Macrophage'][48])
      # simulations.append(df['ActivatedNeutrophil'][48])
      # simulations.append(df['Neutrophil'][48])

      # simulations.append(df['ActivatedFibroblast'][96])
      # simulations.append(df['Fibroblast'][96])
      # simulations.append(df['ActivatedMacrophage'][96])
      # simulations.append(df['Macrophage'][96])
      # simulations.append(df['ActivatedNeutrophil'][96])
      # simulations.append(df['Neutrophil'][96])

      # simulations.append(df['ActivatedFibroblast'][144])
      # simulations.append(df['Fibroblast'][144])
      # simulations.append(df['ActivatedMacrophage'][144])
      # simulations.append(df['Macrophage'][144])
      # simulations.append(df['ActivatedNeutrophil'][144])
      # simulations.append(df['Neutrophil'][144])

      # simulations.append(df['ActivatedFibroblast'][240])
      # simulations.append(df['Fibroblast'][240])
      # simulations.append(df['ActivatedMacrophage'][240])
      # simulations.append(df['Macrophage'][240])
      # simulations.append(df['ActivatedNeutrophil'][240])
      # simulations.append(df['Neutrophil'][240])

      # simulations.append(df['ActivatedFibroblast'][336])
      # simulations.append(df['Fibroblast'][336])
      # simulations.append(df['ActivatedMacrophage'][336])
      # simulations.append(df['Macrophage'][336])
      # simulations.append(df['ActivatedNeutrophil'][336])
      # simulations.append(df['Neutrophil'][336])

      # simulations.append(df['ActivatedFibroblast'][672])
      # simulations.append(df['Fibroblast'][672])
      # simulations.append(df['ActivatedMacrophage'][672])
      # simulations.append(df['Macrophage'][672])
      # simulations.append(df['ActivatedNeutrophil'][672])
      # simulations.append(df['Neutrophil'][672])

      # simulations.append(df['ActivatedFibroblast'][1344])
      # simulations.append(df['Fibroblast'][1344])
      # simulations.append(df['ActivatedMacrophage'][1344])
      # simulations.append(df['Macrophage'][1344])
      # simulations.append(df['ActivatedNeutrophil'][1344])
      # simulations.append(df['Neutrophil'][1344])

      simulations.append(df['ActivatedFibroblast'][48] + df['Fibroblast'][48])
      simulations.append(df['ActivatedMacrophage'][48] + df['Macrophage'][48])
      simulations.append(df['ActivatedNeutrophil'][48] + df['Neutrophil'][48])

      simulations.append(df['ActivatedFibroblast'][96] + df['Fibroblast'][96])
      simulations.append(df['ActivatedMacrophage'][96] + df['Macrophage'][96])
      simulations.append(df['ActivatedNeutrophil'][96] + df['Neutrophil'][96])

      simulations.append(df['ActivatedFibroblast'][144] + df['Fibroblast'][144])
      simulations.append(df['ActivatedMacrophage'][144] + df['Macrophage'][144])
      simulations.append(df['ActivatedNeutrophil'][144] + df['Neutrophil'][144])

      simulations.append(df['ActivatedFibroblast'][240] + df['Fibroblast'][240])
      simulations.append(df['ActivatedMacrophage'][240] + df['Macrophage'][240])
      simulations.append(df['ActivatedNeutrophil'][240] + df['Neutrophil'][240])

      simulations.append(df['ActivatedFibroblast'][336] + df['Fibroblast'][336])
      simulations.append(df['ActivatedMacrophage'][336] + df['Macrophage'][336])
      simulations.append(df['ActivatedNeutrophil'][336] + df['Neutrophil'][336])

      simulations.append(df['ActivatedFibroblast'][672] + df['Fibroblast'][672])
      simulations.append(df['ActivatedMacrophage'][672] + df['Macrophage'][672])
      simulations.append(df['ActivatedNeutrophil'][672] + df['Neutrophil'][672])

      simulations.append(df['ActivatedFibroblast'][1344] + df['Fibroblast'][1344])
      simulations.append(df['ActivatedMacrophage'][1344] + df['Macrophage'][1344])
      simulations.append(df['ActivatedNeutrophil'][1344] + df['Neutrophil'][1344])



      # x=0
      # x=df['ActivatedMacrophage'][48] + df['Macrophage'][48]
      # # x=df['ActivatedFibroblast'][144] + df['Fibroblast'][144]
      # simulations.append(x)

      # x=0
      # x=df['ActivatedMacrophage'][96] + df['Macrophage'][96]
      # # x=df['ActivatedFibroblast'][144] + df['Fibroblast'][144]
      # simulations.append(x)

      # x=0
      # # x=df['ActivatedFibroblast'][48] + df['Fibroblast'][48]
      # x=df['ActivatedMacrophage'][144] + df['Macrophage'][144]
      # simulations.append(x)

# 3401  3595  1665  1868
# 16302 2235  20752 7995
# 1403  1250  1307  1055
# 2433  3990  552 312
# 3914  1837  359 214
# 1442  2412  186 180
# 2456  1891  252 214





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
      # observations=[3401, 3595, 1665, 1868]
      #observations=[1665, 20752, 1307]
      # observations=[3401, 3595, 500, 1665, 500, 1868, 16302, 2235, 500, 20752, 500, 7995, 1403, 1250, 500, 1307, 500, 1055, 2433, 3990, 500, 552, 500, 312, 3914, 1837, 500, 359, 500, 214, 1442, 2412, 500, 186, 500, 180, 2456, 1891, 500, 252, 500, 214]
      
      # observations=[6996, 18537, 2653]
   
      observations=[6996, 1665, 1868, 18537, 20752, 7995, 2653, 1307, 1055, 6423, 552, 312, 5751, 359, 214, 3854, 186, 180, 4347, 252, 214]
   

      sys.stdout.flush()
      return observations

    def objectivefunction(self,simulation,evaluation):
      objectivefunction= -spotpy.objectivefunctions.rmse(evaluation,simulation)  
      print (objectivefunction)
      sys.stdout.flush()
      return objectivefunction