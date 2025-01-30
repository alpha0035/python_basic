# A function defined inside another function
# can access variables of the enclosing scope

def outFunc():
    s = 'alpha'
    print("Outer function " + s)
    def innerFunc():
        print("Inner fuction "+s)
    innerFunc()
outFunc()