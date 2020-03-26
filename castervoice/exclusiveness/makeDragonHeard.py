from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.exclusiveness.DragonModeOnly import DragonModeOnly
from dragonfly import Playback 
from castervoice.exclusiveness.Finished_DragonModeOnly import Finished_DragonModeOnly


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

def makeDragonHeard(pWords, pTime=0.0):
	''' pWords: is an [].
	'''
	# print "\n|>--00000000000000| in makeDragonHeard" , " |=> In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	StateBfore_DragonModeOnly = DragonModeOnly()
	try:
		print "\nMake the speech engine heard: ",pWords , " |=> In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		Playback([(pWords, pTime)]).execute()
		# Mimic([(pWords, pTime)]).execute()

	except Exception as e:
		tx = "\n|>--20191030105444| ", e , " |=> In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		raise ValueError(tx)
	# Playback([(["go", "to", "sleep"], 0.0)]).execute()

	Finished_DragonModeOnly(StateBfore_DragonModeOnly)
