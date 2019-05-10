#!/usr/bin/python
import os
import subprocess
import sys
import time
import csv
import math

def round_of_rating(number):
    number_float = eval(number)
    x=number_float 
    y=math.floor(x)

    if x-y >= 0.5:
        return (y + 0.5)
    else:
        return(y)

def execute():

  stdout_file_name = "/home/amangarg/vocalcord-cpuabm-v6/stdout.txt" # location of VF-ABM output file
  stderr_file_name = "/home/amangarg/vocalcord-cpuabm-v6/stderr.txt" # location of VF-ABM error file
  
  open(stdout_file_name, 'w').close()
  open(stderr_file_name, 'w').close()
  
  Parameter_values_file_name = "Sample.txt"
  
  with open(stdout_file_name, 'a') as stdout_file:
    with open(stderr_file_name, 'a') as stderr_file:
      # location to execute VF-ABM, length of simulation time (in number of ticks), and VF-ABM configuration
      subprocess.call(["/home/amangarg/vocalcord-cpuabm-v6/bin/testRun", "--numticks", "1345" , "--inputfile" , "/home/amangarg/vocalcord-cpuabm-v6/configFiles/config_VocalFold_surgical_rat.txt", "--run_id", "0"], stdout = stdout_file, stderr = stderr_file)
      
def makeSample(input_parameters_value):
  all_parameters = open('/home/amangarg/vocalcord-cpuabm-v6/Sample_DEFAULT.txt', 'r') # location of default parameter values
  parameters = []
  reader = csv.reader(all_parameters, delimiter='\t')
  
  for i in reader:
    for f in i:
      parameters.append(float(f))

# Calibration

# Pass parameter values to parameters chosen from sensitivity analysis

  # For Neutrophils
  parameters[155] = round_of_rating(input_parameters_value[0]) # used for discrete parameters
  parameters[102] = input_parameters_value[1] # used for continuous parameters

  # For Macrophages
  parameters[147] = input_parameters_value[2]
  parameters[116] = input_parameters_value[3]

  # For Fibroblasts      
  parameters[199] = round_of_rating(input_parameters_value[4])

  # Change collagen secretion rate (default 12 hrs).
  parameters[197] = input_parameters_value[5]
  
  #Change HA Secretion Rate (default 1 hrs)
  parameters[198] = input_parameters_value[6]
  
  # Change TNF Threshold from 10
  parameters[142] = input_parameters_value[7]
  
  # Change MMP8 Threshold from 10
  parameters[143] = input_parameters_value[8]

  outputSample = open('/home/amangarg/vocalcord-cpuabm-v6/Sample.txt', 'w') # location to write parameter values
  for val in parameters:
    outputSample.write(str(val))
    outputSample.write("\t")
  outputSample.close()
                        
def main():
  input_parameters_values = []
  for candidate_values in sys.argv[1:]:
    input_parameters_values.append(candidate_values)
  # argv to capture the parameters to plug in 
  makeSample(input_parameters_values)
  
  execute()
  
if __name__ == '__main__':
    main()
