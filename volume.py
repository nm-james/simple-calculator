import math

#Volume Calculations

def sphereVolume( r, null, nil ):
    return (1 + (1 / 3)) * math.pi * r ** 3

def rectangularVolume( l, w, h ):
    return l * w * h

def coneVolume( r, h, NULL ):
    return math.pi * (r ** 2) * (h / 3)

def cylinderVolume( r, h, NULL ):
    return math.pi * ( r ** 2 ) * h