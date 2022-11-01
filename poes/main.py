import numpy as np
from poes.model.poes import poes
from scipy.stats import norm, lognorm, expon, triang, uniform
import matplotlib.pyplot as plt
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

#%%
# Generate random values for porosity
poro_norm = norm.rvs(loc=0.2, scale=0.05, size=1000)
poro_norm = np.where(poro_norm < 0, 0, poro_norm)
poro_norm = np.where(poro_norm > 0.4, 0.4, poro_norm)

poro_exp = expon.rvs(loc=0, scale=0.05, size=1000)
poro_exp = np.where(poro_exp < 0, 0, poro_exp)
poro_exp = np.where(poro_exp > 0.4, 0.4, poro_exp)

poro_log = lognorm.rvs(s=0.8, loc=0, scale=0.2, size=1000)
poro_log = np.where(poro_log < 0, 0, poro_log)
poro_log = np.where(poro_log > 0.4, 0.4, poro_log)

poro_trian = triang.rvs(c=0.3, loc=0, scale=0.4, size=1000)
print(poro_trian)

poro_unif = uniform.rvs(loc=0, scale=0.4, size=1000)

#%% Plot triangular distribution of porosity
plt.hist(poro_trian)
plt.show()
#%%
# Generate random values for thickness
thick_norm = norm.rvs(loc=50, scale=70, size=1000)
thick_norm = np.where(thick_norm < 0, 0, thick_norm)
thick_norm = np.where(thick_norm > 180, 180, thick_norm)

thick_exp = expon.rvs(loc=0, scale=50, size=1000)
thick_exp = np.where(thick_exp < 0, 0, thick_exp)
thick_exp = np.where(thick_exp > 180, 180, thick_exp)

thick_log = lognorm.rvs(s=0.6, loc=0, scale=40, size=1000)
thick_log = np.where(thick_log < 0, 0, thick_log)
thick_log = np.where(thick_log > 180, 180, thick_log)

thick_trian = triang.rvs(c=0.3, loc=0, scale=150, size=1000)

thick_unif = uniform.rvs(loc=0, scale=200, size=1000)

#%% Plot exponential distribution of thickness
print(thick_exp)
plt.hist(thick_exp)
plt.show()

#%% Generate random values for area
area_norm = norm.rvs(loc=190, scale=100, size=1000)
area_norm = np.where(poro_norm < 50, 50, area_norm)
area_norm = np.where(poro_norm > 1000, 1000, area_norm)

area_exp = expon.rvs(loc=50, scale=100, size=1000)
area_exp = np.where(poro_exp < 50, 50, area_exp)
area_exp = np.where(poro_exp > 1000, 1000, area_exp)

area_log = lognorm.rvs(s=0.8, loc=50, scale=100, size=1000)
area_log = np.where(area_log < 50, 50, area_log)
area_log = np.where(area_log > 1000, 1000, area_log)

area_trian = triang.rvs(c=0.3, loc=50, scale=450, size=1000)

area_unif = uniform.rvs(loc=50, scale=500, size=1000)
print(area_unif)

#%%Factor volumetrico
#Normal distribution → loc=1.5, scale=0.5, size=1000
poro_norm = norm.rvs(loc=1.5, scale=0.5, size=1000)
poro_norm = np.where(poro_norm < 0, 1, poro_norm)
poro_norm = np.where(poro_norm > 2, 2, poro_norm)

#Exponential distribution → loc=1, scale=0.2, size=1000
poro_exp = expon.rvs(loc=1, scale=0.2, size=1000)
poro_exp = np.where(poro_exp < 0, 1, poro_exp)
poro_exp = np.where(poro_exp > 2, 2, poro_exp)

#Lognoraml distribution → s=0.7, loc=1, scale=0.2, size=1000
poro_log = lognorm.rvs(s=0.7, loc=1, scale=0.2, size=1000)
poro_log = np.where(poro_log < 0, 1, poro_log)
poro_log = np.where(poro_log > 2, 2, poro_log)

#Triangular distribution → c=0.3, loc=1, scale=1, size=1000
poro_trian = triang.rvs(c=0.3, loc=1, scale=1, size=1000)

#Uniform distribution → loc=1, scale=1, size=1000
poro_unif = uniform.rvs(loc=1, scale=1, size=1000)

#%% Random values of Swi
swi_norm=norm.rvs(loc=0.4,scale=0.2,size=1000)
swi_norm=np.where(swi_norm<0,0,swi_norm)
swi_norm=np.where(swi_norm>1,1,swi_norm)

swi_exp=expon.rvs(loc=0,scale=0.2,size=1000)
swi_exp=np.where(swi_exp<0,0,swi_exp)
swi_exp=np.where(swi_exp>1,1,swi_exp)

swi_log=lognorm.rvs(s=0.8,loc=0,size=1000)
swi_log=np.where(swi_log<0,0,swi_log)
swi_log=np.where(swi_log>1,1,swi_log)

swi_trian=triang.rvs(c=0.3,loc=0,scale=1,size=1000)

print(swi_norm)