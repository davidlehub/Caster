from inspect import getframeinfo, stack, getframeinfo, currentframe


# ,'CasterRule', 'HardwareRule','DragonRule'
# ,'Alphabet'}


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
allRegisteredRule = set() #elements are of type: C:\Users\HP\Documents\Caster\castervoice\exclusiveness\globalVariable\registeredRule_data.py
allRegisteredRule_HavingAppContext = set() #elements are of type: C:\Users\HP\Documents\Caster\castervoice\exclusiveness\globalVariable\registeredRule_data.py
all_RuleHavingAppContext_className = set() 
allRules_className = set()

prevWindHndl_onlyUseToDectectNewApp = None
RbeenExclusive = []

all_loadedRule_mappingRule = []
all_loadedRule_mergeRule = []
# all_MappingRulesLoaded_className = []
#  all_MergeRulesLoaded_className = []
