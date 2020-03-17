from sympy import *
init_printing(use_latex='mathjax')
n=symbols('n',integer=True)
x,y,z=symbols('x, y, z')
#
integrate(x**2,x) # indefinite (no const added)
integrate(x**2, (x,0,3)) # 9
integrate(x**n, (x,y,z)) # Symbolic
Integral(x**n, (x,y,z)) # Integral object, not evaluated
#
Integral(x,x).doit() # Forces evaluation if possible. e.g x^2/2
#
# Infinity
mu,sigma=symbols('mu,sigma',positive=True)
ans3=integrate(exp(-(x-mu)**2/(2*sigma**2)), (x,-oo,oo))
ans3 # sigma*sqrt(2*pi)
#
# Basic assumption is that everything is complex numbers
a=symbols('a', positive=True)
sqrt(a**2)
a # not |a| or +/- a
#
(a+1).is_positive # True
#
n=symbols('n',integer=True)
sin(n*pi) # Knows it is 0
#
