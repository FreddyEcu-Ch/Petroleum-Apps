import numpy as np

from poes.model.poes import poes
#First Part - valores unicos
#%%
area=200
h=40
poro=float(0.30)
swi=float(0.20)
boi=1.12
print("El valor de POES es:",np.round(poes(area,h,poro,swi,boi),2))

#Second Part
#%%
area2=np.array([300,250,200,180,350])
espesor=np.array([50,48,55,42,60])
poros=np.array([0.42,0.40,0.38,0.35,0.45])
swi2=np.array([0.22,0.30,0.25,0.28,0.35])
boi2=np.array([1.10,1.50,1.75,1.60,1.55])
print("El valor de Poes por arreglos es de:",np.round(poes(area,espesor,poros,swi2,boi2),2))
