import numpy
import scipy.integrate as quad
import func_example



#these were broken because if quad doesn't hit the narrow gaussian peak, 
#it will think it has converged when it really hasn't

val,err=quad.quad(func_example.mygauss,-20,20)
print val
val,err=quad.quad(func_example.mygauss,-25,15)
print val

#the way to fix this problem is to make sure that the numerical integrator
#hits the peak of the gaussian.  We know the peak is at zero, so we can integrate 
#from left to zero and zero to right and we'll get the correct answer

val,err=quad.quad(func_example.mygauss,-20,0)
val2,err2=quad.quad(func_example.mygauss,0,20)
print 'new first value is ' + repr(val+val2)

val,err=quad.quad(func_example.mygauss,-25,0)
val2,err2=quad.quad(func_example.mygauss,0,15)
print 'new second value is ' + repr(val+val2)



