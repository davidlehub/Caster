from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data,GramAndRules
from castervoice.exclusiveness import Constant as ct

def store_AllEnabledRule_ofApp(aWindHndl, aForce = False):
	if not data.prevWindHndl and not aForce:
		return

	# #--- instatiate
	# if not data.appGramAndRules.has_key(aWindHndl): data.appGramAndRules[ct.default] = GramAndRules()

	#--- do it
	data.makeAcopy_AllEnabledRule(aWindHndl)

	print "\n", "dbg20200322191551| done: data.makeAcopy_AllEnabledRule(aWindHndl).",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	#region--- (old caster
	# data.makeAcopy_AllEnabledRule(aWindHndl)
	# data.makeAcopy_engineGrammars(aWindHndl)
	# data.makeAcopy_NexusMergerConfigs(aWindHndl)
	#endregion (old caster
