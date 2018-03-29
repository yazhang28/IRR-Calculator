# -*- coding: utf-8 -*-
"""
Yao Zhang
IRR calculator
03/28/18

references: https://docs.scipy.org/doc/numpy-1.10.4/reference/generated/numpy.irr.html
"""

import numpy as np # for array arithmetic
from scipy.optimize import fsolve # for root calculation

#class irrCalculator:
# IRR given by npv = sum((cashflow at t/( 1 + irr)^t)) 
def npvForIRR(irr, t, cashFlow):
    periods = np.arange(t) 
    return np.sum(cashFlow / (1 + irr) ** periods)
   
def calcIRR(t, cashFlow, x = 0.1):
    # calculate IRR: polynomial root for which y - intercept (NPV) = 0
    irr = fsolve(npvForIRR, args = (t, cashFlow), x0=x)
    return np.asscalar(irr)
 
# actual npv = sum(cashflow at t=1 /(1 + irr)^t) + initial
# def calcNPV(irr, t, cashFlow):
#    periods = np.arange(0,t) 
#    return (cashFlow[0] + np.sum(cashFlow[1:]/((1 + irr) **periods[1:]))) 
   
# to prove correctness of IRR returns T/F on the condition whether NPV is close to 0 
def validate(irr, t, cashFlow):
    print('validation for NPV: ', npvForIRR(irr, t, cashFlow))
    print(np.allclose(npvForIRR(irr, t, cashFlow), 0))

# builds array for n repeated cashflows
def repeatFLow(initial, amount, n):
    t = n+1
    cashflow = np.array([initial] + [amount]*n)
    return t, cashflow

# x: starting estimate for f(NPV) = 0
def calcResults(t, cashflow, x): 
    print('given cashflow: ', cashflow)
    print('period t: ', t)
    print('starting estimate value for IRR: ', x)
    print()
    irr = calcIRR(t, cashflow, x)
    print('IRR: %.2f%%' % (irr*100))
    validate(irr, t, cashflow)
    print()