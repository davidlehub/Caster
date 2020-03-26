from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.lib.merge.mergerule import MergeRule

#region--- (This is how you annotate a function definitio)
# def f(num1, ListOfString, my_float=3.5):
#     # type: (int,List[str], float) -> float
#     """Your function docstring goes here after the type definition."""
#     return num1 + my_float 
#endregion (This is how you annotate a function definitio)

def set_mapping_UniqMode_NonCCR(mapping={}):
	# type: (Dict[str, ...]) -> None
	""" """
	
	if not gl.UniqMode_NonCCR_ruleClass:
		#__ get our 'UniqMode_NonCCR'
		for RegisteredR in gl.allRegisteredRule:
			if RegisteredR.className == 'UniqMode_NonCCR':
				gl.UniqMode_NonCCR_ruleClass = RegisteredR.rule_class # type: MergeRule
				break
		if not gl.UniqMode_NonCCR_ruleClass:
			print "\n", "!!! Can not get the rule 'UniqMode_NonCCR'. | gl.UniqMode_NonCCR_ruleClass:", gl.UniqMode_NonCCR_ruleClass, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
			return

	#__ Set "dynamically" the mapping
	gl.UniqMode_NonCCR_ruleClass.mapping = mapping
	# print "\n", "ici20200324113228| gl.UniqMode_NonCCR_ruleClass.mapping:", gl.UniqMode_NonCCR_ruleClass.mapping, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)