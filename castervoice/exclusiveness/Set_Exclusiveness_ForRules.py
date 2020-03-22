# from castervoice.lib.control import _NEXUS
from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly.engines import (_default_engine)
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data, Exclusiveness,GramAndRules
from castervoice.exclusiveness.disableR import disableR
from castervoice.exclusiveness.enableR import enableR
from castervoice.exclusiveness.setGramToBeExclusive import setGramToBeExclusive


# def Set_Exclusiveness_ForRules(Rule):
def Set_Exclusiveness_ForRules(RulestoBeExclusive_className):
    print "\n", "ici 20200317152040| Gonna set exclusiv for: @RulestoBeExclusive_className:", RulestoBeExclusive_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    #--- RulestoBeExclusive_className = list
    # return

    # --- list of rule we want to be exclusive
    # RulestoBeExclusive_className = RulestoBeExclusive_className # | gl.RulesToBeAlwayExclusive_className #the 'RulesToBeAlwayExclusive_className' is added outside of this methode. bcz there is case we don't need it. 
    # RulestoBeExclusive_className = RulestoBeExclusive_className | gl.RulesToBeAlwayExclusive_className
    # RulestoBeExclusive_className = RulestoBeExclusive_className + gl.RulesToBeAlwayExclusive_className
    # RulestoBeExclusive_className = Rule.get_rule_class_name() + gl.RulesToBeAlwayExclusive_className


    # print "\n", "20200112220615| New caster: exclusiveness for| RulestoBeExclusive_className:", RulestoBeExclusive_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    #--- Diable all Rules, except those we want to be exclusive.
    # AllRules = gl.all_MappingRule |  gl.all_MergeRule
    # AllRules_className = set([i.get_rule_class_name() for i in AllRules])
    # AllRules_className = set([i.className for i in gl.allRegisteredRule])
    AllRules_className = [i.className for i in gl.allRegisteredRule]
    # print "\n", "20200316164931| AllRules_className:", AllRules_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    
    # print "\n", "20200319192135| RulestoBeExclusive_className:", RulestoBeExclusive_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # disableR(AllRules, RulestoBeExclusive_className)
    disableR(AllRules_className, RulestoBeExclusive_className)
    
    # disableR(_NEXUS._grammar_manager._config.get_enabled_rcns_ordered(),RulestoBeExclusive_className)

    #--- Enable rule we want to be exclusive.
    enableR(RulestoBeExclusive_className)
    #--- Remember
    data.store_enablebRules_associatedWithApp(data.currWindHndl) #TODO: not sure if is correct.

    print "\n", "20200319194948| gl.all_loadedRule_mappingRule:", [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    print "\n", "20200319194949| gl.all_Merge_result.all_rule_class_names:", gl.all_Merge_result.all_rule_class_names, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # print "\n", "20200319194949| gl.all_loadedRule_mergeRule:", [i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

    #--- Set Exclusiveness of all grammar in the system (_default_engine).
    setGramToBeExclusive(_default_engine.grammars)		

    print "\n", "(exclusiveness) All Rules been Exclusive :", gl.RbeenExclusive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

