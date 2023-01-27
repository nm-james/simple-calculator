import math

#TSA Calculations

def rectangularTSA( l, w, h ):
    return 2 * (( l * w ) + ( l * h ) + ( w * h ))

def cylinderTSA( r, h, nil ):
    return 2 * math.pi * (r * (r + h))
    
def sphereTSA( r, null, nil ):
    return math.pi * (4 * (r ** 2))

def coneTSA(r, h, null):
    return math.pi * (r ** 2) + math.pi * ( r * math.sqrt( (r ** 2) + (h ** 2) ) )