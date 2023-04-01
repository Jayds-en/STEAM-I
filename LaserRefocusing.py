# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:14:55 2021

@author: Jayden Maree
Requirements:
    Lenses should be adjustable for fine and course focus
    A minimum spot size should be attained (and another model for max Intensity 
                                            incorporated)
Steps:
    Create a thin lens system
    Figure out spot size via magnification (uses s and f)
    - this would give us ideal distances?
    Create a way to manipulate variables visually?
    
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#Laser characteristics at aperture
wavelength = 532*10**-6 #mm
divergence = 0.125*10**-3 #rad

d = 9 #mm #Exit diameter at aperture
wAperture  = d/2

#Lens Distances from Laser Aperture to Lenses 1, 2 and 3
Lens1Laser =  1817.68#mm
Lens2Laser =  2268.53#mm
Lens3Laser = 0 #meter #This lens is in water
SubstrateLens3 = Lens2Laser + 45.955

#Lens Effective Focal Lengths 
f1 = 360 #mm?
f2 = 45.955
# f3 = 45.955

#substrate d


#Beam between aperture and Lens 1
w0 = wavelength/(np.pi*divergence) #could be named "w00"
zR = (np.pi*w0**2)/wavelength #"""This is why my results were not as I expected"""
z = (np.sqrt(((wAperture/w0)**2)-1)*(np.pi*w0**2))/wavelength

# print (z)
print (w0)
print(zR)

def dImage(LensLaser,sPrimeLaser,f,zR,w0):
    s = -(LensLaser - sPrimeLaser)
    #sPrimeLaser for lens 1 is actually = -z
    #this line allows for s to be calculated for lens 2, 3, etc. 
    
    mag = 1/(np.sqrt(((1-s/f)**2) + ((zR/f)**2))) 
 
    # Image1dist = 1/((1/(s1+(zR**2)/(s1+f1)))+ 1/f1) #Image distance from lens
    
    sPrime = 1/((1/(((zR**2)/(f-s))-s))+(1/f)) #s1prime is the same calculation Image distance 1
    sPrimeLaser = LensLaser +sPrime 
    zRP = zR*mag**2 #Raleigh range for beam after lens 1 and before lens 2
    wP = mag*w0
    # print(magTest)
    print(sPrime)
    # print(mag)
    print(wP)
    # print(2*wP)
    # print(zR)
    # print(zRP)
    return [sPrimeLaser,wP,zRP]
#There is an equation to calculate the maximum and minimum image distance, and I want to see if my code
# correlates
#Lens 1

def system(Lens1Laser,Lens2Laser,):#Lens3Laser):

    [sPrime1Laser,w01,zR1] = dImage(Lens1Laser,-z,f1,zR,w0) 

    [sPrime2Laser,w02,zR2] = dImage(Lens2Laser,sPrime1Laser,f2,zR1,w01)
    
    # [sPrime3Laser,w03,zR3] = dImage(Lens3Laser,sPrime2Laser,f3,zR2,w02)

    # return [sPrime1Laser,w01,sPrime2Laser,w02, sPrime3Laser, w03]
    return [sPrime1Laser,w01,sPrime2Laser,w02]

# [sPrime1Laser,w01,sPrime2Laser,w02, sPrime3Laser, w03] = system(Lens1Laser,Lens2Laser,Lens3Laser)
[sPrime1Laser,w01,sPrime2Laser,w02] = system(Lens1Laser,Lens2Laser)

#Visualise System and Add Sliders
lens1y = list(range(0,5)) #scale: 5 mm
lens1x = [Lens1Laser]*len(lens1y)
lens2y = list(range(0,5)) #scale: 5 mm
lens2x = [Lens2Laser]*len(lens2y)
# lens3y = list(range(0,5)) #scale: 5 mm
# lens3x = [Lens3Laser]*len(lens3y)

'''
may have to adjust  the height of the spots to some scale
- determine this after seeing the plots
'''


#add code to get the waist in the middle
waist0y = list(np.linspace(0,wAperture)) # This is the laser, hence w0 is laser D/2
waist0x = [0]*len(waist0y)       # Location set to 0 meter
waist1y = list(np.linspace(0,w01)) #
waist1x = [sPrime1Laser]*len(waist1y) # Decided to use these values over the "Imagexdist" for no good reason.
# print(waist1x)
# print(waist1y)
waist2y = list(np.linspace(0,w02)) #
waist2x = [sPrime2Laser]*len(waist2y)
# waist3y = list(np.linspace(0,w03)) #
# waist3x = [sPrime3Laser]*len(waist3y)

substrateY = list(np.linspace(0,25))
substrateX = [SubstrateLens3]*len(substrateY)

# print("x is \n",x,"\ny is \n",y)a

fig, ax = plt.subplots(dpi = 200)
plt.subplots_adjust(left =0.1, bottom = 0.35)
lens1plot, = plt.plot(lens1x, lens1y, linewidth = 2, color = 'blue')
lens2plot, = plt.plot(lens2x, lens2y, linewidth = 2, color = 'blue')
# lens3plot, = plt.plot(lens3x, lens3y, linewidth = 2, color = 'blue')
substratePlot = plt.plot(substrateX, substrateY, linewidth = 2, color = 'black')

waist0plot, = plt.plot(waist0x, waist0y, linewidth = 2, color = 'red')
waist1plot, = plt.plot(waist1x, waist1y, linewidth = 2, color = 'green')
waist2plot, = plt.plot(waist2x, waist2y, linewidth = 2, color = 'purple')
# waist3plot, = plt.plot(waist3x, waist3y, linewidth = 2, color = 'orange')
# plt.axis([-300,500,0,(w01+w02+w03)])
plt.axis([-300,5000,0,(w01+w02)])

lens1Slider = plt.axes([0.1, 0.2, 0.8, 0.05])
slder1 = Slider(lens1Slider, 'Lens 1', valmin= -0.5, valmax=5000, valinit = Lens1Laser)
lens2Slider = plt.axes([0.1, 0.1, 0.8, 0.05])
slder2 = Slider(lens2Slider, 'Lens 2', valmin= 68, valmax=5000  , # slidermin = slder1,
                valinit = Lens2Laser)

def val_update(val):
    x1val = slder1.val
    lens1plot.set_xdata(x1val)
    x2val = slder2.val
    lens2plot.set_xdata(x2val)
    
    # [sPrime1Laser,w01,sPrime2Laser,w02, sPrime3Laser, w03]= system(x1val,x2val,Lens3Laser) 
    [sPrime1Laser,w01,sPrime2Laser,w02]= system(x1val,x2val) 
    # print(sPrime1Laser)
    waist1plot.set_xdata(sPrime1Laser) 
    # print(w01)
    waist1plot.set_ydata(list(np.linspace(0,w01)))
    waist2plot.set_xdata(sPrime2Laser)
    waist2plot.set_ydata(list(np.linspace(0,w02)))
    # waist3plot.set_xdata(sPrime3Laser)
    # waist3plot.set_ydata(list(np.linspace(0,w03)))
    plt.draw()

slder1.on_changed(val_update) 
slder2.on_changed(val_update)

axButton1 = plt.axes([0.1,0.9, 0.1, 0.1])
btn1 = Button(axButton1, 'Reset')

# axButton2 = plt.axes([0.25, 0.9, 0.2, 0.1])
# btn2 = Button(axButton2, 'Set Val')

def resetSliders(event):
    slder1.reset()
    slder2.reset()
btn1.on_clicked(resetSliders)
    
# def setValue(val):
#     slder2.set_val(50)
# btn2.on_clicked(setValue)

plt.show()





