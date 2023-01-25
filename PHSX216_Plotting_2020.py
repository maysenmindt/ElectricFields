#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Physics 216
#Plotting code to use the whole year!
#Jaylene Naylor
#September 2015, modified Sept 2017, August 2018, Aug 2020(for Python 3.8)
#-------------------------------------------#
get_ipython().run_line_magic('matplotlib', 'inline')

#Import packages and libraries needed and give them shortcut names

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------#
#Data Section - Create Arrays for data. Perform necessary calculations
#CHANGE THE VARIABLE NAMES and numbers to match your data
Natural_Log_of_rMid = np.array([2.047692843,1.981001469,1.909542505,1.832581464,1.749199855,1.658228077,1.558144618,1.446918983,1.32175584,1.178654996,1.011600912,0.810930216,0.559615788,0.223143551]) #what are units?
Natural_Log_of_E = np.array([0.937399695,-1.32175584,-3.064725145,-1.514127733,-0.89976143,-2.612740021,-1.57664809,-1.040343381,-1.32175584,-0.776528789,-0.653926467,-0.679901954,-0.544727175,0.373859769]) #what are units?


#--------------------------------------------#
#Create arrays for uncertainties
#CHANGE THE VARIABLE NAME and numbers to match your data 
E_error = np.array([-1.414218172,-1.414213613,-1.414213564,-1.414213597,-1.414213679,-1.414213566,-1.414213593,-1.414213651,-1.414213613,-1.414213712,-1.414213754,-1.414213744,-1.4142138,-1.414215056])


#--------------------------------------------#
#Re-assign variables as x, y, dy so that the following code may remain generic

x = Natural_Log_of_rMid   #this should be the array you want to plot on the x axis
y = Natural_Log_of_E
dy = E_error  #this should be your error in y array

#----------------------------------------------#
#Don't need to change anything in this section!
 
#Find the intercept and slope, b and m, from Python's polynomial fitting function
b,m=np.polynomial.polynomial.polyfit(x,y,1,w=dy)

#Write the equation for the best fit line based on the slope and intercept
fit = b+m*x

#Calculate the error in slope and intercept 
#def Delta(x, dy) is a function, and we will learn how to write our own at a later date. They are very useful!
def Delta(x, dy):
    D = (sum(1/dy**2))*(sum(x**2/dy**2))-(sum(x/dy**2))**2
    return D
 
D=Delta(x, dy)
 
dm = np.sqrt(1/D*sum(1/dy**2)) #error in slope
db = np.sqrt(1/D*sum(x**2/dy**2)) #error in intercept

#Calculate the "goodness of fit" from the linear least squares fitting document
def LLSFD2(x,y,dy):
    N = sum(((y-b-m*x)/dy)**2)
    return N
                      
N = LLSFD2(x,y,dy)

#-----------------------------------------------------------------------#
#Plot data on graph. Plot error bars and place values for slope, error in slope
#and goodness of fit on the plot using "annotate"

plt.figure(figsize=(15,10))
 
plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')
 
 
#create labels  YOU NEED TO CHANGE THESE!!!
plt.xlabel('Natural Log of rMid (m)')
plt.ylabel('Natural Log of E (N/C)')
plt.title('Electric Field and Potential')
 
plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars
 
plt.annotate('Slope (N/(C*m)) = {value:.{digits}E}'.format(value=m, digits=2),
             (0.05, 0.9), xycoords='axes fraction')
 
plt.annotate('Error in Slope (N/(C*m) = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.05, 0.85), xycoords='axes fraction')
 
plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.05, 0.80), xycoords='axes fraction')

plt.show()


# In[ ]:




