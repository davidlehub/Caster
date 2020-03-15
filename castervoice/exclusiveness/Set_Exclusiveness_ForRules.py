# from castervoice.lib.control import _NEXUS
from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly.engines import (_default_engine)
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data, Exclusiveness,GramAndRules
from castervoice.exclusiveness.disableR import disableR
from castervoice.exclusiveness.enableR import enableR
from castervoice.exclusiveness.setGramToBeExclusive import setGramToBeExclusive


# def Set_Exclusiveness_ForRules(Rule):
def Set_Exclusiveness_ForRules(Rules_className):
    #--- Rules_className = list

    #--- list of rule we want to be exclusive
    RulestoBeExclusive_className = Rules_className | gl.RulesCasterAlwayNeed_className
    # RulestoBeExclusive_className = Rules_className + gl.RulesCasterAlwayNeed_className
    # RulestoBeExclusive_className = Rule.get_rule_class_name() + gl.RulesCasterAlwayNeed_className

    # print "\n", "20200112220615| New caster: exclusiveness for| RulestoBeExclusive_className:", RulestoBeExclusive_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    #--- Diable all Rules, except those we want to be exclusive.
    AllRules = gl.all_MappingRule |  gl.all_MergeRule
    # new_list = [expression(i) for i in old_list if filter(i)]
    AllRules_className = [i.get_rule_class_name() for i in AllRules]
    print "\n", "ici 20200315150841| AllRules_className:", AllRules_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    AllRules_className = set(AllRules_className)
    print "", "ici 20200315150842| AllRules_className:", AllRules_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # disableR(AllRules, RulestoBeExclusive_className)
    # # disableR(_NEXUS._grammar_manager._config.get_enabled_rcns_ordered(),RulestoBeExclusive_className)

    # #--- Enable rule we want to be exclusive.
    # enableR(RulestoBeExclusive_className)
    # #--- Remember
    # data.store_enablebRules_associatedWithApp(data.currWindHndl) #TODO: not sure if is correct.

    # #--- Set Exclusiveness of all grammar in the system (_default_engine). (_default_engine.grammars)
    # setGramToBeExclusive(_default_engine.grammars)		

    # print "\n", "(exclusiveness) All Rules been Exclusive :", gl.RbeenExclusive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

