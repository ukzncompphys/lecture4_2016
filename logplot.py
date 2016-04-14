import numpy
from matplotlib import pyplot as plt

#this will me we don't have to click!
plt.ion()

x=numpy.arange(0,5,0.1)
y=1+numpy.exp(x)
plt.plot(x,y)
#get the current figure axes
ax=plt.gca()
#set the yscale to be logarithmic
ax.set_yscale('log')
plt.draw()
#let's write the figure to disk
plt.savefig('logplot_example')
