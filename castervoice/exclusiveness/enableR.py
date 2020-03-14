from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.lib.control import _NEXUS
# import inspect

def enableR(aRclassName):
	""" Enables Rules so they gonna be part of exclusiveness """
	 
	for iRclassName in aRclassName:

		# print "\n", "20200313195006| iRclassName:", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		if type(iRclassName) is not str: #bcz could be an object
			iRclassName = iRclassName.__class__.__name__
		if iRclassName	== "Rule": #skeep those with 'Rule(_IntegerRefST_xx)'. TODO: Better way to check?
			continue
		# print "\t", "20200313195007| iRclassName.__class__.__name__):", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

		# if iRclassName in Storage.RbeenExclusive:
		if iRclassName in gl.RbeenExclusive:
			continue
		# try:
		_NEXUS._grammar_manager._change_rule_enabled(iRclassName, True)
		gl.RbeenExclusive.append(iRclassName)
  
		# Storage.RbeenExclusive.add(iRclassName)

		# except:
		# 	winsound.PlaySound("C:\\- To Burn\\- Project My\\Sound My\\Alarm09.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		# 	print "\n", "20200112213925| got exception| iRclassName: ", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	raise ValueError("(see Print above)")
