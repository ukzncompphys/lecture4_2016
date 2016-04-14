import numpy

x0=0
x1=numpy.pi

mydelts=[0.5,0.1,0.03,0.01,0.003,0.001]
for dx in mydelts:
    x=numpy.arange(x0,x1,dx)
    y=numpy.sin(x)
    tot=y.sum()*dx
    print 'integral is ' + repr(tot) + ' with dx=' + repr(dx)

