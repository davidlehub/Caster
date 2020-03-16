def setGramToBeExclusive(aGramObj):
	for iG in aGramObj:
		# makeSureGramIsLoadedEnabled([iG])
	 
		iG.set_exclusiveness(1)
		print "\n", "20200316172015| grammar with exsl = 1: ig.name:", iG.name

		# GramHavingDeactivatingRules = makeSureRulesOfGramAreActivated_forNoMerged([iG]) 		
