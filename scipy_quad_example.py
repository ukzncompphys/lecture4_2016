import numpy
import scipy.integrate as quad
import func_example


val,err=quad.quad(func_example.mygauss,-20,20)
print val
val,err=quad.quad(func_example.mygauss,-25,15)
print val

