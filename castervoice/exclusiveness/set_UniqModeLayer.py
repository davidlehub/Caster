from castervoice.exclusiveness.rules.UniqMode_NonCCR import UniqMode_NonCCR
from castervoice.exclusiveness.UniqModeLayer import UniqModeLayer
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from inspect import getframeinfo, stack, getframeinfo, currentframe

#region--- (This is how you annotate a function definitio)
# def f(num1, my_float=3.5):
#     # type: (int, float) -> float
#     """Your function docstring goes here after the type definition."""
#     return num1 + my_float 
#endregion (This is how you annotate a function definitio)

def set_UniqModeLay(new_UniqModeLayer_instance):
	# type: (new_UniqModeLayer_instance) -> None
	"""  """
	from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules

	#region--- Set "dynamically" the mapping attribute of the class 'UniqMode_NonCCR'
	#__ get our 'UniqMode_NonCCR'
	UniqMode_NonCCR_ruleClass =None
	for RegisteredR in gl.allRegisteredRule:
		if RegisteredR.className == 'UniqMode_NonCCR':
			UniqMode_NonCCR_ruleClass = RegisteredR.rule_class
			break
	if not UniqMode_NonCCR_ruleClass:
		print "\n", "!!! Can not get the rule 'UniqMode_NonCCR'. | UniqMode_NonCCR_ruleClass:", UniqMode_NonCCR_ruleClass, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
		return

	#__ Set "dynamically" the mapping
	UniqMode_NonCCR_ruleClass.mapping = new_UniqModeLayer_instance.ending_cmd.copy()
	print "\n", "ici20200324113228| UniqMode_NonCCR_ruleClass.mapping:", UniqMode_NonCCR_ruleClass.mapping, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# UniqMode_NonCCR_ruleClass.mapping = {"(done | finished)": R(Text("coucou 20200324113924"), rdescript="test test")} 

	#endregion Set "dynamically" the mapping attribute of the class 'UniqMode_NonCCR'
	

	# rule = UniqMode_NonCCR(mapping = new_UniqModeLayer_instance["ending_cmd"])
	# rule = UniqMode_NonCCR(mapping = new_UniqModeLayer_instance.ending_cmd, name='UniqMode_NonCCR' + str(data.count_UML_ofApp(data.currWindHndl)))
	# ['Alphabet', 'Numbers', UniqMode_NonCCR(UniqMode NonCCR0)]	
 
	#__ 
 	new_UniqModeLayer_instance.uniqRule.append('UniqMode_NonCCR') #TODO: no need this one?
 	new_UniqModeLayer_instance.RtoActivate.append('UniqMode_NonCCR')
 
	#__ store history of mode layer...
	data.append_UML_ofCurrApp(new_UniqModeLayer_instance)

	#__ Backup/store Rules been exclusive.
	new_UniqModeLayer_instance.RbeenExclusive_stored = list(gl.RbeenExclusive)
	# new_UniqModeLayer_instance["bkp_MergedCcRule_inf"] = currMergedCcRule_inf.copy()	

	#__
	#__ TODO: not sure about this calling.
	# Set_Exclusiveness_ForRules(['UniqMode_NonCCR'])
	Set_Exclusiveness_ForRules(new_UniqModeLayer_instance.RtoActivate)