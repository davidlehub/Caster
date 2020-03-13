from castervoice.lib._tests.GlabalStorage.allGrammars import all_MappingRule_className, all_MergeRules_className
from castervoice.lib.control import _NEXUS
from dragonfly.engines import (_default_engine)


def OnFocusedWindowChanged():
	pass

	#region--- Quick test: set esclusive = 1, for: 
	# "NavigationNon" and "Alphabet"

	RweWantToBeExclusive = ["Alphabet",  "NavigationNon"]
	RcasterAlwayNeed = ['GrammarActivatorRule','HooksActivationRule','TransformersActivationRule']
	RtoBeExclusive = RcasterAlwayNeed + RweWantToBeExclusive

	#--- Diable all Rules, except those we want to be exclusive.
	# disableR(_NEXUS._grammar_manager._config.get_enabled_rcns_ordered(),RtoBeExclusive)
	# def disableR(aRclassName,aExceptR=[]):
		# for iRclassName in aRclassName:
		# 	if iRclassName in aExceptR:
		# 		Storage.RbeenExclusive.add(iRclassName)
		# 		continue
		# 	_NEXUS._grammar_manager._change_rule_enabled(iRclassName, False)
		# 	Storage.RbeenExclusive.discard(iRclassName)

	AllRules = all_MappingRule_className +  all_MergeRules_className
	# for iRclassName in _NEXUS._grammar_manager._config.get_enabled_rcns_ordered():
	for iRclassName in AllRules:
		if iRclassName in RtoBeExclusive:
			continue
		_NEXUS._grammar_manager._change_rule_enabled(iRclassName, False)

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


	#endregion  