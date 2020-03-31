#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
# from castervoice.exclusiveness.cls.DragonVocabulary_cls import DragonVocabulary
from castervoice.exclusiveness.cls.DragonVocabulary_cls import enable_dragonVocabulary,disable_dragonVocabulary,dragonVocabulary_is_Disabled, dragonVocabulary_is_Enabled,enable_temporary_dragonVocabulary, disable_temporary_dragonVocabulary, dragonVocabulary_wasTemporary_disable, dragonVocabulary_wasTemporary_enabled,indicate_DragonVocabulary_is_Disabled

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

def detect_SpeechEngineVocabulary_activation(class_name, enabled):
	from castervoice.exclusiveness.rules.SpeedEngineExclusion import SpeedEngineExclusion

	# print "\n|-- SpeedEngineExclusion.__name__:", SpeedEngineExclusion.__name__,  "--| 20200330084738 |{ In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno), "}|"

	#__ make sure to enable_dragonVocabulary, when 'SpeedEngineExclusion' rule is disable.
	if class_name == SpeedEngineExclusion.__name__ and not enabled:
		# print "\n|-- Ok gonna enable_dragonVocabulary:",   "--| 20200330090213 |{ In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno), "}|"
		enable_dragonVocabulary()

	# __ make sure to disable_dragonVocabulary, when 'SpeedEngineExclusion' rule is enable.
	elif class_name == SpeedEngineExclusion.__name__ and enabled:
		disable_dragonVocabulary()

