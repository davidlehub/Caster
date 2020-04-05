from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data,GramAndRules
from castervoice.exclusiveness import Constant as ct
from castervoice.exclusiveness.globalVariable.Data_Manager import data

# def store_AllEnabledRule_ofApp(aWindHndl):
def store_AllEnabledRule_ofApp(aWindHndl, aForce = False):
	# if not data.prevWindHndl:
	if not data.prevWindHndl and not aForce:
		return

	# #--- instatiate
	# if not data.appGramAndRules.has_key(aWindHndl): data.appGramAndRules[ct.default] = GramAndRules()

	#--- do it
	# data.makeAcopy_AllEnabledRule(aWindHndl)
	data.store_enablebRules_associatedWithApp(data.prevWindHndl) # is 'data.prevWindHndl', not 'data.currWindHndl'
	# print "\n", "dbg20200322191551| Exclusive state saved.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# print "", "dbg20200322191551b| data.store_enablebRules_associatedWithApp(data.prevWindHndl):", data.restore_enablebRules_associatedWithApp(data.prevWindHndl),  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	#__ also store speech engine state
	data.store_speechEngineState_associatedWithApp(data.prevWindHndl)

	#region--- (old caster
	# data.makeAcopy_AllEnabledRule(aWindHndl)
	# data.makeAcopy_engineGrammars(aWindHndl)
	# data.makeAcopy_NexusMergerConfigs(aWindHndl)
	#endregion (old caster
