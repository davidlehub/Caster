from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.cls.DragonVocabulary_cls import enable_dragonVocabulary,disable_dragonVocabulary,dragonVocabulary_is_Disabled, dragonVocabulary_is_Enabled,enable_temporary_dragonVocabulary, disable_temporary_dragonVocabulary, dragonVocabulary_wasTemporary_disable, dragonVocabulary_wasTemporary_enabled,indicate_DragonVocabulary_is_Disabled
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.reStore_AllEnabledRule_ofApp import reStore_AllEnabledRule_ofApp
from castervoice.exclusiveness.get_currUniqModeLayer_ofApp import get_currUniqModeLayer_ofApp
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules
from castervoice.exclusiveness import Constant as ct


# def BackToPreviousState_OfCurrApp(aContextGram):
def BackToPreviousState_OfCurrApp():
	""" Back to the state this new app was,
		if it was been in excluseness state (eg: was in Uniq mode layer).
		So, the fflowing things gonna be set exclusiveness:
		- Normal Grammar that was been exclusive
		- all grammars of _Nexus merger
		- all the merged rule >> currMergedCcRule_inf
		- (but not the grammar in >> retGrmAndRule['grammar']
	 """
	
	#region--- (deprecated with new Caster)
	#--- Case: Current App has data previously stored
	# if data.appExclusiveness.has_key(data.currWindHndl): 

	# #--- Put back grammar and rules for the app
	# print "\n|~ici20191218191823| Put back grammar and rules for curr app." , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# # reStore_AllEnabledRule_ofApp(data.currWindHndl)  
	# data.putBack_AllEnabledRule(data.currWindHndl)
	#endregion (deprecated with new Caster)

	#region 20191207150310: Back to previous state of exclusiveness.  
	#--== Any UML layer?
	# print "\n|~ici 20191207003726| data.count_UML_ofApp(data.currWindHndl):",data.count_UML_ofApp(data.currWindHndl) , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	if bool(False): #for new Caster, no need this 'if'. So we jump to 'else' part.
	# if data.count_UML_ofApp(data.currWindHndl) > 0:
		#-- activate excluseveness the grammar of that UML
		currUML = get_currUniqModeLayer_ofApp(data.currWindHndl)

		# #-- Triggering the merging process to update merged things . We give a bogus rule pronunciation.
		# print "\n|>0-20191218122310| Using a 'bogusPronun' to Trigger the merging process, to update merged things (eg.CCR rules).",":->In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s|%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# MergeRulePronun(bogusPronun, False, False)		

		#____ restore exclusive state
		restored_RbeenExclusive = list(currUML.RbeenExclusive_stored)
		print "\n|dbg20191208170030| set back exclusiveness of UML| restored_RbeenExclusive",restored_RbeenExclusive,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		#__ 
		Set_Exclusiveness_ForRules(restored_RbeenExclusive)


	#--== 
	else: #No any UML layer
		#---== Set back Excluvenisse of where it was
		# Exclusiveness.getAllGram()
		#--- for 'Normal' Grammars 
		# enableR(data.restore_enablebRules_associatedWithApp(data.currWindHndl)) #not sure if this is ok with new Caster. Or the line below.
		restoredRules_className = data.restore_enablebRules_associatedWithApp(data.currWindHndl)
		# print "\n", "dbg20200322135904| back to previoustate | restoredRules_className:",restoredRules_className,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

		Set_Exclusiveness_ForRules(restoredRules_className)

		#__ also restore the state of the speech engine
		restoredState_ofSpeechEngine = data.store_speechEngineState_associatedWithApp(data.currWindHndl)
		if restoredState_ofSpeechEngine == ct.enabled_state:
			enable_dragonVocabulary()
		else:
			disable_dragonVocabulary()


#endregion

	# #--- Case: Current App doesn't have any data previously stored 
	# else:
	# 	#--- put back the 'default' things
	# 	print "\n|~ici 20191215133611| put back the 'default' things.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	reStore_AllEnabledRule_ofApp(ct.default) #no need to have a methode?.
	# 	# data.putBack_AllEnabledRule(ct.default)



	#region--- (old caster)
	# """ Back to the state this new app was,
	# 	if it was been in excluseness state (eg: was in Uniq mode layer).
	# 	So, the fflowing things gonna be set exclusiveness:
	# 	- Normal Grammar that was been exclusive
	# 	- all grammars of _Nexus merger
	# 	- all the merged rule >> currMergedCcRule_inf
	# 	- (but not the grammar in >> retGrmAndRule['grammar']
	#  """
	
	# #--- Main condition
	# # if not data.appExclusiveness.has_key(data.currWindHndl):
	# # 	return

	# if data.appExclusiveness.has_key(data.currWindHndl): 
	# 	#--- Put back grammar and rules for the app
	# 	print "\n|~ici20191218191823| Put back grammar and rules for curr app." , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	reStore_AllEnabledRule_ofApp(data.currWindHndl)  
	
	# 	#region 20191207150310: Back to previous state of exclusiveness.  
	# 	#--== Any UML layer?
	# 	# print "\n|~ici 20191207003726| data.count_UML_ofApp(data.currWindHndl):",data.count_UML_ofApp(data.currWindHndl) , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	if data.count_UML_ofApp(data.currWindHndl) > 0:
	# 		#-- activate excluseveness the grammar of that UML
	# 		# currUML = data.getTop_UML_ofApp(data.currWindHndl)
	# 		currUML = get_currUniqModeLayer_ofApp(data.currWindHndl)
	# 		# do_backOneLevelOfUML(currUML)

	# 		# #-- Triggering the merging process to update merged things . We give a bogus rule pronunciation.
	# 		# print "\n|>0-20191218122310| Using a 'bogusPronun' to Trigger the merging process, to update merged things (eg.CCR rules).",":->In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s|%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		# MergeRulePronun(bogusPronun, False, False)		

	# 		# enableR(currUML["thingsToBeUniq"])
	# 		# setExclusivForGram_andMemorise(currUML["thingsToBeUniq"])
	# 		print "\n|~ici 20191208170030| set back exclusiveness| currUML['thingsToBeUniq']:", currUML["thingsToBeUniq"], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		SetThingzToBeExclusive(currUML["thingsToBeUniq"], [], [], "Back To PreviousState _Of CurrApp")

	# 		#--== Make sure the Merged Gram are been exclusive:
	# 		# retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = getMergedRules_obj() 
	# 		# enableR(retGrmAndRule['grammar'])
	# 		setExclusivFor_MergedGram()  
	# 	#--== 
	# 	else: #No any UML layer
	# 		#---== Set back Excluvenisse of where it was
	# 		# Exclusiveness.getAllGram()
	# 		#--- for 'Normal' Grammars 
	# 		enableR(data.restore_enablebRules_associatedWithApp(data.currWindHndl))
	# 		#--- for 'non' CCR Grammars 
	# 		enableR(data.getFrmMemory_CcrNonGram(data.currWindHndl))
	# 		#--- for CCR merged rules
	# 		# unmergeCcRules(data.getFrmMemory_MergedRule_zip(data.currWindHndl))
	# 		mergeCcRules(data.getFrmMemory_MergedRule_zip(data.currWindHndl))
	# 		# enableR()

	# 		# #--- SEt eclusiveness for Merged grammar that have to be alway exclusive
	# 		# retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = getMergedRules_obj()
	# 		# enableR(retGrmAndRule['grammar'])
			
	# 		#--== Make sure the Merged Gram are been exclusive:
	# 		# retAllCompositeMergedRules, retGrmAndRule, currMergedCcRule_inf = getMergedRules_obj() 
	# 		# enableR(retGrmAndRule['grammar'])
	# 		setExclusivFor_MergedGram()    

	# 		# print "\n|>-00-20191206190519|: ",[i.name for i in CurrUniqModeLayer["bkp_GramzBeenExclusi"]],":->In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s|%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		# SetThingzToBeExclusive(CurrUniqModeLayer["bkp_GramzBeenExclusi"], [],[], Why + "20181119222053")
	# 		# enableR(data.restore_enablebRules_associatedWithApp(data.currWindHndl))
			
	# 		# if type(aContext) is AppContext and not isMergedGram(aContextGram):
	# 		# 	print "\n|~ici 20191208170031| Set BACK exclusiv for cur App.", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		# 	enableR(aContextGram)

	# 			# enableR(aContextGram)
	# 		# data.memoriseAppExclusiveness(iG) 
	# 	#endregion 

	# else:
	# 	#--- put back the 'default' things
	# 	# print "\n\n|~ici 20191215133611| put back the 'default' things.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	#- (before vers  20200109170619)
	# 	reStore_AllEnabledRule_ofApp(ct.default)
	# 	#- (vers 20200109170619)
	# 	# try:
	# 	# 	reStore_AllEnabledRule_ofApp(ct.default)
	# 	# except:
	# 	# 	data.appGramAndRules[ct.default] = GramAndRules()			

	#endregion 	
