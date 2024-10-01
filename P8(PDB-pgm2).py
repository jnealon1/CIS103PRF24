# property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    print('\n'*2)
    AssessmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = getinput('Enter value of property: ')
    LocalTaxRate = getinput('Enter loacal tax rate: ')
    StateEqualizer = getinput('Enter state equalizer rate: ')
    print('\n'*2)
    AssessedValue= PropertyValue * AssessmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n'*2)
    print(' Property tax due: ',TotalPropertyTax)
    print('\n'*2)
    return
main()
