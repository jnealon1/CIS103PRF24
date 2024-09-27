# property tax calculator 1
def part1():
    nheac = .004
    mwrdc = .406
    pmab = .006
    cpd = .362
    MiscTx = nheac + mwrdc + pmab + cpd
    return MiscTx
def part2():
    bec = 3.726
    cccd = .169
    Schooltax = bec + cccd
    return Schooltax
def part3():
    csbif=.128
    clf=.122
    city = 1.630
    City = csbif + clf + city    
    return City
def part4():
    ccfpd = .063
    cook = .316
    ccps = .130
    cchf = .087
    CookCty = ccfpd + cook + ccps + cchf
    return CookCty
def main():
    print('--------------------------------')
    mt = part1()
    st = part2()
    ct = part3()
    cc = part4()
    TotalTaxRate = mt + st + ct + cc
    print('Property Tax Rate is: ', TotalTaxRate)
main()
