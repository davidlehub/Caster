from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data, Exclusiveness,GramAndRules
from castervoice.exclusiveness.isInUniqModeForCurrApp import isInUniqModeForCurrApp
from castervoice.exclusiveness.windowManager import win
from castervoice.exclusiveness.DragonModeOnly import DragonModeOnly
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.disableR import disableR
from castervoice.lib.control import _NEXUS
from castervoice.exclusiveness.enableR import enableR
from castervoice.exclusiveness.setGramToBeExclusive import setGramToBeExclusive
from dragonfly.engines import (_default_engine)


def createAndSetExclusiv_forCurrApp(aAppGram, aContext):
	# type: (list(Grammar)) -> ?
	#--== A: Set, and memorize, exclusiness of grammar related to current app.
	#--== B: Make sure the list of grammars we want to be alway exlusive, are exclusive.

	if not data.currWindHndl: #it hapen that this vallue = 0. (eg. when an app is closed).
		return

	#--- Only if current isn't in Uniq Mode
	if isInUniqModeForCurrApp():
		print "|~ici 20191211131841| Return (exit) of 'def createAndSetExclusiv_forCurrApp', bcz: in if isInUniqModeForCurrApp", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return

	#region--- instantiate class 'Exclusiveness()' (if not already exist). 
	""" -- EACH APP is associate with an instance of the class 'Exclusiveness()'.
		-- That class 'Exclusiveness()' is used to: remember witch grammar and rules are exclusive.
 	 """
 	#-- That class is use to remember  
	if not data.appExclusiveness.has_key(data.currWindHndl):
		data.appExclusiveness[data.currWindHndl] = Exclusiveness()		
	if not data.appGramAndRules.has_key(data.currWindHndl):
		data.appGramAndRules[data.currWindHndl] = GramAndRules()
	#endregion

	#region--- Case: 'dragon dictatation box' is the forgrounde window.
	#-- A. no exclusiveness, bcz we want normal dragon vovabulary.
	#-- B. Activate grammars we want to be with the dragon vocabulary, if any.		
	if win.currentIs_DragonDictBox(data.currWindHndl):

		#-- A.
		# gl.ForgrnWind_BforeCalng_DgnDictationBox = data.prevWindHndl # Remember the app before this app.
		gl.State_BforeCalng_DgnDictationBox = DragonModeOnly(True)
		# print "\n", gl.dbgInd["childs"],"20181202211810| gl.State_BforeCalng_DgnDictationBox: ",gl.State_BforeCalng_DgnDictationBox , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	#endregion
	
	#region--- Case: other apps is the forgrounde window.
	else:
		SetRuleToBeExclusive(aRuleClassNames)
    	#--- aRuleClassNames = list
  
		#region--- Begin Exclusive Mode
		#--- list of rule we want to be exclusive
		RtoBeExclusive = aRuleClassNames + gl.RcasterAlwayNeed
  
		# print "\n", "20200112220615| New caster: exclusiveness for| RtoBeExclusive:", RtoBeExclusive, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		#--- Diable all Rules, except those we want to be exclusive.
		AllRules = all_MappingRule_className +  all_MergeRules_className
		disableR(AllRules, RtoBeExclusive)
		# disableR(_NEXUS._grammar_manager._config.get_enabled_rcns_ordered(),RtoBeExclusive)
	
		#--- Enable rule we want to be exclusive.
		enableR(RtoBeExclusive)
		#--- Remember
		data.store_enablebRules_associatedWithApp(data.currWindHndl)

		#--- Set Exclusiveness of all grammar in the system (_default_engine). (_default_engine.grammars)
		setGramToBeExclusive(_default_engine.grammars)		
   	
		#endregion Begin Exclusive Mode

		
		#region--- (od Caster
		# #region--- Make grammars and rules to be exclusive. 
		# #--- Make sure the list of grammars we want to be alway exlusive, are exclusive.
		# setExclusivForGram_andMemorise(data.getGramObjFrmGramStr(gl.gramName_AlwayExclusi))		

		# #--- Set, and memorize, exclusiness of grammar related to current app. if ...
		# if type(aContext) is AppContext and not isMergedGram(aAppGram):
		# 	# print "\n|~ici 20191210224809| gonna  setExclusivForGram_andMemorise" , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	# print "\n\t|~ici 20191210224809| [aAppGram]:", [aAppGram], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	setExclusivForGram_andMemorise([aAppGram])

		# #--- id20191216184219: for 'CCR non' grammar (autogenerated by caster)
		# #region--- (TD: To upgrade for new Caster)
		# print "\n", "TD 20200111182549| To upgrade for new Caster:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)	
		# # enableR(_NEXUS.merger._grammars) #20191210171116
		# # data.memorise_CcrNonGram()
		# #endregion 

		# #--- 
		# data.memorise_MergedRule_zip()		
		# #endregion
		#endregion (od Caster
  
	#endregion
