import math
operation = input("Operation: ")

if operation=="dtrigonometry" or operation=="degreetrig" or operation=="dtrig" :
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

    if operation=="-" : (print(subtractionAnswer))
