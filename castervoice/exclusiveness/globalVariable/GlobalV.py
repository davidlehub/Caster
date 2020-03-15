from inspect import getframeinfo, stack, getframeinfo, currentframe

# RulesCasterAlwayNeed_className = ['GrammarActivatorRule','HooksActivationRule','TransformersActivationRule']
RulesCasterAlwayNeed_className = {'GrammarActivatorRule','HooksActivationRule','TransformersActivationRule'}


all_MergeRule = set()
all_MappingRule = set()

""" 
    - To have a rule details use '.get_details()', ex: Rdetail = rule.get_details()
    Rdetail.name:
    Rdetail.function_context:
    Rdetail.executable:
    Rdetail.title:
    Rdetail.grammar_name:
    Rdetail.declared_ccrtype:
    Rdetail.transformer_exclusion:
    Rdetail.watch_exclusion:
    Rdetail._filepath:
 """
all_RuleHavingAppContext = set() 

prevWindHndl_onlyUseToDectectNewApp = None
RbeenExclusive = set()
