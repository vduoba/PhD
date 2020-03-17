# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:54:45 2020

@author: VDuoba
"""
from sympy import * # Not a good idea as lots, and lots and lots
init_printing() # fancy printing
from sympy.stats import Binomial, Beta, density
from sympy import Symbol

x=Symbol('x')
mu=Symbol('mu')
sigma=Symbol('sigma')
ans =exp(-(x - mu)**2/sigma**2)
ans
# Try some stuff to do with printing, etc
latex(ans) # Print latex expression
preview(ans) # latex program is not installed!!!
pprint(ans)  # Gives teletext output (clumsy)
#
ans.diff(x)
# or
diff(ans,x)
#
# 2nd derivative
diff(ans.diff(x),x)
# or
ans2= ans.diff(x).diff(x)
#
simplify(ans2)
#
expr=sin(x)**2 + cos(x)**2
expr # Just the above, not 1
simplify(expr) # Simplified to 1
#
# NOTE: sympify is not the same as simplify!!!
sympify('r*cos(theta)^2') # Coverts python objects intp Sympy objects
#
# All sympy expressions are immutable
a=(x+1)**2
b=x**2 +2*x +1
a==b  # False, as not structurally the same
simplify(a-b)==0 # True
#
# Symbolic equality
y=Symbol('y')
eq = Eq(x**2, y)
eq
#
acos(S.Half) # Symbolic pi/3
acos(Rational(1,2)) # Symbolic pi/3
#