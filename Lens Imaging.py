# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:22:48 2022

@author: Jayden Maree

Thin Lens Imaging System:
    This program simulates a simple imaging system, predicting both location and 
    magnification of an object's image. This is based on on a Khan Academy video
    and will be used to better understand the nature of imaging focal lengths on position 

* All equations are based on the thin lens approximation       
"""

#Object ---- Converging ---- Diverging ---- Eye

def dImage (f, do):
    di = 1/(1/f - 1/do)
    return di

def Mag (di,do):
    M = abs(-di/do) #should be negative for image direction, but right now I just want magnitude
    #wont run with negative M values - w1 and w2 ranges require positive values
    return M

# #Lets say fConverging is 12cm, fDiverging is 10cm, and length C-D is 33cm
# #Object is 36cm from Converging center.
# object1 = 24
# f1 = 12
# l1 = object1 + f1
# lCD = 33
# f2 = -10 #negative because diverging

# lprime1 = dImage(f1,l1)
# Mag1 = Mag(lprime1,l1)

# object2 = lCD - lprime1
# # l2 = object2 + f2  #This was incorrect to use below. 
# l2 = object2
# lprime2 = dImage(f2,l2)
# Mag2 = Mag(lprime2,l2)

# print(lprime1, Mag1, lprime2, Mag2)

"The above works and is simple, now lets add sliders and visualize, and graph."
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

f1 = 12
f2 = -10 #negative because diverging
ObjectToLens1 = 36
ObjectToLens2 = 69
w0 = 30

def System(ObjectToLens1,ObjectToLens2):
    
    lprime1 = dImage(f1,ObjectToLens1) #technically, ObjectToLPrime1
    Mag1 = Mag(lprime1,ObjectToLens1)
    
    Object2ToLens2 = ObjectToLens2 - (ObjectToLens1 + lprime1)
    lprime2 = dImage(f2,Object2ToLens2)
    Mag2 = Mag(lprime2,Object2ToLens2)
    
    w1 = w0*Mag1
    w2 = w1*Mag2
    return [lprime1,w1,lprime2,w2] 

[lprime1,w1,lprime2,w2] = System(ObjectToLens1,ObjectToLens2)
# x = list(range(0,101)) 
# y = [10]*101

lens1y = list(range(0,15)) #scale: 15 cm 
lens1x = [ObjectToLens1]*len(lens1y)
lens2y = list(range(0,15)) #scale: 15 cm
lens2x = [ObjectToLens2]*len(lens2y)


#could center waists vertically
waist0y = list(np.linspace(0,w0)) 
waist0x = [0]*len(waist0y)       # Location set to 0 meter
waist1y = list(np.linspace(0,w1)) 
waist1x = [ObjectToLens1 + lprime1]*len(waist1y) 
waist2y = list(np.linspace(0,w2)) 
waist2x = [ObjectToLens2 + lprime2]*len(waist2y)

fig, ax = plt.subplots(dpi = 200)
plt.subplots_adjust(left =0.1, bottom = 0.35)

lens1plot, = plt.plot(lens1x, lens1y, linewidth = 2, color = 'blue')
lens2plot, = plt.plot(lens2x, lens2y, linewidth = 2, color = 'blue')
waist0plot, = plt.plot(waist0x, waist0y, linewidth = 2, color = 'red')
waist1plot, = plt.plot(waist1x, waist1y, linewidth = 2, color = 'green')
waist2plot, = plt.plot(waist2x, waist2y, linewidth = 2, color = 'purple')
plt.axis([-1,100,0,40])



axSlider1 = plt.axes([0.1, 0.2, 0.8, 0.05])
slder1 = Slider(axSlider1, 'Lens 1', valmin=0, valmax=100, valinit = ObjectToLens1)
axSlider2 = plt.axes([0.1, 0.1, 0.8, 0.05])
slder2 = Slider(axSlider2, 'Lens 2', valmin=0, valmax=100, valinit = ObjectToLens2,
                slidermin = slder1)
slder1 = Slider(axSlider1, 'Lens 1', valmin=0, valmax=100, valinit = ObjectToLens1,
                slidermax = slder2)
"cant figure out a better way to two-way sliders"

def val_update(val):
    x1val = slder1.val
    lens1plot.set_xdata(x1val)
    x2val = slder2.val
    lens2plot.set_xdata(x2val)
    
    [lprime1,w01,lprime2,w02]= System(x1val,x2val)
  
    waist1plot.set_xdata(lprime1 + x1val) #continue here
    # print(w01)
    waist1plot.set_ydata(list(np.linspace(0,w01)))
    waist2plot.set_xdata(lprime2 + x2val)
    # print(w02)
    # print(lprime2 + x2val)
    waist2plot.set_ydata(list(np.linspace(0,w02)))
    plt.show()
slder1.on_changed(val_update)    
slder2.on_changed(val_update)

axButton1 = plt.axes([0.1,0.89, 0.1, 0.1])
btn1 = Button(axButton1, 'Reset')

def resetSliders(event):
    slder1.reset()
    slder2.reset()
btn1.on_clicked(resetSliders)






