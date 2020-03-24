from castervoice.exclusiveness.rules.UniqMode_NonCCR import UniqMode_NonCCR
from castervoice.exclusiveness.UniqModeLayer import UniqModeLayer
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules

#region--- (This is how you annotate a function definitio)
# def f(num1, my_float=3.5):
#     # type: (int, float) -> float
#     """Your function docstring goes here after the type definition."""
#     return num1 + my_float 
#endregion (This is how you annotate a function definitio)

def set_UniqModeLay(pUniqModeLayer):
	# type: (UniqModeLayer) -> None
	"""  """


	# rule = UniqMode_NonCCR(mapping = pUniqModeLayer["ending_cmd"])
	rule = UniqMode_NonCCR(mapping = pUniqModeLayer.ending_cmd, name='UniqMode NonCCR' + str(data.count_UML_ofApp(data.currWindHndl)))
	# ['Alphabet', 'Numbers', UniqMode_NonCCR(UniqMode NonCCR0)]	
 	pUniqModeLayer.uniqRule.append(rule)
 	pUniqModeLayer.RtoActivate.append(rule)
 
	#__ store history of mode layer...
	data.append_UML_ofCurrApp(pUniqModeLayer)

	#__ Backup/store Rules been exclusive.
	pUniqModeLayer.RbeenExclusive_stored = list(gl.RbeenExclusive)
	# pUniqModeLayer["bkp_MergedCcRule_inf"] = currMergedCcRule_inf.copy()	

	#__
	#__ TODO: not sure about this calling.
	Set_Exclusiveness_ForRules(pUniqModeLayer.RtoActivate)