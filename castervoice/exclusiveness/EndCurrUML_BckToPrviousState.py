from inspect import getframeinfo, stack, getframeinfo, currentframe

def EndCurrUML_BckToPrviousState(): #20191123223011
    print "\n", "!!20200323233645| Not Implemented yet.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    return
    
    print "\n-->20181122065858| in def EndCurrUML_BckToPrviousState:"

    global TamFc
    if TamFc not in sys.modules:
        print "\n---20181123201053| in :if TamFc not in sys.modules"
        from rules.lib import TamFunction as TamFc

    #--{Test 20181119105244: end of uniq mode layer
    #-- TODO: change it to be more relate with Uniq mode...
    TamFc.backOneLevelOfUML() #20191123223135

    #-- show info
    print "\n|~20191121231633| Done Processing back, of 1 level of UniqMode|", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    TamFc.ShoInf_thingzBnExclusiv()
    #-- }Test 20181119105244
