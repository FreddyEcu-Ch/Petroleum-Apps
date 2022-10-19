import numpy as np
from poes.model.poes import poes
#%%
#First part: To use only one value for each variable.

print((np.round(poes(200,40,0.30,0.20,1.2),2)))

#Second part: To use an array of 5 values for each parameter.
#%%
area= np.array([200,210,220,230,240])
h=np.array([40,50,60,70,80])
poro=np.array([0.30,0.25,0.20,0.15,0.18])
swi=np.array([0.20,0.30,0.40,0.50,0.55])
boi=np.array([1.2,1.22,1.23,1.25,1.30])

print(np.round(poes(area,h,poro,swi,boi),2))