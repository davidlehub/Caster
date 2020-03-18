from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from dragonfly import Window
# from dragonfly import AppContext, Window
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.processExclusivForNewApp import processExclusivForNewApp
import os, win32gui
from castervoice.lib.utilities import get_active_window_path
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules
from castervoice.exclusiveness.CurrWindow_data import CurrWindow_data


# def Notify_process_begin_GramBase(aGram, aExecutable, aTitle, aWindHndl):
def Notify_on_begin_fromDragonFly():
	# print "\n|~ici 20191215145726| in def Notify_process_begin_GramBase | aGram, aExecutable, aTitle, aWindHndl:", aGram, aExecutable, aTitle, aWindHndl, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	if not ExclusivMode.enabled: #skeep
		print "\n|~20200109164509| Exclusive mode is off, so not gonna change exclusiveness state.",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return	

	data.currWindHndl =  Window.get_foreground().handle
	# data.currWindHndl =  aWindHndl

	#--== detect new app chenged
	# if not data.currWindHndl == data.prevWindHndl:
	# if not data.currWindHndl == gl.prevWindHndl_onlyUseToDectectNewApp:
	# print "\n|~ici 20191215152147| data.currWindHndl,gl.prevWindHndl_onlyUseToDectectNewApp:", data.currWindHndl,gl.prevWindHndl_onlyUseToDectectNewApp, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	if data.currWindHndl != gl.prevWindHndl_onlyUseToDectectNewApp: #active window has changed
		gl.prevWindHndl_onlyUseToDectectNewApp = data.currWindHndl

		#region--- (? still needed?)
		#--== info user
		activeWinPath = get_active_window_path()
		if not activeWinPath:
			print "\n|>1- Forground app changed. @activeWinPath= '",activeWinPath,"'<|20181110212118| In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s|%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			return False	
		#endregion (? still needed?)


		ForegroundAppProcessName = (os.path.splitext(os.path.basename(activeWinPath))[0]).lower()
		CurrWindowData = CurrWindow_data(ForegroundAppProcessName)
		print "\n|>--20181110212119| ** Forground app changed, process name: ", ForegroundAppProcessName , " |=> In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)



		#region--- set exclusiveness For Rule(S) related to the matched App context
		# print "\n", "20200316114715| gl.allRegisteredRule_HavingAppContext:", gl.allRegisteredRule_HavingAppContext, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

		#--- Find out witch rule matched..
		RulesMatchingCurrAppContext_className = set()
		for R in gl.allRegisteredRule_HavingAppContext: #R is type of: C:\Users\HP\Documents\Caster\castervoice\exclusiveness\globalVariable\registeredRule_data.py
			Rdetail = R.detail #Rdetail is type of: #of type: C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\rule_details.py
			# print "\n", "20200316111905| Rdetail:", Rdetail, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			# print "", "20200316111906| Rdetail.executable:", Rdetail.executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			# print "", "20200316111907| executable:", executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			
			#--- TODO: Filter/validate also using: title
			#--- (Rdetail.executable= ,exemple, 'code')
			# if Rdetail.executable in executable:
			# if Rdetail.executable in executable:
			# 	RulesMatchingCurrAppContext_className.add(R.get_rule_class_name())		
			if Rdetail.executable == CurrWindowData.ForegroundAppProcessName:
				RulesMatchingCurrAppContext_className.add(R.className)

		# if len(RulesMatchingCurrAppContext_className) > 0:
		# 	print "\n", "20200315150947| (exclusiveness) App Context matched. So gonna try to set exclusivenss for: ",RulesMatchingCurrAppContext_className,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	Set_Exclusiveness_ForRules(RulesMatchingCurrAppContext_className)
		

		if len(RulesMatchingCurrAppContext_className) > 0:
			# processExclusivForNewApp(None,None) #
			processExclusivForNewApp(RulesMatchingCurrAppContext_className,CurrWindowData)
			# try:
			# except:
			# 	print "\n|~!!!20191216153327| error:", sys.exc_info()[0], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			# 	pass
			# 	# data.prevWindHndl = data.currWindHndl

		#endregion set exclusiveness For Rule(S) related to the matched App context

		data.prevWindHndl = data.currWindHndl



		
	# print "\n|~ici 20191202215108f| in _process_begin:",aExecutable, aTitle, aWindHndl , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)				
	# # if handle == _PrevAppHwnd:
	# if aWindHndl == data.prevWindHndl:
	# 	return

	# #--*** Foreground window switching detected.
	# print "\n|~ici 20191208120044| new app dected:",aExecutable, aTitle, aWindHndl , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)				
	# #-- update
	# data.currWindHndl = aWindHndl
	# # print "\n|~ici 20191208120052| new app dected:",self,executable, title, handle , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)				
	# # TamFc.Notify__process_begin_GramBase(self,executable, title, handle)
	# # TamFc.Notify__process_begin_GramBase(executable, title, handle)
	
	# #region-- Cleanup
	# if data.prevWindHndl:
		
	# 	#---- delete data.appExclusiveness if thre is no any UML layer... ANd when detec app (the handle) is no more exist
	# 	if not data.count_UML_ofApp(data.prevWindHndl):
	# 		del data.appExclusiveness[data.prevWindHndl]
			
	# 	#---- Also delete data.appExclusiveness if that app doesn't exist anymore.
	# 	try:
	# 		x = win32gui.GetClassName(data.prevWindHndl)
	# 	except:
	# 		#-- (app doesn't exist anymore)
	# 		#---- delete data.appExclusiveness
	# 		# print "\t|~ici 20191206203011| previous app is closed.", " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)					
	# 		del data.appExclusiveness[data.prevWindHndl]

	# 	#---- flush/purge exclusiveness
	# 	# unSetAll_GramzBeenExclusi([], "20191206190343")	
	# 	unsetExclusivenessForGram(data.appExclusiveness[data.prevWindHndl].getAllGram())
	# 	# _NEXUS.merger.wipe() #20191128211839
	# #endregion
		
	# #--- ..
	# ActivateExclusivenessForCurrApp()

	# # #--== Make sure the list of grammars we want to be alway exlusive, are exclusive.
	# # if not isInUniqModeForCurrApp():
	# # 	# TamFc.SetThingzToBeExclusive(gl.gramName_AlwayExclusi,[], [],"DetectChangesIn_DfaultEngineGramz. Making sure grammars we want alway exclusiv are in exclusive. |20191129105607")
	# # 	enableR(data.getGramObjFrmGramStr(gl.gramName_AlwayExclusi))		

		
	# #--- update
	# data.prevWindHndl = aWindHndl

	# # return
	# # print "\n|~ici 20191205183747c| in def Notify__process_begin_GramBase| aExecutable, aTitle, aWindHndl:", aExecutable, aTitle, aWindHndl , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)		

	# # # gl.isFrgddWind_chnged = True
	# # gl.CurrExecutable = aExecutable
	# # gl.CurrTitle = aTitle
	# # data.currWindHndl = aWindHndl


 
	# # #--== RainBow

	# # #--== Normal
	# # #-- set exclusiveness for the app
	# # # setExclusivenessForApp
	# # # if aContext is not None or aContext == :
	# # # if type(aContext) is AppContext :
		
 	# # # 	# SetThingzToBeExclusive([aGram],[],["AppContext"], "fereground app changed, but the grammar is not yet been exclusive. |20181113133851")
	# # # 	aGram.set_exclusiveness(1)

	# # # 	#-- Add the app to memory
	# # # 	# data.memoriseAppExclusiveness(aGram,aContext)
	# # # 	data.memoriseAppExclusiveness(aGram,aContext)
