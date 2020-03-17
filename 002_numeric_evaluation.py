# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:31:57 2020

@author: VDuoba
"""
# numeric_evaluation.py
from sympy import *
init_printing(use_latex='mathjax')
n=symbols('n',integer=True)
x,y,z=symbols('x, y, z')
n,m=symbols('n, m', integer=True)
import matplotlib as plt
#
# The simplest and slowest way to evaluate an expression
# is via .subs and .evalf
sin(x)
sin(x).subs({x:0})      # 0
sin(x).subs({x:-1})     = -sin(1)
sin(x).subs({x:-1}).evalf() # ￼-0.84147
sin(x).subs({x:-1}).evalf(n=100) # ￼Wow, what a lot of decimal places!
#
result=integrate(x**n,(x,y,z))
result.subs({n: 2, y: 0, z: 3}).evalf() # 9
result.subs({n: -1, y: 5, z: 3}).evalf() # -0.5108
# doit() instead of evalf() would try and do it symbolically
result.subs({n: -1, y: 5, z: 3}).doit() # -log(5) + log(3)
#
