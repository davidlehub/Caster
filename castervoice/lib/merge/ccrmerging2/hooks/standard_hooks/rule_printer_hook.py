from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

def RulePrinter(merge_rules=None, mapping_rule=None):

    if merge_rules:
        for rule in merge_rules: # list
            # list, hook runs runs once per update of merge_rules
            # Update: entire merge_rules list each update
            print("merge_rules:   ", str(rule.get_rule_class_name()))
            #for item in rule._rule_class.mapping.items():
            #    print(item[0])   # spec
            #    print(item[1])   # action
            #    print("")        # divider (optional)
            #    break
    
    elif mapping_rule: # Not a list

        #  On start hook runs for all Rule one at a time.
        #  On update: hook runs for on updated rule only.
        print("mapping_rule:   ", str(mapping_rule.get_rule_class_name()))
        #for item in mapping_rule._rule_class.mapping.items():
        #    print(item[0])   # spec
        #    print(item[1])   # action
        #    print("")        # divider (optional)
        #    break

    print("===================================================")        # divider (optional)

class RulePrinterHook(BaseHook):
    def __init__(self):
        super(RulePrinterHook, self).__init__(EventType.RULES_LOADED)

    def get_pronunciation(self):
        return "rule printer"

    def run(self, event_data):
        merge_rules = event_data.active_mrs
        mapping_rule = event_data.managed_rule
        RulePrinter(merge_rules, mapping_rule)

def get_hook():
    return RulePrinterHook