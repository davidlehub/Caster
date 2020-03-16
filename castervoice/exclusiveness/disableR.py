from castervoice.lib.control import _NEXUS
from castervoice.exclusiveness.globalVariable import GlobalV as gl

def disableR(aRclassName,aExceptR=[]):
	for iRclassName in aRclassName:
		if iRclassName in aExceptR:
			# gl.RbeenExclusive.add(iRclassName)
			continue
		# try:
		_NEXUS._grammar_manager._change_rule_enabled(iRclassName, False)
		gl.RbeenExclusive.discard(iRclassName)
		# except:
		# 	winsound.PlaySound("C:\\- To Burn\\- Project My\\Sound My\\Alarm09.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		# 	print "\n", "20200112213924| got exception with '_NEXUS._grammar_manager._change_rule_enabled'| iRclassName: ", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	raise ValueError("(see Print above)")
