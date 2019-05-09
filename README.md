# VF-ABM-RF-SPOTPY

Sensitivity analysis and calibration for a vocal fold agent-based model (VF-ABM) of surgical injury and repair

## Description

Random Forest (RF) was used as a sensitivity analysis method to identify the most influential model parameters. Statistical Parameter Optimization Tool for Python (SPOTPY) was used to calibrate the parameter values to match the ABM-simulation data with corresponding empirical data from Day 1 to Day 5 following surgery. 

The intended application for this sensitivity analysis and calibration code was the [VF-ABM](https://github.com/VF-ABM/hpc-abm-vf-version_0_6).

### Papers 

Further discussion can be found in the relevant article in [Applied Sciences](https://www.mdpi.com/journal/applsci). 

## Requirements

* Matlab 
* R
* Python

### Dependencies

* [SciPy](https://www.scipy.org/)
* [SPOTPY](https://pypi.org/project/spotpy/)

#### Installation

Use the package manager [pip](https://pypi.org/project/spotpy/) to install SPOTPY.

```bash
pip install spotpy
```

There are various [ways](https://www.scipy.org/install.html) to install SciPy. 

## Getting Started

### Sensitivity analysis using Random Forest

Sample Generation
1. Run *sample_generate.m* on MATLAB.
2. Run *generate.m* on MATLAB. 

Model Execution
1. Save generated sample files. See "Sample_Inputs.zip" for an example.
2. Run model with sample files as input. To execute automatically, use *master.py*.
3. Export outputs from model.

Data Preprocessing
1. Import outputs from model into MATLAB.
2. Run *Output_process.m* on MATLAB. 
3. Run *Input_process.m* on MATLAB. 

Random Forest
1. Run *Random Forest.r* on R. 

### Calibration using SPOTPY

1. Choose number of iterations in *spot.py*.
2. Choose location of execution and parameters to be calibrated in *calibration.py*.
3. Choose location of execution and parameters to be calibrated in *setup.py*.
4. Run *spot.py* on Python.
