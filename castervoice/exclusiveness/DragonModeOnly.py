from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.enableDNS import enableDNS

#region--- (This is how you annotate a function definitio)
# For mappings, we need the types of both keys and values
# x = {'field': 2.0}  # type: Dict[str, float]
# def f(num1, ListOfString, my_float=3.5):
#     # type: (int,List[str], float) -> float
#     """ Your function docstring goes here after the type definition. """
#     return num1 + my_float 

# # This is how you annotate a callable (function) value
# x = f  # type: Callable[[int, float], float]
#endregion (This is how you annotate a function definitio)

def DragonModeOnly(aEnableExclusiveMode=False):
	''' Dragon Naturally speaking vocabulary with Caster. (no any Cster exlsuiveness).
	'''
	# print "\n-20181130202025|",":->In:",stack()[0][3],"%s:%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# why = "Unset all so only Dragon grammar is active. |20181130061141"

	# ExclusivMode.set_enabled(False,"20181217193712| Activating Dragon Mode only.")
	# ExclusivMode.set_enabled(aEnableExclusiveMode)

	RbeenExclusive = list(data.restore_enablebRules_associatedWithApp(data.currWindHndl))

	enableDNS()
	# unsetExclusivenessForGram(data.restore_enablebRules_associatedWithApp(data.currWindHndl))

	return RbeenExclusive


