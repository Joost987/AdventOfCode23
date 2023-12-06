import math
import numpy;
def FindRoots(Trace, distance):
    #distance=(Trace-tbutton)*tbutton
    #(t^2-Tt+distance=0)
    a,b=(Trace-(Trace**2-4*distance)**(1/2))/2,(Trace+(Trace**2-4*distance)**(1/2))/2
    return math.floor(b)-math.ceil(a)+1

racelst=[[40,233],[82,1011],[84,1110],[92,1487]];numpy.product([FindRoots(*racelst[i]) for i in range(len(racelst))])

