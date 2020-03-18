def setGramToBeExclusive(aGramObj):
	for iG in aGramObj:
		# makeSureGramIsLoadedEnabled([iG])
	 
		iG.set_exclusiveness(1)
		print "", "20200316172015| grammar with exclusiveness = 1:", iG.name

		# GramHavingDeactivatingRules = makeSureRulesOfGramAreActivated_forNoMerged([iG]) 		
