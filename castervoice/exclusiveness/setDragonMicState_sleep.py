#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.exclusiveness.makeDragonHeard import makeDragonHeard
# from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
import natlink
from castervoice.exclusiveness.cls.DragonVocabulary_cls import enable_dragonVocabulary,disable_dragonVocabulary,dragonVocabulary_is_Disabled, dragonVocabulary_is_Enabled,enable_temporary_dragonVocabulary, disable_temporary_dragonVocabulary, dragonVocabulary_wasTemporary_disable, dragonVocabulary_wasTemporary_enabled


#endregion (Import)

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

def setDragonMicState_sleep():

	mic_state = natlink.getMicState()

	#__ store: ... (TODO)

	#__
	makeDragonHeard(["go", "to", "sleep"])

	#__ When going to sleep, Dragon vocabulary must be enabled: because if not,
	#__ the system is still hearing everything and react as if it is not in sleep mode!
	# DragonVocabulary.temporary_Disabled = False
	# if  DragonVocabulary.enabled
	# if not DragonVocabulary.enabled:
	if dragonVocabulary_is_Disabled():
		print("20200328194934 gonna 'DragonVocabulary.enable()' temporary, bcz it going to sleep")
		# DragonVocabulary.enable()
		# enable_dragonVocabulary()
		enable_temporary_dragonVocabulary()
		# DragonVocabulary.temporary_Disabled = True
		# DragonVocabulary.temporary_Enabled = True

	# print("20200328230205 |'DragonVocabulary.enabled':" , DragonVocabulary.enabled)
