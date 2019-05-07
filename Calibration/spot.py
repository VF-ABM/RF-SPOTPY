import spotpy
from setup import spotpy_setup

results=[]
spotpy_setup=spotpy_setup()
rep=5

sampler=spotpy.algorithms.rope(spotpy_setup,  dbname='RosenROPE',  dbformat='csv')
results.append(sampler.sample(rep))

sys.stdout.flush()
