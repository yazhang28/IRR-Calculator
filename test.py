# -*- coding: utf-8 -*-
"""
Test cases for irrCalculator.py
03/28/18
"""
import numpy as np
from irrCalculator import calcResults, repeatFLow

# Tests #

# given array of cashflow (cs), number of periods (t) starting from 0, 
# x the staring estimate for f(NPV) = 0 
# cs[0] is the initial investment (negative value)

# cash inflow
cs = np.array([-70000,12000,15000,18000,21000,26000])
t = 6
calcResults(t, cs, 0.1)

# fixed cash inflow
t2, cs2 = repeatFLow(-100.0, 60.0, 3)
calcResults(t2, cs2, 0.1)

cs3 = np.array([-100, 100, 0, 7])
t3 = 4
calcResults(t3, cs3, 0.1)

cs4 = np.array([-100, 0, 0, 74])
t4 = 4
calcResults(t4, cs4, 0.1)
