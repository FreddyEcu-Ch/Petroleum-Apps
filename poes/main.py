import numpy as np

from poes.model.poes import poes

#first part
#%%
area=200
poro=0.30
h=40
swi=0.2
boi=1.12
firstway=poes(area,h,poro,swi,boi)
print(np.round(firstway,2))
import random as rd
#second part
#%%
area1=np.array([210,190,193,212,195])
poro1=np.array([0.25,0.26,0.32,0.31,0.29])
h1=np.array([39,36,43,37,41])
swi1=np.array([0.19,0.17,0.22,0.18,0.23])
boi1=np.array([1.13,1.14,1.11,1.10,1.09])
secondway=poes(area1,h1,poro1,swi1,boi1)
print(np.round(secondway,2))

