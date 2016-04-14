import numpy
from numpy import pi
def orthog(k1,k2,N):
    x=numpy.arange(N)
    I=numpy.complex(0,1)
    vec1=I*2*pi*k1*x/N
    vec2=-I*2*pi*k2*x/N
    col1=numpy.exp(vec1)
    col2=numpy.exp(vec2)
    tot=numpy.sum(col1*col2)
    return tot

if __name__=="__main__":
    print orthog(3,-3,16)
    
