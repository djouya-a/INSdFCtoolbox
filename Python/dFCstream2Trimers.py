#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This function takes dFCstream as input ('2D' or '3D') and calculates "trimers" of meta-connectivity 
# (MC) [nxnxn] matrix, where n is the number of nodes in your network.
# You may use this function instead of dFCstream2MC if number of 
# nodes in your network > 200 regions.
#
# input: dFCstream --> generated by FCstr2dFCstream (2D or 3D)
#
# Example: MC3=dFCstream2Trimers(dfcstream)

# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np
from Vec2Matrix import Vec2Matrix
import itertools

def dFCstream2Trimers(dFCstream):
    
    if len(dFCstream.shape)==2:
        FCstr=Vec2Matrix(dFCstream)
        
    if len(dFCstream.shape)==3:
        FCstr=dFCstream
        
    n = FCstr.shape[0]
    MC3 = np.zeros((n,n,n))
    var1=np.zeros((FCstr.shape[0],FCstr.shape[2]))
    for i in range(n):
        var1[:,:] = FCstr[:,i,:]
        var2 = np.corrcoef(var1)
        var2=np.nan_to_num(var2)
        np.fill_diagonal(var2, 0)
#         var2[var2==1]=0
        MC3[:,:,i]=var2
    
   
    return MC3


