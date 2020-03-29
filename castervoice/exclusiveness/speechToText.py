#__ TODO: Delete file
# from inspect import getframeinfo, stack, getframeinfo, currentframe
# from castervoice.exclusiveness.exclusiveness_OnOff import exclusiveness_OnOff
# from castervoice.exclusiveness.set_UniqModeLayer import set_UniqModeLay
# from castervoice.exclusiveness.UniqModeLayer import UniqModeLayer
# from castervoice.exclusiveness.EndCurrUML_BckToPrviousState import EndCurrUML_BckToPrviousState
# from castervoice.lib.merge.state.short import R
# from dragonfly import Function
# from castervoice.lib.actions import Text
#
# #region--- (This is how you annotate a function definitio)
# # def f(num1, ListOfString, my_float=3.5):
# #     # type: (int,List[str], float) -> float
# #     """Your function docstring goes here after the type definition."""
# #     return num1 + my_float
# #endregion (This is how you annotate a function definitio)
#
# # def speechToText(ending_cmd="",CompanionRules_clasName=[]):
# def speechToText(text="", ending_cmd="",CompanionRules_clasName=[]):
# 	# type: (str, List[str]) -> float
# 	""" """
# 	print "\n", "20200324185910|  ending_cmd,CompanionRules_clasName:",  ending_cmd,CompanionRules_clasName, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
# 	return
#
# 	exclusiveness_OnOff(False)
#
#
#
# 	#__
# 	ThisUniqModeLayer = UniqModeLayer()
# 	ThisUniqModeLayer.name = ""
# 	ThisUniqModeLayer.RtoActivate.extend(CompanionRules_clasName)
# 	# ThisUniqModeLayer.RtoActivate.extend(['Alphabet','Numbers'])
# 	ThisUniqModeLayer.ending_cmd = {ending_cmd: R(Function(EndCurrUML_BckToPrviousState), rdescript="")}
# 	# ThisUniqModeLayer.ending_cmd = {"(done | finished)": R(Text("coucou 20200324113924"), rdescript="")}
#
# 	set_UniqModeLay(ThisUniqModeLayer)
#
#  	#__
# 	Text(text).execute()