from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.UniqModeLayer import UniqModeLayer
from castervoice.exclusiveness.set_mapping_UniqMode_NonCCR import set_mapping_UniqMode_NonCCR
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable import ExclusivenessSetting
from castervoice.exclusiveness import Constant as ct

#region--- (This is how you annotate a function definitio)
# def f(num1, ListOfString, my_float=3.5):
#     # type: (int,List[str], float) -> float
#     """Your function docstring goes here after the type definition."""
#     return num1 + my_float 
#endregion (This is how you annotate a function definitio)

# def do_backOneLevelOfUML():
def do_backOneLevelOfUML(CurrUniqModeLayer):
	from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules
	from castervoice.exclusiveness.disableR import disableR
	
	Why = "back one level of uniq mode layer"
	#region--- (comments)
	#--== Delete/remove UniqMode grammar that was generated.
	#region replaced by vers 20191128204732
	# for iG in CurrUniqModeLayer['thingsToBeUniq']:
	# 	print "\n|~20191125102733| iG:", iG, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	if not isMergedGram(iG):
	# 		print "\t|~hasattr(iG, unload):", hasattr(iG, "unload"), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		if hasattr(iG, "unload"):
	# 			print "\n|~20191125102734| gonna unload grammar| iG:", iG, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 			iG.unload()
	# 			# try:
	# 			# 	iG.unload()
	# 			# except:
	# 			# 	pass
	# 	# Grammar.unload()
	#endregion


	# print "\n|~ before pop. 20191125102734| gl.UniqModeLayer_Hist:", gl.UniqModeLayer_Hist, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# y = gl.UniqModeLayer_Hist[len(gl.UniqModeLayer_Hist) - 1]
	# x = gl.UniqModeLayer_Hist.pop()

	# # y = gl.UniqModeLayer_Hist.pop(len(gl.UniqModeLayer_Hist) - 1)
	# print "\t|~after pop 20191125102734| gl.UniqModeLayer_Hist:", gl.UniqModeLayer_Hist, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# print "\t|~x:", x
	# print "\t|~y:", y
	# print "\t|~| y:", y

	#==== For CCR merged. (Set exclusiveness back previous one.)
	# rePutCCR(CurrUniqModeLayer["bkp_CcrMergedID_x_Type"])
	# mergeCcRules(CurrUniqModeLayer["bkp_MergedCcRule_inf"]) #replave by vers 20191128204732

	#--{20191128212653 vers 20191128204732
	#-- remove/delete all _NEXUS.merger_grammars
	# _NEXUS.merger.wipe() #20191128211839
	#endregion (comments)
 
	#____ restore exclusive state
	restored_RbeenExclusive = list(CurrUniqModeLayer.RbeenExclusive_stored)
	# _NEXUS._grammar_manager._managed_rules = CurrUniqModeLayer["bkp_AllEnabledRule"].copy()
	#__ 
	Set_Exclusiveness_ForRules(restored_RbeenExclusive)

	#____ Cleanup/reset/reinitialise 
	# set_mapping_UniqMode_NonCCR({"!!!": None}) # some thing that will never speeched by user.
	set_mapping_UniqMode_NonCCR({}) #
	disableR([ct.UniqMode_NonCCR_className]) #have to, if not the spec is still available.
	CurrUniqModeLayer = None
 
	#--{20191128224442 vers 20191128204732
	#--== Delete/remove UniqMode grammar that was generated.
	# CurrUniqModeLayer["uniqGram"].pop




	#-- (don't show info here, bcz will show by the caller of this function)
	# print "\n|~20191121231633| Done Processing back, of 1 level of UniqMode| len(gl.UniqModeLayer_Hist):", len(gl.UniqModeLayer_Hist), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# ShoInf_thingzBnExclusiv()

