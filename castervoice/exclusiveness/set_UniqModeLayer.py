from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.rules.UniqMode_NonCCR import UniqMode_NonCCR
from castervoice.exclusiveness.UniqModeLayer import UniqModeLayer
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.set_mapping_UniqMode_NonCCR import set_mapping_UniqMode_NonCCR
from castervoice.exclusiveness import Constant as ct

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
	# set_mapping_UniqMode_NonCCR(new_UniqModeLayer_instance.ending_cmd.copy())
	set_mapping_UniqMode_NonCCR(new_UniqModeLayer_instance.ending_cmd)
	#endregion Set "dynamically" the mapping attribute of the class 'UniqMode_NonCCR'
 
	#__ 
 	# new_UniqModeLayer_instance.uniqRule.append('UniqMode_NonCCR') #TODO: no need this one?
 	new_UniqModeLayer_instance.RtoActivate.append(ct.UniqMode_NonCCR_className)
 
	#__ store history of mode layer...
	data.append_UML_ofCurrApp(new_UniqModeLayer_instance)

	#__ Backup/store Rules been exclusive.
	new_UniqModeLayer_instance.RbeenExclusive_stored = list(gl.RbeenExclusive)
	print "\n", "20200325132041| new_UniqModeLayer_instance.RbeenExclusive_stored:", new_UniqModeLayer_instance.RbeenExclusive_stored, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	#__
	#__ TODO: not sure about this calling.
	Set_Exclusiveness_ForRules(new_UniqModeLayer_instance.RtoActivate)