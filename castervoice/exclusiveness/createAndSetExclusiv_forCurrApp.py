from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data, Exclusiveness,GramAndRules
from castervoice.exclusiveness.isInUniqModeForCurrApp import isInUniqModeForCurrApp
from castervoice.exclusiveness.windowManager import win
from castervoice.exclusiveness.DragonModeOnly import DragonModeOnly
from castervoice.exclusiveness.globalVariable import GlobalV as gl
# from castervoice.lib.control import _NEXUS
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules

# from dragonfly.engines import (_default_engine)

# from castervoice.exclusiveness.disableR import disableR
# from castervoice.exclusiveness.enableR import enableR
# from castervoice.exclusiveness.setGramToBeExclusive import setGramToBeExclusive


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
		#--- TODO
		pass 
		# Set_Exclusiveness_ForRules(Rule)

		
