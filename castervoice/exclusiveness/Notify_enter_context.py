#region--- (import)
from dragonfly.grammar.grammar_base import Grammar


from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import AppContext, Window
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.processExclusivForNewApp import processExclusivForNewApp
from castervoice.exclusiveness.isMergedGram import isMergedGram
from castervoice.exclusiveness.isInUniqModeForCurrApp import isInUniqModeForCurrApp
from castervoice.exclusiveness.setExclusivForGram_andMemorise import setExclusivForGram_andMemorise
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.SetRuleToBeExclusive import SetRuleToBeExclusive


# from castervoice.exclusiveness.globalVariable.Data_Manager import data_manager as data
# from castervoice.exclusiveness.globalVariable import Data_Manager
# from castervoice.exclusiveness.globalVariable.Data_Manager import data as data


#endregion (import)


def Notify_enter_context(aGram,aContext):
    #--- aGram = , exemple, 'g25' || aContext = , exemple, 'AppContext(['code'], ['visual studio code'], False)'

	# print "\n|~ 20191211131932| aGram,aContext: ", aGram, aContext," || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# print "\n|~ 20191211131932| aContext,aGram.rules: ", aContext, aGram.rules," || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# return
	
	# Data_Manager.data.currWindHndl =  Window.get_foreground().handle
	data.currWindHndl =  Window.get_foreground().handle

	#region--- (CommentOut temporary for testing)
	#--== detecting new app changed
	# if data.currWindHndl != gl.prevWindHndl_onlyUseToDectectNewApp:
	# 	#--- === New app detected.
  
	# 	gl.prevWindHndl_onlyUseToDectectNewApp = data.currWindHndl

	# 	#region--- (comments)
	# 	#region--- Case: 'dragon dictatation box' is the forgrounde win.
	# 	# #-- A. no exclusiveness, bcz we want normal dragon vovabulary.
	# 	# #-- B. Activate grammars we want to be with the dragon vocabulary, if any.		
	# 	# if win.currentIs_DragonDictBox(data.currWindHndl):
	# 	# 	print "\n", gl.dbgInd["childs"],"20181202211809| Dictation box is forgroud app detected" , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# 	# 	#-- A.
	# 	# 	# gl.ForgrnWind_BforeCalng_DgnDictationBox = data.prevWindHndl # Remember the app before this app.
	# 	# 	gl.State_BforeCalng_DgnDictationBox = DragonModeOnly()
	# 	#endregion
  

	# 	#region--- Case: Dragon dictation box is CLOSED and return back to the app the called it.
	# 	# elif activeWinHnd and gl.ForgrnWind_BforeCalng_DgnDictationBox == activeWinHnd:
	# 	# 	print "\n-20181202211841| return back to window that called Dictation box detected",":->In:",stack()[0][3],"%s:%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# 	# 	#--== return back to  state before calling dragon dictation box
	# 	# 	TamFc.Finished_DragonModeOnly(gl.State_BforeCalng_DgnDictationBox)
	# 	# 	# TamFc.SetThingzToBeExclusive(gl.State_BforeCalng_DgnDictationBox,[],[],"Back to state before calling Dragon Dictation Box . |20181130061428")

	# 	# 	#--
	# 	# 	# gl.ForgrnWind_BforeCalng_DgnDictationBox = None

	# 	# 	if not TamFc.isInUniqModeForCurrApp():
	# 	# 		#-- (new 20181221170033)
	# 	# 		#--== Verify >> if the grammar that have context app matching the freground app is been exclusive, if not, set it to be exclusive.
	# 	# 		TamFc.MakeSureAnGramIsBeenExclusivFor_AppContext(ForegroundAppProcessName, _default_engine.grammars)
	# 	# 		TamFc.ShoInf_thingzBnExclusiv()

	# 	# 	#-- reset variable. It will set when the dictation box will be the forgound window.
	# 	# 	gl.ForgrnWind_BforeCalng_DgnDictationBox = None
	# 	#endregion
	# 	#endregion (comments)
  
	# 	#region--- case: ** Normal (other apps )
	# 	processExclusivForNewApp(aGram,aContext)
	# 	#endregion


	# 	# data.prevWindHndl = data.currWindHndl 				
	#endregion (CommentOut temporary for testing)
		
	#--- Detecte if Window has a grammar associated with (App Content). IF yes: set exclusive it exclusive. 
	# if type(aContext) is AppContext and not isMergedGram(aGram) and not isInUniqModeForCurrApp(): #(no more valide with new Caster)
	if type(aContext) is AppContext and not isInUniqModeForCurrApp():
		#--- TODO: Check why, for example with visual studio code, only 'VSCodeNonCcrRule' and no 'VSCodeCcrRule'??
		# for iR in aGram.rules:
		# 	# if type(iR) is not str:
		# 	iR = iR.__class__.__name__
		# 	if iR	== "Rule": 
		# 		continue
		RuleClassNames = [i.__class__.__name__ for i in aGram.rules if i.__class__.__name__ != 'Rule'] #skeep those with 'Rule(_IntegerRefST_xx)'. TODO: Better way to check?
		print "\n(Exclusiveness) Detected Window has AppContext: ",aContext, ". The following Rule gonna be exclusive:", RuleClassNames, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		print "aGram: ",aGram, 
		print "aGram.rules: ",aGram.rules, 
		# SetRuleToBeExclusive(RuleClassNames)
		
		#--- TODO: ShoInf_thingzBnExclusiv()
  
		
	
	# #--== RainBow

	#--== Normal
	#-- set exclusiveness of grammars for the app.
	# if type(aContext) is AppContext and not isMergedGram(aGram):
		# #-- ex: aGram >> Grammar(VSCodeNonCcrRule(VSCodeNonCcrRule)), Grammar(MergeRule(Merged102MV))
		# # enableR([aGram])

		# # gl.currAppContext_NotMergedGram = aGram
		# data.addNotMergedGram_ofCurrAppContext(aGram)

	data.prevWindHndl = data.currWindHndl 				
