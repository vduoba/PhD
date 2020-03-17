# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:54:58 2020

@author: VDuoba
"""
# lambify.py (should be lambdify.py)
# .subs() and .evalf() are ok for point evaluations
# but not good for evaluation at a number of points.
# Sympy can rewrite expressions as normal Python functions
# that use the math library, vectorized computations using the
# NumPy library, C or FORTRAN code using code printers or other systems.
from sympy import *
init_printing(use_latex='mathjax')
import numpy as np
#
f=lambdify(x,x**2)
f(3) # 9
f=lambdify(x,x**2,'numpy') # Use numpy backend
data=np.array([1,2,3,4,5])
f(data) # Returns array of squared numbers
#
from sympy.physics.hydrogen import R_nl
n=3 # These are python objects, not SymPy objects
l=1
r=6 # Carbon
expr=R_nl(n,l,x,r)
expr # Return expression with x as a variable
# Turn it into a function that uses the numpy backend
f=lambdify(x,expr,'numpy')
from matplotlib.pyplot import plot
nx=np.linspace(0,5,1000)
plot(nx,f(nx)) # Get a plot in the console.
# Create a numpy fn that computes the derivative of the above
import numba
g=numba.jit(f)
timeit g(nx) # faster
# Derivative
d2=diff(expr,x) # Go back to SymPy object, not python object
f2=lambdify(x,d2,'numpy')
plot(nx,f2(nx))
# Do the plots together
plot(nx,f2(nx))
plot(nx,f(nx))
#