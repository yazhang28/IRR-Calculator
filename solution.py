# -*- coding: utf-8 -*-
"""
IRR calculator
03/28/18
"""

import numpy as np

# given array of cashflow, cashflow[0] is the initial investment
# number of periods t

# npv = sum((cashflow at t/( 1 + irr) ** t)) 
def calcNPV(irr, t, cashFlow):
    periods = np.arange(t) 
    npv = np.sum(cashFlow / (1 + irr) ** periods)
    return npv
    

def calcIRR(t, cashflow):
    # calculate rate: polynomial root
    pass