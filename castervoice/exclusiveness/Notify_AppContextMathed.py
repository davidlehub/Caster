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
	#--- Find out witch rule matched..
	RulesMatchingCurrAppContext_className = set()
	for R in gl.all_RuleHavingAppContext:
		Rdetail = R.get_details()
		#--- TODO: Filter/validate also using: title
		#--- (Rdetail.executable= ,exemple, 'code')
		if Rdetail.executable in executable:
			RulesMatchingCurrAppContext_className.add(R.get_rule_class_name())
			
	print "\n", "20200315150947| (exclusiveness) App Context matched. So gonna try to set exclusivenss for: ",RulesMatchingCurrAppContext_className,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	Set_Exclusiveness_ForRules(RulesMatchingCurrAppContext_className)

	#endregion set exclusiveness For Rule(S) related to the matched App context
	

	