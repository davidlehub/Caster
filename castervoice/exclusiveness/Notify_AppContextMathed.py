from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules


# def Notify_AppContextMathed(aAppContext_data): #id20200315080523
def Notify_AppContextMathed(executable,title,handle): #id20200315080523
    #--- executable: ex: ['code']


    # print "\n", "20200315135625| executable:", executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # pass

    #region--- set exclusiveness For Rule(S) related to the matched App context

    #--- Find out witch rule matched..
    # gl.all_MappingRule
    # gl.all_MergeRule
    print "", "gl.all_RuleHavingAppContext:",gl.all_RuleHavingAppContext
    
    RulesMatchingCurrAppContext_className = set()
    for R in gl.all_RuleHavingAppContext:
        Rdetail = R.get_details()
        #--- TODO: Filter/validate also using: title
        print "\n", "ici 20200315151660| Rdetail.executable:",Rdetail.executable,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        print "\n", "ici 20200315151658| executable:",executable,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        #--- (Rdetail.executable= ,exemple, 'code')
        if Rdetail.executable in executable:
            print "\n", "20200315150947| (exclusiveness) App Context matched. So gonna set exclusivenss for: Rdetail._filepath: ",Rdetail._filepath,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
            RulesMatchingCurrAppContext_className.add(R.get_rule_class_name())
            
    Set_Exclusiveness_ForRules(RulesMatchingCurrAppContext_className)
            # Set_Exclusiveness_ForRules(R)
            
        
    
    #endregion set exclusiveness For Rule(S) related to the matched App context

    