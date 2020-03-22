# from castervoice.lib.control import _NEXUS
from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly.engines import (_default_engine)
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data, Exclusiveness,GramAndRules
from castervoice.exclusiveness.disableR import disableR
from castervoice.exclusiveness.enableR import enableR
from castervoice.exclusiveness.setGramToBeExclusive import setGramToBeExclusive
from castervoice.exclusiveness.get_AllActiveRules import get_AllActiveRules


# def Set_Exclusiveness_ForRules(Rule):
def Set_Exclusiveness_ForRules(RulestoBeExclusive_className):
    #--- RulestoBeExclusive_className = list
    print "\n", "dbg20200317152040| Gonna set exclusiv for: @RulestoBeExclusive_className:", RulestoBeExclusive_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

    # print "\n", "20200112220615| New caster: exclusiveness for| RulestoBeExclusive_className:", RulestoBeExclusive_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    #--- Disable all Rules, except those we want to be exclusive.
    AllRules_className = [i.className for i in gl.allRegisteredRule]
    # print "\n", "20200316164931| AllRules_className:", AllRules_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    
    disableR(AllRules_className, RulestoBeExclusive_className)
    
    #--- Enable rule we want to be exclusive.
    enableR(RulestoBeExclusive_className)
    #--- Remember
    data.store_enablebRules_associatedWithApp(data.currWindHndl) #TODO: not sure if is correct.

    # print "\n", "20200319194948| gl.all_loadedRule_mappingRule:", [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # print "", "20200319194949| gl.all_Merge_result.all_rule_class_names:", gl.all_Merge_result.all_rule_class_names, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)


    #--- Set Exclusiveness of all grammsar in the system (_default_engine).
    #--- Set ExclusiveHook = true. (in C:\Users\HP\AppData\Local\caster\settings\hooks.toml)
    # setGramToBeExclusive(_default_engine.grammars) #comment out, bcz: using ExclusiveHook	instead	

    print "\n", "(exclusiveness) All Rules been Exclusive :", gl.RbeenExclusive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # print "\n", "(exclusiveness) All Rules been Exclusive :", get_AllActiveRules(), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)


