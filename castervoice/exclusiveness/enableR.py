def enableR(aRclassName):
	""" Enables Rules so they gonna be part of exclusiveness """

	for iRclassName in aRclassName:
		if iRclassName in Storage.RbeenExclusive:
			continue
		# try:
		_NEXUS._grammar_manager._change_rule_enabled(iRclassName, True)
		# Storage.RbeenExclusive.add(iRclassName)

		# except:
		# 	winsound.PlaySound("C:\\- To Burn\\- Project My\\Sound My\\Alarm09.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		# 	print "\n", "20200112213925| got exception| iRclassName: ", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	raise ValueError("(see Print above)")
