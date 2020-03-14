from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.lib._tests.GlabalStorage.allGrammars import all_MappingRule_className, all_MergeRules_className
from castervoice.lib.control import _NEXUS
from dragonfly.engines import (_default_engine)
from castervoice.exclusiveness.globalVariable import GlobalV as gl



def SetRuleToBeExclusive(aRuleClassNames):
    #--- aRuleClassNames = list
    

	RweWantToBeExclusive = aRuleClassNames
	RtoBeExclusive =  RweWantToBeExclusive + gl.RcasterAlwayNeed
 
	#--- Diable all Rules, except those we want to be exclusive.
	# disableR(_NEXUS._grammar_manager._config.get_enabled_rcns_ordered(),RtoBeExclusive)
	# def disableR(aRclassName,aExceptR=[]):
		# for iRclassName in aRclassName:
		# 	if iRclassName in aExceptR:
		# 		Storage.RbeenExclusive.add(iRclassName)
		# 		continue
		# 	_NEXUS._grammar_manager._change_rule_enabled(iRclassName, False)
		# 	Storage.RbeenExclusive.discard(iRclassName)

	AllRules = all_MappingRule_className +  all_MergeRules_className #!? all_MergeRules_className is empty!?
	
	for iRclassName in AllRules:
		if iRclassName in RtoBeExclusive:
			continue
		_NEXUS._grammar_manager._change_rule_enabled(iRclassName, False)
		# print "\n", "20200312210240| Follow rule (class name) is disabled:", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	#--- Enable rule we want to be exclusive.
	# enableR(RtoBeExclusive)
	# def enableR(aRclassName):
		# """ Enables Rules so they gonna be part of exclusiveness """

		# for iRclassName in aRclassName:
		# 	if iRclassName in Storage.RbeenExclusive:
		# 		continue
		# 	# try:
		# 	_NEXUS._grammar_manager._change_rule_enabled(iRclassName, True)
	for iRclassName in RtoBeExclusive:
		# if iRclassName in Storage.RbeenExclusive:
		# 	continue
		_NEXUS._grammar_manager._change_rule_enabled(iRclassName, True)
		# print "\n", "20200312210241| Follow rule (class name) is enable:", iRclassName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)



	#--- Remember
	# data.store_enablebRules_associatedWithApp(data.currWindHndl)


	#--- Set Exclusiveness of all grammar in the system (_default_engine). (_default_engine.grammars)
	# setGramToBeExclusive(_default_engine.grammars)		
	# def setGramToBeExclusive(aGramObj):
		# for iG in aGramObj:
		# 	# makeSureGramIsLoadedEnabled([iG])
		
		# 	iG.set_exclusiveness(1)
	for iG in _default_engine.grammars:
		iG.set_exclusiveness(1)		
		# print "", "20200312210242| Follow grammar are set to be exclusive:", iG, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)


	#--- Info the user:
	print "\n", "(Exclusiveness) Only those rules are available:", gl.RbeenExclusive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# print "\n", "(Exclusiveness) Only those rules are available:", RweWantToBeExclusive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# print "\n\t", "*** GUIDE: Try to say 'arch' (alphabet) or 'sure stoosh' (navigationNon)."

	#endregion  