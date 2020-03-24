from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.const import CCRType

class UniqMode_NonCCR(MergeRule): # (note: this an exmple of using 'MergeRule' without making it been CCR)
	name = ""
	mapping = {
		"!!!": {}
	}
def get_rule():
	
	# print "\n", "20200324004713| Callers::",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# for i in range(1, 16):
	# 	try:
	# 		print "\t","",stack()[i][3],"%s:%d" % (getframeinfo(stack()[i][0]).filename, getframeinfo(stack()[i][0]).lineno)    
	# 	except:
	# 		print ""
	# 		break    
	return UniqMode_NonCCR, RuleDetails(ccrtype=CCRType.GLOBAL)         
	# return UniqMode_NonCCR, RuleDetails(name=UniqMode_NonCCR.name,ccrtype=CCRType.GLOBAL)         
	# return UniqModeLayer, RuleDetails(name="caster rule")             