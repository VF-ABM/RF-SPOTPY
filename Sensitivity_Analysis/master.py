# Make a loop to submit jobs
import os

for i in range (1, 120):
  os.system("sqsub -q gpu -f threaded -n 4 --mpp=22g --gpp=2 -r 60m -o /home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/output_files/copper" + str(i) + ".txt" + " /home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/bin/testRun --numticks 1344  --inputfile /home/amangarg/ABM_Runf2/vocalcord-cpuabm-v6/configFiles/config_VocalFold_surgical_rat.txt --wxw 0.2 --wyw 1.0 --wzw 1.0 --run_id " + str(i));

