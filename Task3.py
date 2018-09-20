password_list = {"chris":"helloworld", "john":"passw1", "nelly":"2hell1", "wendy":"1Passw"}
 
def pwfinder(pwlist):
 
    global hasUpper
    global hasDigit
    global is6Digit
    for value in pwlist.values():
        hasDigit = False
        hasUpper = False
        is6Digit = False
 
        if len(value) < 6:
            is6Digit = False
        elif len(value) > 6:
            is6Digit = False
        else:
            is6Digit = True
 
        valuearray = list(value)
        for c in valuearray:
            if c.isdigit():
                hasDigit = True
            elif c.isupper():
                hasUpper = True
 
        if hasUpper is True and hasDigit is True and is6Digit is True:
            print("The password " + value + " matches your criteria!")
            hasDigit = False
            hasUpper = False
            is6Digit = False
 
 
pwfinder(password_list)