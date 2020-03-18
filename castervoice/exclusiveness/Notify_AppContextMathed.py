from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules
from castervoice.exclusiveness.globalVariable.Data_Manager import data


# def Notify_AppContextMathed(aAppContext_data): #id20200315080523
def Notify_AppContextMathed(executable,title,handle): #id20200315080523
	#--- executable: ex: ['code']

	#--- do it only once (not like 3 times).
	# data.currWindHndl =  Window.get_foreground().handle
	data.currWindHndl =  handle
	if data.currWindHndl == gl.prevWindHndl_onlyUseToDectectNewApp: return	
	gl.prevWindHndl_onlyUseToDectectNewApp = data.currWindHndl

	# print "\n", "20200315135625| executable:", executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# pass

	#region--- set exclusiveness For Rule(S) related to the matched App context
	# print "\n", "20200316114715| gl.allRegisteredRule_HavingAppContext:", gl.allRegisteredRule_HavingAppContext, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	#--- Find out witch rule matched..
	RulesRelatedToCurrWindow_className = []
	for R in gl.allRegisteredRule_HavingAppContext: #R is type of: C:\Users\HP\Documents\Caster\castervoice\exclusiveness\globalVariable\registeredRule_data.py
		Rdetail = R.detail #Rdetail is type of: #of type: C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\rule_details.py
		# print "\n", "20200316111905| Rdetail:", Rdetail, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# print "", "20200316111906| Rdetail.executable:", Rdetail.executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# print "", "20200316111907| executable:", executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		
		#--- TODO: Filter/validate also using: title
		#--- (Rdetail.executable= ,exemple, 'code')
		if Rdetail.executable in executable:
			RulesRelatedToCurrWindow_className.append(R.className)
		# if Rdetail.executable in executable:
		# 	RulesRelatedToCurrWindow_className.add(R.get_rule_class_name())		

	print "\n", "20200315150947| (exclusiveness) App Context matched. So gonna try to set exclusivenss for: ",RulesRelatedToCurrWindow_className,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	Set_Exclusiveness_ForRules(RulesRelatedToCurrWindow_className)

	#endregion set exclusiveness For Rule(S) related to the matched App context
	

	