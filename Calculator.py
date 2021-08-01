import math
operation = input("Operation: ")

#beginning of the side trignometry section

if operation=="sidetrigonometry" or operation=="strig" or operation== "sidetrig" :
    print("If value unknown, input 0. If a variable, input 1.")
    opp = float(input("Opposite: "))
    hyp = float(input("Hypotenuse: "))
    adj = float(input("Adjacent: "))
    angleDeg = float(input("Angle in degrees: "))
    
    if adj ==float("0") and hyp==float("1") :
        angleRad = (math.radians(angleDeg))
        adjpreStrigAnswer = (math.sin(angleRad))
        adjStrigAnswer = (opp / adjpreStrigAnswer)
        print(adjStrigAnswer)
    
    
    if hyp ==float("0") and opp==float("1") :
       angleRad = (math.radians(angleDeg))
       oppPreStrigAnswer = math.tan(angleRad)
       oppStrigAsnwer = (adj / oppPreStrigAnswer)
       print(oppStrigAsnwer)
        
        
    if opp ==float("0") and adj==float("1") :
        angleRad = (math.radians(angleDeg))
        hypPreStrigAnswer = math.cos(angleRad)
        hypStrigAnswer = (hyp / hypPreStrigAnswer)
        print(hypStrigAnswer)

#beginning of the degree trigonometry section        
        
elif operation=="dtrigonometry" or operation=="degreetrig" or operation=="dtrig" :
    print("If value unknown, input 0.")
    opp = float(input("Opposite: "))
    hyp = float(input("Hypotenuse: "))
    adj = float(input("Adjacent: "))
    
    if opp ==float("0") :
        oppzeropreAnswer = math.acos(adj / hyp)
        oppzeroAnswer = math.degrees(oppzeropreAnswer)
        print(oppzeroAnswer)
 
    if adj ==float("0") : 
        adjzeropreAnswer = math.asin(opp / hyp)
        adjzeroAnswer = math.degrees(adjzeropreAnswer)
        print(adjzeroAnswer)   
  
    if hyp ==float("0") : 
        hypzeropreAnswer = math.atan(opp / adj)
        hypzeroAnswer = math.degrees(hypzeropreAnswer)
        print(hypzeroAnswer)

#beginning of the Percentages section

elif operation== "%" or operation == "percentages" or operation=="pcnt" :
    
    print("One for Multiplication by Percentages, two for Division, three for Value Before Deduction, four for Tax.")
    
    percentOperation = (input(""))
    
    if  percentOperation ==("1"):    
            pctMNumber1 = float(input("Number 1: "))
            pctMNumber2 = float(input("Number 2: "))
            pctMultiplicationAnswer = (pctMNumber1 * pctMNumber2)
            print(pctMultiplicationAnswer)
                
    if  percentOperation == "2" :
            pctDNumber1 = float(input("Number 1: "))
            pctDNumber2 = float(input("Number 2: "))
            pctDivisionAnswer = (pctDNumber1 * pctDNumber2)
            print(pctDivisionAnswer)
        
    elif percentOperation == "3" :
            currentValue = float(input("Current Value: "))
            percentOff = float(input("Percent Off (0.1-100%): "))
            percent = (percentOff/100)
            remainingA = (1 - percent)
            pctDeductionAnswer = (currentValue / remainingA)
            print(pctDeductionAnswer)
    
    elif percentOperation =="4" :
            taxBefore = float(input("Original Amount: "))
            taxPct    = float(input("Tax Percent (0.1-100): "))
            taxPercentage = (taxPct / 100)
            taxedAmount = (taxBefore * taxPercentage)
            print(taxedAmount + taxBefore)
            
#basic addition, multiplication, subtraction and division
if operation=="*" :
    
        Number1 = float(input("Number 1: "))
    
        Number2 = float(input("Number 2: "))
    
        multiplicationAnswer = float(Number1 * Number2)
        
        print(multiplicationAnswer)
        
if operation=="+" :
            
            Number1 = float(input("Number 1: "))
    
            Number2 = float(input("Number 2: "))

            additionAnswer = float(Number1 + Number2)
    
            print(additionAnswer)
            
if operation=="/" :
    
            Number1 = float(input("Number 1: "))
    
            Number2 = float(input("Number 2: "))
    
            divisionAnswer = float(Number1 / Number2)
       
            print(divisionAnswer)
        
if operation=="-" : 
            
            Number1 = float(input("Number 1: "))
    
            Number2 = float(input("Number 2: "))
            
            subtractionAnswer = float(Number1 - Number2)
            
            print(subtractionAnswer)

#circle operations

if operation == "circumference" or "ccf" : 

            radius = float(input("Radius: "))
            
            pi = 3.1415926535897
        
            circumference = (2 * radius * pi)
            
            print(circumference)
            
if operation == "areacircle" or "ac" : 
    
            radius = float(input("Radius: "))
            
            pi = 3.1415926535897
            
            areaCircle = (radius ** 2 * pi)
        
            print(areaCircle) 
            
#shape operations. the threedOperation variable isnt actually used for any three dimensional shapes. I just didnt feel liek changing it.
            
if operation== "3d" or "3D" :           

        threedOperation = input("1 for right Triangles, 2 for Trapezoids, 3 for Parallelograms: ")
        
        if threedOperation == "1":
        
            triangleOperation = input("1 for right triagnle perimeter, 2 for right triangle area, 3 for Pythagorean theorem: ")
            
            if triangleOperation == "1" :
                
                sideA = float(input("Side A: "))
                
                sideB = float(input("Side B: "))
                
                sideC = float(input("Side C: "))
                
                trianglePerim = (sideA + sideB + sideC)
                
                print(trianglePerim)
                
            if triangleOperation == "2" :
                
                base = float(input("Base: "))
                
                height = float(input("Height: "))
                
                triangleArea = (base * height)
                
                print(triangleArea)
                
            if triangleOperation == "3" :
                
                print("If value unknown, input 0. Input values squared.")
                
                asqrd = float(input("A: "))
                
                bsqrd = float(input("B: "))
                
                csqrd = float(input("C: "))
                
                if asqrd == "0" :
                
                    asqrdSolve = (math.sqrt(csqrd-bsqrd))
                
                    print(asqrdSolve)
                    
                if bsqrd =="0" :
                    
                    bsqrdSolve = (math.sqrt(csqrd-asqrd))
                    
                    print(bsqrdSolve)
                    
                if csqrd =="0" :
                    
                    csqrdSolve = (math(asqrd + bsqrd))
                    
                    print(csqrdSolve)
                    
        if threedOperation == "2" :
            
            trapOperation = input("1 for trapezoid perimeter, 2 for trapezoid area: ")
            
            if trapOperation == "1" :

                sideA = float(input("Side A: "))
                
                sideB = float(input("Side B: "))
                
                sideC = float(input("Side C: "))
                
                baseTrap = float(input("Base: "))
                
                trapPerim = float(sideA + sideB +sideC + baseTrap)
                
                print(trapPerim)
                
            if trapOperation == "2" :
                
                trapHeight = float(input("Height: "))
                
                sideB = float(input("Side B: "))
                
                baseTrap = float(input("Base: "))
                 
                trapArea = (.50 * trapHeight(baseTrap + sideB))
                
                print(trapArea)                   
                
        if threedOperation == "3" :
            
            paraOperation = input("1 for Parallelogram Perimeter, 2 for Parallelogram Area : ")
            
            if paraOperation == "1" : 
                
                sideA = float(input("Side A: "))
                
                sideB = float(input("Side B: "))
            
                paraPerimeter = (sideA * sideB)
                
                print(paraPerimeter)
            
            if paraOperation == "2" :
                
                sideB = float(input("Side B: "))
                
                paraHeight = float(input("Height: "))
                
                paraArea = (sideB * paraHeight)

                print(paraArea)
                
            #three 3 section -_-    
                
if operation == "fullsolid" or "fs" : 
           
            trueThreeD = input("1 for Rectangular Solid, 2 for Cubes, 2 for Cones, 4 for Cylinders, 5 for Spheres: ")
        
           
            #rectangular solid (box) section        
        
            if trueThreeD == "1" :
             
                rectSolidOperation = input("1 for volume, 2 for surface area")
                
            if rectSolidOperation == "1" : 
                        
                rectSLength = float(input("Length: "))
                        
                rectSWidth = float(input("Width: "))
                        
                rectSHeight = float(input("Height: "))
                        
                rectSVolume = (rectSHeight * rectSLength * rectSWidth)
                
                print(rectSVolume)
                
            #rectangular solid (box) section    
                
            if rectSolidOperation == "2" :
            
                rectSLength = float(input("Length: "))
                        
                rectSWidth = float(input("Width: "))
                        
                rectSHeight = float(input("Height: "))
                
                rectSPreSurfaceArea = (rectSLength * rectSHeight * 2) + (rectSLength * rectSWidth * 2)
                
                rectSSurfaceArea = (rectSPreSurfaceArea + ((rectSWidth * rectSHeight) * 2))
                
                print(rectSSurfaceArea)
            
            #cube volume section
                
            if trueThreeD == "2" : 
            
                print("Cube Volume")
                      
                cubeSide = float(input("Side Length: "))   
                      
                cubeVolume = (cubeSide ** 3)
                
                print(cubeVolume)
            
            #cone volume section
                
            if trueThreeD == "3" :
            
                print("Cone Volume: ")
                
                coneRadius = float(input("Radius: "))
                
                coneHeight = float(input("Height: "))
                
                coneVolume = (.33 * pi * (coneRadius * 2) * coneHeight)
                
                print(coneVolume)
            
            #cirular cylinder section
                
            if trueThreeD == "4" : 
            
                cylinOperation = input("1 for Volume of right circular cylinder, 2 for Surface Area of right circular cylinder: ")
                
                if cylinOperation == "1" : 
                    
                    cylinRadius = float(input("Radius: "))
                    
                    cylinHeight = float(input("Height: "))
                    
                    cylinVolume = (pi * (cylinRadius ** 2) * cylinHeight)
                    
                    print(cylinVolume)
                
                if cylinOperation == "2" : 
                    
                    cylinRadius = float(input("Radius: "))
                    
                    cylinHeight = float(input("Height: "))
                    
                    cylinSurfaceArea = ((2 * pi * (cylinRadius ** 2) * (2 * pi * cylinRadius * cylinHeight) ))
                    
                    print(cylinSurfaceArea)                    
            
            #sphere volume section
            
            if trueThreeD == "5": 
                
                print("Sphere Volume.")
                
                sphereRadius = float(input("Radius: "))
                
                sphereVolume = ((4 / 3) * pi * (sphereRadius ** 3))

                print(sphereVolume)