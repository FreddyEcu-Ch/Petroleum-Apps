import numpy as np
from poes.model.poes import poes
#firstpart
area=200
poro=0.3
h=40
swi=0.2
boi=1.12
print(np.round(poes(area,poro,h,swi,boi)),2)

#%%
#secondpart
area=np.array([200,220,270,300,320])
poro=np.array([0.3,0.25,0.22,0.40,0.15])
h=np.array([40,45,35,30,50])
swi=np.array([0.2,0.15,0.25,0.3,0.35])
boi=np.array([1.12,1.15,1.20,1.25,1.27])
print(np.round(poes(area,poro,h,swi,boi)),2)
