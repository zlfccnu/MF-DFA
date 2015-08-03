#-*-coding: utf-8-*-
"""
Created on Thu Dec  4 20:30:25 2014

@author: zlfccnu
"""

import numpy as np
import pandas as pd
import matplotlib as mp
import scipy as sy
import sympy as syy
from igraph import *
import random
import itertools
import statsmodels.formula.api as sm

def F2_DFA(x,nVec,sampleNum,detrendOrder):
    y=x-x.mean()
    y=y.cumsum()
    f2_DFA=pd.DataFrame()
    for n in nVec:
        f2_DFA_Tmp=np.array(np.zeros(sampleNum))
        startIndex=random.sample(range(len(y)-n+1),sampleNum)
        for i in range(sampleNum):
            fit_x=range(startIndex[i],(startIndex[i]+n-1))
            fit_y=y[startIndex[i]:(startIndex[i]+n-1)]
            DFA_coef=np.polyfit(fit_x,fit_y,detrendOrder)
            fitDFA=np.poly1d(DFA_coef)
            f2_DFA_Tmp[i]=np.mean(fit_y-fitDFA(fit_x))
        f2_DFA[str(n)]=f2_DFA_Tmp
    