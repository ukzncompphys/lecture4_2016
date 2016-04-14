from numpy import concatenate,exp,pi,arange,complex
import numpy
def myfft(vec):
    n=vec.size
    #FFT of length 1 is itself, so quit
    if n==1:
        return vec
    #the % operator 
    if (n%2==0):
        #pull out even and odd parts of the data
        myeven=vec[0::2]
        myodd=vec[1::2]

        nn=n/2;
        j=complex(0,1)    
        #get the phase factors
        twid=exp(-2*pi*j*arange(0,nn)/n)

        #get the dfts of the even and odd parts    
        eft=myfft(myeven)
        oft=myfft(myodd)
        
        #Now that we have the partial dfts, combine them with 
        #the phase factors to get the full DFT
        myans=concatenate((eft+twid*oft,eft-twid*oft))
        return myans
    else:
        assert(n%3==0)
        mya=vec[0::3]
        myb=vec[1::3]
        myc=vec[2::3]
        j=complex(0,1)
        nn=n/3
        twid1=exp(-2*pi*j*arange(0,nn)/n)
        twid2=exp(-4*pi*j*arange(0,nn)/n)

        f1=exp(-2*pi*j/3) #these two guys are for n/3<=k/2n/3
        f2=exp(-4*pi*j/3)
        f1b=f2;          #and these are for 2n/3<=k<n
        f2b=f1; #started off as -8*pi*j/3

        aft=myfft(mya)
        bft=myfft(myb)*twid1
        cft=myfft(myc)*twid2
        
        ft1=aft+bft+cft
        ft2=aft+bft*f1+cft*f2
        ft3=aft+bft*f1b+cft*f2b
        
        ft=concatenate((ft1,ft2,ft3))
        
        return ft
    
