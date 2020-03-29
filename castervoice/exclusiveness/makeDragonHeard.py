from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
# from castervoice.exclusiveness.DragonModeOnly import DragonModeOnly
from dragonfly import Playback 
from castervoice.exclusiveness.Finished_DragonModeOnly import Finished_DragonModeOnly
# from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules
# from castervoice.exclusiveness.exclusiveness_OnOff import exclusiveness_OnOff
from castervoice.exclusiveness.cls.DragonVocabulary_cls import enable_dragonVocabulary,disable_dragonVocabulary,dragonVocabulary_is_Disabled, dragonVocabulary_is_Enabled,enable_temporary_dragonVocabulary, disable_temporary_dragonVocabulary, dragonVocabulary_wasTemporary_disable, dragonVocabulary_wasTemporary_enabled,indicate_DragonVocabulary_is_Disabled


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

	#__ if excllusive is ON(enabled), TEMPORARY turn it Off: to make DNS vocabulary available.
	# Exclusive_wasTemporaryTurnOff = False
	# if  ExclusivMode.enabled:
	# if  DragonVocabulary.enabled:
	# if  not DragonVocabulary.enabled:
	if dragonVocabulary_is_Disabled():
		# StateBfore_DragonModeOnly = DragonModeOnly()
		# StateBfore_DragonModeOnly = list(data.restore_enablebRules_associatedWithApp(data.currWindHndl))

		print "\n", "20200328224721| Gonna 'DragonVocabulary.enable()' temporary "

		enable_temporary_dragonVocabulary()
		# enable_dragonVocabulary()
		# DragonVocabulary.enable()
		# DragonVocabulary.disable()
		# exclusiveness_OnOff(False)

		# DragonVocabulary.temporary_Enabled = True
		# DragonVocabulary.temporary_Disabled = True
		# Exclusive_wasTemporaryTurnOff = True

	#__ calling DNS command. (using 'Playback()')
	try:
		print "\nMake the speech engine heard: ",pWords , " |=> In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		Playback([(pWords, pTime)]).execute()
		# Mimic([(pWords, pTime)]).execute()
	except Exception as e:
		tx = "\n|>--20191030105444| ", e , " |=> In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		raise ValueError(tx)


	# if  StateBfore_DragonModeOnly: 

	#__ Turn back exclusive to ON, If it was Temporary turn Off.
	# if  Exclusive_wasTemporaryTurnOff:
	# if  DragonVocabulary.temporary_Disabled:
	# if  DragonVocabulary.temporary_Enabled:
	if dragonVocabulary_wasTemporary_enabled():

		# Finished_DragonModeOnly(StateBfore_DragonModeOnly)

		# ExclusivMode.set_enabled(True)
		# Set_Exclusiveness_ForRules(StateBfore_DragonModeOnly)		
		print "\n", "2020032824939| Gonna 'DragonVocabulary.disable()' bcz it was 'DragonVocabulary.temporary_Enabled' "

		disable_dragonVocabulary()
		# DragonVocabulary.disable()
		# DragonVocabulary.enable()
		# exclusiveness_OnOff(True)


	# if  StateBfore_DragonModeOnly: 
	# 	# Finished_DragonModeOnly(StateBfore_DragonModeOnly)

	# 	# ExclusivMode.set_enabled(True)
	# 	Set_Exclusiveness_ForRules(StateBfore_DragonModeOnly)		
	# 	exclusiveness_OnOff(True)		

		# print "\n", "20200326131611| ici:",StateBfore_DragonModeOnly,  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
