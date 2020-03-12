#--- (David)
from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

from castervoice.lib._tests.GlabalStorage.allGrammars import all_MappingRule_className, all_MergeRules_className

def storeAllRulesLoaded(merge_rules=None, mapping_rule=None):

    if merge_rules:
        #region--- (david)
        all_MergeRules_className = []
        #endregion 

        for rule in merge_rules: # list
            #---(david) save those info globaly. Gonna needed for exclusiveness syst.
            all_MergeRules_className.append(rule.get_rule_class_name())

            # print("get_rule_instance:   ", str(rule.get_rule_instance()))
            # print("get_rule_class:   ", str(rule.get_rule_class()))
    
    elif mapping_rule: # Not a list
        #--- save those info globaly. Gonna needed for exclusiveness syst.
        #--- [] hmm, how to reset the variable 'all_MappingRule_className', since 'mapping_rule' is not a list
        #--- 
        all_MappingRule_className.append(mapping_rule.get_rule_class_name())

        # print("get_rule_instance:   ", str(mapping_rule.get_rule_instance()))
        # print("get_rule_class:   ", str(mapping_rule.get_rule_class()))

class storeAllRulesLoadedHook(BaseHook):
    def __init__(self):
        super(storeAllRulesLoadedHook, self).__init__(EventType.RULES_LOADED)

    def get_pronunciation(self):
        return "rule storage"

    def run(self, event_data):
        merge_rules = event_data.active_mrs
        mapping_rule = event_data.managed_rule
        storeAllRulesLoaded(merge_rules, mapping_rule)

def get_hook():
    return storeAllRulesLoadedHook