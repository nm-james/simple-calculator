import time
import math
from area import *
from volume import *
from surfacearea import *

choice = True
a = "0"
b = "0"
c = "0"

# Check if the number is an actual option
def CheckValidOption( numberSelected, maximumRequired ):
    if not numberSelected.isnumeric():
        print("You haven't selected a valid number. Please try again.")
        time.sleep(2)
        return False
    else:
        optionsSelected = int(numberSelected)
        print("=" * 35)
        if ( optionsSelected == (maximumRequired + 1) ):
            print("You have decided to exit the script.")
            print("Thanks for using it!")
            time.sleep(3)
            return "Break"
        if (optionsSelected > maximumRequired or optionsSelected < 1):
            print("You haven't selected a valid number. Please try again.")
            time.sleep(2)
            return False
        else:
            return True

# Calculations Array
calcArray = {}
calcArray["Area"] = {}
calcArray["Total Surface Area"] = {}
calcArray["Volume"] = {}
typeArray = [ "NULL", "Area", "Total Surface Area", "Volume" ]

# Config Work
# Area
calcArray["Area"][1] = ["Rectangle", rectangleArea, ["Length", "Width"]]
calcArray["Area"][2] = ["Circle", circleArea, ["Radius"] ]
calcArray["Area"][3] = ["Triangle", triangleArea, ["Base", "Height"]]
calcArray["Area"][4] = ["Trapezium", trampeziumArea, ["Side A", "Side B", "Height"]]
calcArray["Area"][5] = ["Parallelogram", parallelogramArea, ["Base", "Height"]]

#Total Surface Area
calcArray["Total Surface Area"][1] = ["Rectangular Prism", rectangularTSA, ["Length", "Width", "Height"]]
calcArray["Total Surface Area"][2] = ["Cylinder", cylinderTSA, ["Radius", "Height"]]
calcArray["Total Surface Area"][3] = ["Cone", coneTSA, ["Radius", "Height"]]
calcArray["Total Surface Area"][4] = ["Sphere", sphereTSA, ["Radius"]]

#Volume
calcArray["Volume"][1] = ["Sphere", sphereVolume, ["Radius"]]
calcArray["Volume"][2] = ["Rectangular Prism", rectangularVolume, ["Length", "Width", "Height"]]
calcArray["Volume"][3] = ["Cone", coneVolume, ["Radius", "Height"]]
calcArray["Volume"][4] = ["Cylinder", cylinderVolume, ["Radius", "Height"]]

#Menu
while choice == True:
    print("+" * 35)
    print("Shape Calculations")
    print("+" * 35)
    print("1. Calculate the Area of a Shape")
    print("2. Calculate the Total Surface Area of a Shape")
    print("3. Calculate the Volume of a Shape")
    print("4. Exit the Script")

    typeSelected = input("Select an option: ")

    typeValidation = CheckValidOption( typeSelected, 3 )

    if typeValidation == "Break": 
        break

    # Convert to int if needed
    if typeValidation:
        typeSelected = int(typeSelected)
    else:
        continue
    
    print("You have selected to calculate the", typeArray[typeSelected], "of a shape.")
    time.sleep(1)

    print("=" * 35)

    options = calcArray[typeArray[typeSelected]]

    # Loop through CalcArray and display options
    for i in range( 1, len( options ) + 1):
        print( str(i) + ". Calculate the area of a " + options[i][0] + ".")

    print( str( len(options) + 1) + ". Exit the Script" )

    optionsSelected = input("Select an option: ")

    optionValidation = CheckValidOption( optionsSelected, len(options) )

    if optionValidation == "Break": 
        break

    if optionValidation:
        optionsSelected = int(optionsSelected)
    else:
        continue

    # Loop through a table and ask for inputs
    optionstbl = calcArray[typeArray[typeSelected]][optionsSelected][2]
    for x in optionstbl:
        inputvar = input(x + ": ")
        if inputvar == "":
            a = "nil"
            break
        if (a == "0"):
            a = inputvar
        elif (b == "0"):
            b = inputvar
        elif (c == "0"):
            c = inputvar
    
    print("=" * 35)
    if not a.isnumeric() or not b.isnumeric() or not c.isnumeric(): 
        print("Error! There has been a problem with the value you have given. Please try again.")
        time.sleep(2)
    else:
        print( "The", typeArray[typeSelected], "of your", calcArray[typeArray[typeSelected]][optionsSelected][0], "is: ", calcArray[typeArray[typeSelected]][optionsSelected][1]( int(a), int(b), int(c) ) )
        time.sleep(3)

    a = "0"
    b = "0"
    c = "0"
