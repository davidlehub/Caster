from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.lib.merge.mergerule import MergeRule


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

"""
Store: all rules been exclusive (been active).
This variable is equivalent of: (gl.all_Merge_result + gl.all_loadedRule_mappingRule), without the duplicates, like: 
    #--- (Concatonate/add 2 list without duplicate element)
    list(OrderedDict.fromkeys(gl.all_Merge_result.all_rule_class_names + [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]))
 """
RbeenActive = []
GbeenExclusive = [] #Grammars been exclusive.

#region--- to get all active rules: all_loadedRule_mappingRule + all_Merge_result 
all_loadedRule_mappingRule = []
""" (david)
Interesting: 'all_Merge_result.all_rule_class_names', exemple, = ['Alphabet', 'Navigation', 'Numbers', 'Punctuation', 'HistoryRule', 'ChainAlias', 'BringRule'] 
"""
all_Merge_result = None #'all_Merge_result' is type of <C:\Users\HP\Documents\Caster\castervoice\lib\merge\ccrmerging2\merge_result.py>
# all_loadedRule_mergeRule = [] #TODO: to delete
#endregion to get all active rules

# all_MappingRulesLoaded_className = []
#  all_MergeRulesLoaded_className = []

#__ Uniq Mode
UniqMode_NonCCR_ruleClass = None # type: MergeRule