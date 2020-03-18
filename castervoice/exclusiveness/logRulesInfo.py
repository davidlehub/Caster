from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.lib.control import _NEXUS
from castervoice.lib.ctrl.mgr.grammar_manager import GrammarManager

""" 
-for: '_NEXUS._grammar_manager' members:
	C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\grammar_manager.py
-when Iterating Through '_NEXUS._grammar_manager._managed_rules' (a dict.), like:
	- 'for RclasssName, R in _NEXUS._grammar_manager._managed_rules.items():'
	- for 'R' members:
		C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\managed_rule.py
 """

def logRulesInfo():
	# ManagedRule.get_rule_instance
	# print "\n", "20200318144942| _NEXUS._grammar_manager._managed_rules:", _NEXUS._grammar_manager._managed_rules, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	print "\n", "20200318144942| '_managed_rules' info:", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	for RclasssName, R in _NEXUS._grammar_manager._managed_rules.items():
		print "\t", "RclasssName:", RclasssName
		print "\t", "R.get_rule_instance().active:", R.get_rule_instance().active    
		print "\t", "R.get_rule_instance().enabled:", R.get_rule_instance().enabled