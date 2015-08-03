# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:51:07 2015

@author: oliver
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

def F_DFA(x,nVec,sampleNum,qVec,detrendOrder):
    f2_dfa=F2_DFA(x=x,nVec=nVec,sampleNum=sampleNum,detrendedOrder=detrendOrder)
    f_dfa=pd.DataFrame()
    for q in qVec:
        f_dfa_Tmp=f2_dfa**(q/2)
        f_dfa[str(q)]=f_dfa_Tmp.apply(mean)**(1/q)
    return(f_dfa)