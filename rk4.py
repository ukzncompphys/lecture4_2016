import numpy
def myfun(x,y,a):
    #evaluate dydx=a*x*y
    return x*y*a
def rkstep(x,y,h,a,func):
    k1=h*func(x,y,a);
    k2=h*func(x+0.5*h,y+0.5*k1,a);
    k3=h*func(x+0.5*h,y+0.5*k2,a);
    k4=h*func(x+h,y+k3,a);
    dy=(k1+2*k2+2*k3+k4)/6
    return dy
y0=2.0
x0=4.0
x1=10
a=0.5
h=0.01
y=y0
for x in numpy.arange(x0,x1,h):
    #print "(x,y)="+repr(x)+' '+repr(y)
    y=y+rkstep(x,y,h,a,myfun)
print "at end (x,y)=" + repr(x+h) + ' ' + repr(y)
#can solve analytically:
#dy/y=axdx, log(y)=0.5*ax^2+c, y=c*exp(0.5*ax^2)
#at (x0,y0)=c=y0/exp(0.5*ax0**2)
c=y0/numpy.exp(0.5*a*x0**2)
print "predicted: " + repr(c*numpy.exp(0.5*a*(x+h)**2))
