def DragonModeOnly(aEnableExclusiveMode=False):
	''' Dragon Naturally speaking vocabulary with Caster. (no any Cster exlsuiveness).
	'''
	# print "\n-20181130202025|",":->In:",stack()[0][3],"%s:%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# why = "Unset all so only Dragon grammar is active. |20181130061141"

	# ExclusivMode.set_enabled(False,"20181217193712| Activating Dragon Mode only.")
	ExclusivMode.set_enabled(aEnableExclusiveMode,"20181217193712| Activating Dragon Mode only.")

	bkp_GramzBeenExclusi = data.restore_enablebRules_associatedWithApp(data.currWindHndl)

	unsetExclusivenessForGram(data.restore_enablebRules_associatedWithApp(data.currWindHndl))

	#region--- (TD: To upgrade for new Caster)
	print "\n", "TD 20200111180545| To upgrade for new Caster:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)	
	# unsetExclusivenessForGram(_NEXUS.merger._grammars)
	#endregion 

	return bkp_GramzBeenExclusi
