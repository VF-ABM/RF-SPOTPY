#!/usr/bin/python
import os
import subprocess
import sys
import time
import csv
import math

#def round_of_rating(number):
 # number_float = eval(number)
 # return str(round(number_float * 2) / 2)



def round_of_rating(number):
    number_float = eval(number)
    x=number_float 
    y=math.floor(x)

    if x-y >= 0.5:
        return (y + 0.5)
    else:
        return(y)

def execute():

  stdout_file_name = "/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/stdout.txt"
  stderr_file_name = "/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/stderr.txt"
  
  open(stdout_file_name, 'w').close()
  open(stderr_file_name, 'w').close()
  
  
  Parameter_values_file_name = "Sample.txt"

  
  with open(stdout_file_name, 'a') as stdout_file:
    with open(stderr_file_name, 'a') as stderr_file:
      subprocess.call(["/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/bin/testRun", "--numticks", "1345" , "--inputfile" , "/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/configFiles/config_VocalFold_surgical_rat.txt", "--run_id", "0"], stdout = stdout_file, stderr = stderr_file)
      #os.system("/home/amangarg/ABM_CALIB/vocalcord-cpuabm-v6/bin/testRun --numticks 26 --inputfile /home/amangarg/ABM_CALIB/vocalcord-cpuabm-v6/configFiles/config_VocalFold_surgical_rat.txt")

def makeSample(input_parameters_value):
  all_parameters = open('/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/Sample_DEFAULT.txt', 'r')
  parameters = []
  reader = csv.reader(all_parameters, delimiter='\t')
  
  for i in reader:
    for f in i:
      parameters.append(float(f))
    #parameters.append(line)
  #all_parameters.close()

# Recalibration

# For Neutrophils
  parameters[155] = 0.096
  parameters[102] = 5.71405737742
  parameters[38] = 2.85560786137
  parameters[163] = 5.6918973356
  parameters[180] = 2.18643165544

  parameters[154] = 78.8552944693
  parameters[152] = 14.85

# For macrophages
  parameters[147] = 1.0
  parameters[116] = 1.30718967881
  parameters[132] = 6.89056162596
  parameters[176] = 77.110119517
  parameters[158] = 1.46279239648
  parameters[157] = 0.0817485218347

  parameters[148] = 10.0
  parameters[159] = 0.0163775365385

  parameters[153] = 0.2
  # parameters[145] = 40.0

#For Fibroblasts      
  parameters[199] = 1.0
  parameters[149] = 24.0
  parameters[165] = 87.7056502581
  parameters[13] = 2.767644645
  parameters[71] = 8.444732289
  parameters[10] = 423.930178175
  parameters[109] = 67.58423113
  parameters[50] = 4.5713641191 

  parameters[161] = 5
  parameters[162] = 0.05
  parameters[163] = 5

  # Change collagen secretion rate (default 12 hrs).
  parameters[197] = 3
  #Change HA Secretion Rate (default 1 hrs)
  parameters[198] = 1
  # Change TNF Threshold from 10
  parameters[142] = 500
  # Change MMP8 Threshold from 10
  parameters[143] = 500

# # For Neutrophils
#   parameters[155] = 0.0826524463063
#   parameters[102] = 5.71405737742
#   parameters[38] = 2.85560786137
#   parameters[163] = 5.6918973356
#   parameters[180] = 2.18643165544

#  # 0.0826524463063 5.71405737742 2.85560786137 5.6918973356 2.18643165544

# # For macrophages
#   parameters[147] = 2.0
#   parameters[116] = 3.5961054536
#   parameters[132] = 7.62463365973
#   parameters[176] = 87.8485537131
#   parameters[158] = 1.64014907141
#   parameters[157] = 0.0857683793864
#   parameters[148] = 33.0
#   parameters[159] = 0.00903598809985

# # 2.0388107647 3.5961054536 7.62463365973 87.8485537131 1.64014907141 0.0857683793864 33.0031414361 0.00903598809985


# #For Fibroblasts
#   parameters[199] = 2.0
#   parameters[149] = 21.0
#   parameters[165] = 89.3274935831
#   parameters[13] = 3.00155258148
#   parameters[71] = 10.2027616595
#   parameters[10] = 418.223330147
#   parameters[109] = 73.8826855854
#   parameters[50] = 4.63300534008

# # 27.039855407 88.3551836121 2.91080295124 9.37069756712 390.428695456 67.4408635878 4.63055047287
# # 20.7340218844 89.3274935831 3.00155258148 10.2027616595 418.223330147 73.8826855854 4.63300534008

#   # Change collagen secretion rate (default 12 hrs).
#   parameters[197] = 3
#   #Change HA Secretion Rate (default 1 hrs)
#   parameters[198] = 1
#   # Change TNF Threshold from 10
#   parameters[142] = 500
#   # Change MMP8 Threshold from 10
#   parameters[143] = 500


# # Recalibration

# # For Neutrophils
#   parameters[155] = 0.075474920841
#   parameters[102] = 6.47113865353
#   parameters[38] = 2.677376646
#   parameters[163] = 6.392016104
#   parameters[180] = 2.75996494684

# # For macrophages
#   parameters[147] = 2.5
#   parameters[116] = 4.8371413081
#   parameters[132] = 6.827961674
#   parameters[176] = 82.72522507
#   parameters[158] = 1.43748823
#   parameters[157] = 0.085455088
#   parameters[148] = 31
#   parameters[159] = 0.010423045


# #For Fibroblasts
#   parameters[199] = 2.0
#   parameters[149] = 23.5
#   parameters[165] = 87.7056502581
#   parameters[13] = 2.767644645
#   parameters[71] = 8.444732289
#   parameters[10] = 423.930178175
#   parameters[109] = 67.58423113
#   parameters[50] = 4.5713641191

#   # Change collagen secretion rate (default 12 hrs).
#   parameters[197] = 3
#   #Change HA Secretion Rate (default 1 hrs)
#   parameters[198] = 1
#   # Change TNF Threshold from 10
#   parameters[142] = 500
#   # Change MMP8 Threshold from 10
#   parameters[143] = 500

  
# For macrophages

  # parameters[147] = round_of_rating(input_parameters_value[0])
  # parameters[148] = round_of_rating(input_parameters_value[1])
  # parameters[157] = input_parameters_value[2]
  # parameters[159] = input_parameters_value[3]

#   parameters[147] = 2.5
#   parameters[148] = 31.0
#   parameters[157] = 0.0854550880115
#   parameters[159] = 0.0104230445743

#   # 2.57768900607 31.3749402623 0.0854550880115 0.0104230445743

# # Calibrated
#   parameters[116] = 4.8371413081
#   parameters[165] = 87.7056502581
#   parameters[50] = 4.5713641191

#   parameters[199] = 2.0
#   parameters[149] = 23.5
#   parameters[10] = 423.930178175

#   parameters[155] = 0.075474920841
#   parameters[180] = 2.75996494684

#   # Change collagen secretion rate (default 12 hrs).
#   parameters[197] = 3
#   #Change HA Secretion Rate (default 1 hrs)
#   parameters[198] = 1
#   # Change TNF Threshold from 10
#   parameters[142] = 500
#   # Change MMP8 Threshold from 10
#   parameters[143] = 500


  #4.8371413081 87.7056502581 4.5713641191 2.84982417973 23.5230393327 423.930178175
  

  # Total Fibroblast day1
  # parameters[199] =  4.5
  # parameters[199] = round_of_rating(input_parameters_value[0])
  # parameters[149] =  10.5
# 4.73930192287 10.6522533584

  #Fibroblast Day2
  # parameters[13] = 0.433195718339
  # parameters[47] = 4.42227702886
  # parameters[181] = 6.68978868203
  # parameters[93] = 2.27227563709

  #Neutrophils day 2
  # parameters[155] = 0.075474920841
  # parameters[180] = 2.75996494684

  #Macrophages day 2
  # parameters[158] = 6.20651871811
  # parameters[157] = 0.097426616259





  # Fibroblast day1
  # parameters[199] =  17.0
  # parameters[149] =  27.0
  # parameters[10] = 1497.40229534
  # parameters[165] =  64.4058099077
  # #parameters[125] = 8.49535409671

  # #Fibroblast Day2
  # parameters[13] = 0.433195718339
  # parameters[47] = 4.42227702886
  # parameters[181] = 6.68978868203
  # parameters[93] = 2.27227563709

  # #Neutrohils day 2
  # parameters[155] = 0.075474920841
  # parameters[180] = 2.75996494684

  # #Macrophages day 2
  # parameters[158] = 6.20651871811
  # parameters[157] = 0.097426616259




  #6.20651871811 0.097426616259

  # parameters[199] = 8.0
  # parameters[149] = 93.5
  # parameters[10] = 2457.37285068
  # parameters[165] = 18.0643024013
  # parameters[125] = 8.49535409671

  # parameters[155] = 0.075474920841
  # parameters[180] = 2.75996494684


  # parameters[13] = 9.83369086141
  # parameters[47] = 2.76612445335
  # parameters[181] = 2.43290392767
  # parameters[93] = 3.4072330088
  # parameters[83] = 0.832707403642



  #8.27759284007 93.7311163774 2457.37285068 18.0643024013 8.49535409671

  #9.83369086141 2.76612445335 2.43290392767 3.4072330088 0.832707403642



  outputSample = open('/home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/Sample.txt', 'w')
  for val in parameters:
    outputSample.write(str(val))
    outputSample.write("\t")
  outputSample.close()
                        
def main():
  input_parameters_values = []
  for candidate_values in sys.argv[1:]:
    input_parameters_values.append(candidate_values)
  #do the argv to capture the parameters to plug in 
  makeSample(input_parameters_values)
  
  execute()
  
  
  
if __name__ == '__main__':
    main()

