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

#start of the percentages section
elif operation== "%" or operation == "percentages" or operation=="pcnt" :
    print("1 for Multiplication by Percentages, 2 for Division, 3 for Value Before Deduction, 4 for Tax")
    percentOperation = float((input(""))
    if percentOperation ==float("1"):
            
        pctNumber1 = float(input("Number 1: ")
        pctNumber2 = float(input("Number 2: ")
        pctMultiplicationAnswer = (pctNumber1 * pctNumber2)
        print(pctMultiplicationAnswer)
                
    if percentOperation ==float("2"):
        pctNumber1 = float(input("Number 1: ")
        pctNumber2 = float(input("Number 2: ")
        pctDivisionAnswer = (pctNumber1 * pctNumber2)
        print(pctDivisionAnswer)
        
    if percentOperation ==float("3"):
        currentValue = float(input("Current Value: "))
        percentOff = float(input("Percent Off (0.1-100%): "))
        percent = (percentOff/100)
        remaining = (1 - percent)
        pctDeductionAnswer = (currentValue / remaining)
        print(pctDeduction)
    
    if percentOperation ==float("4"):
        taxBefore = float(input("Original Amount: "))
        taxPct    = float(input("Tax Percent (0.1-100): "))
        taxPercentage = (taxPct / 100)
        taxedAmount = (taxBefore * taxPercentage)
        print(taxedAmount + taxBefore)


    else :
    Number1 = float(input("Number 1: "))
    Number2 = float(input("Number 2: "))
    multiplicationAnswer = float(Number1 * Number2)
    additionAnswer = float(Number1 + Number2)
    divisionAnswer = float(Number1 / Number2)
    subtractionAnswer = float(Number1 - Number2)
    if operation=="*" : (print(multiplicationAnswer))

    if operation=="+" : (print(additionAnswer))

    if operation=="/" : (print(divisionAnswer))

    if operation=="-" : (print(subtractionAnswer)))
