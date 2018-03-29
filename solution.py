# -*- coding: utf-8 -*-
"""
IRR calculator
03/28/18

references: https://docs.scipy.org/doc/numpy-1.10.4/reference/generated/numpy.irr.html
"""

import numpy as np # array arithmetic
from scipy.optimize import fsolve # for root calculation

# given array of cashflow, cashflow[0] is the initial investment
# number of periods t

# IRR given by npv = sum((cashflow at t/( 1 + irr) ** t)) 
def npvForIRR(irr, t, cashFlow):
    periods = np.arange(t) 
    return np.sum(cashFlow / (1 + irr) ** periods)
       
def calcIRR(t, cashflow, x = 0.1):
    # calculate rate: polynomial root for which y - intercept (NPV) = 0
    irr = fsolve(npvForIRR, args = (t, cashflow), x0=x)
    return irr
    
# actual NPV
def npv(irr, t, cashflow):
    periods = np.arange(1,t)
    return np.sum(cashflow[1:]/(1 + irr) **periods[1:]) + cashflow[0]
    
