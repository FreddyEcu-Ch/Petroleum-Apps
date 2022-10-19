import numpy as np
from poes.model.poes import poes
#data
#First part: To use only one value for each variable.
#%%
R1= poes(100,25,15,0.20,1.20)
print(np.round(R1,2))


#Second part: To use an array of 5 values for each parameter.
#%%
area=np.array([100,150,120,200,300])
h=np.array([20,25,15,10,30])
porosity=np.array([0.2,0.15,0.3,0.18,0.25])
swi=np.array([0.2,0.18,0.15,0.12,0.21])
boi=np.array([1.2,1.3,1.4,1.8,1.1])

R2=poes(area,h,porosity,swi,boi)
print(np.round(R2,2))