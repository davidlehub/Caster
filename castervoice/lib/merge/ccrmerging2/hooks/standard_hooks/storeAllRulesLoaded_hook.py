#--- (David)
from inspect import getframeinfo, stack, getframeinfo, currentframe

from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

from castervoice.lib._tests.GlabalStorage.allGrammars import all_MappingRule_className, all_MergeRules_className

def storeAllRulesLoaded(merge_rules=None, mapping_rule=None, mappingRule_anabled=None):

    if merge_rules:
        # all_MergeRules_className = []

        for rule in merge_rules: # list
            # print "", "20200312151237| ",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
            #--- save those info globaly. Gonna needed for exclusiveness syst.
            if rule not in all_MergeRules_className:
                all_MergeRules_className.append(rule.get_rule_class_name())
	    # print "\n", "20200312212545| all_MergeRules_className:", all_MergeRules_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

    elif mapping_rule: # Not a list
        if mappingRule_anabled:
            all_MappingRule_className.append(mapping_rule.get_rule_class_name())
        elif not mappingRule_anabled:
            try:
                all_MappingRule_className.remove(mapping_rule.get_rule_class_name())
            except:
                pass
            

class storeAllRulesLoadedHook(BaseHook):
    def __init__(self):
        super(storeAllRulesLoadedHook, self).__init__(EventType.RULES_LOADED_EXCL)

    def get_pronunciation(self):
        return "rule storage"

    def run(self, event_data):
        merge_rules = event_data.active_mrs
        mapping_rule = event_data.managed_rule
        mappingRule_anabled = event_data.mappingRule_anabled
        
        storeAllRulesLoaded(merge_rules, mapping_rule, mappingRule_anabled)

def get_hook():
    return storeAllRulesLoadedHook