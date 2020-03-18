from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.store_AllEnabledRule_ofApp import store_AllEnabledRule_ofApp
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness._cleanupPreviousApp import _cleanupPreviousApp
from castervoice.exclusiveness.BackToPreviousState_OfCurrApp import BackToPreviousState_OfCurrApp
from castervoice.exclusiveness.createAndSetExclusiv_forCurrApp import createAndSetExclusiv_forCurrApp
from castervoice.lib.utilities import get_active_window_path,get_active_window_title, get_window_by_title


# def processExclusivForNewApp(aGram,aContext): #(deprecated for new caster)
# def processExclusivForNewApp(RulesRelatedToCurrWindow_className,CurrWindowData):
def processExclusivForNewApp(CurrWindowData):
	# return
	# print "\n\n\n|~*** 20191202215108g| new app dected|wintitle,data.currWindHndl:", get_active_window_title(), data.currWindHndl, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)				

	#region--- (TODO: uncomment after quick test)
	if not ExclusivMode.enabled: #skeep
		print "\n|~20191207214310| Exclusive mode is off, so not gonna change exclusiveness state.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return				
		
	# gl.currAppContext = aContext #(deprecated for new caster)

	#--- Backup Grammars and rules of previous app, before restoring/cleanup.
	# #--- id2020009170651: do it only >> if the app exist (not closed).
	store_AllEnabledRule_ofApp(data.prevWindHndl)
	# store_EnabledRule_byApp(data.prevWindHndl)

	# #-- 20191205214327
	#--- Cleanup/purge exclusiveness for previous app, IF needed
	_cleanupPreviousApp()  #20191207210733
		
	#--- Back to previous state of the foregound window, if have to.
	#--- ex.: We was with a window A, then we switch to window B. Then switch back to A, witch is the current foregound one.
 	#--- The current window A could have his exclusiveness 'state' previously saved (at id2020009170651), so we retore that saved 'state'.
	#--- An other scenario: where the current foreground window is a new one, that just open/launched (so there is no state saved), ... 
	# BackToPreviousState_OfCurrApp(aContext) #(deprecated for new caster)
	BackToPreviousState_OfCurrApp()
	

	# #region--- Case: 'dragon dictatation box' is the forgrounde window.
	# #-- A. no exclusiveness, bcz we want normal dragon vovabulary.
	# #-- B. Activate grammars we want to be with the dragon vocabulary, if any.		
	# if win.currentIs_DragonDictBox(data.currWindHndl):
	# 	print "\n", gl.dbgInd["childs"],"20181202211809| Dictation box is forgroud app detected" , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# 	#-- A.
	# 	# gl.ForgrnWind_BforeCalng_DgnDictationBox = data.prevWindHndl # Remember the app before this app.
	# 	gl.State_BforeCalng_DgnDictationBox = DragonModeOnly(True)
	# 	# print "\n", gl.dbgInd["childs"],"20181202211810| gl.State_BforeCalng_DgnDictationBox: ",gl.State_BforeCalng_DgnDictationBox , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# #endregion
	#endregion (TODO: uncomment after quick test)

	# #--== ** Ceate and set exclusiveness for current app.
	# createAndSetExclusiv_forCurrApp(aGram, aContext) #(deprecated for new caster)
	# createAndSetExclusiv_forCurrApp(RulesRelatedToCurrWindow_className,CurrWindowData)
	createAndSetExclusiv_forCurrApp(CurrWindowData)

	# else:
	# 	# print "\n\t|~ici 20191208115702| Gonna create and ActivateExclusivenessForCurrApp()",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	createAndSetExclusiv_forCurrApp(aGram, aContext)

	#---  (show info)
	# ShoInf_thingzBnExclusiv()
