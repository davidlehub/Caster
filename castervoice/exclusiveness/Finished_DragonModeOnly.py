from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
# from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.Set_Exclusiveness_ForRules import Set_Exclusiveness_ForRules
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.exclusiveness.cls.DragonVocabulary_cls import DragonVocabulary


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

def Finished_DragonModeOnly(pStateToReturnBack):
	# type: (List[str]) -> None
	"""  """

	# print "\n|~ici 20191207220001| Finished_DragonModeOnly, switch back exlcueness with rules  :", pStateToReturnBack, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	Set_Exclusiveness_ForRules(pStateToReturnBack)

	DragonVocabulary.enabled
	# ExclusivMode.set_enabled(True)


	# # print "\n|~ici 20191207220001| Finished_DragonModeOnly, switch back exlcueness with rules  :", pStateToReturnBack, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# ExclusivMode.set_enabled(True)
	# # ExclusivMode.set_enabled(True,"20181217224548| Finished dragon mode only.")
	# # _set_GramToBeExclusiInDefaultEngi(pStateToReturnBack,[],"Finished_DragonModeOnly. |20181130061428")
	# # SetThingzToBeExclusive(pStateToReturnBack,[],[],"Finished_DragonModeOnly. |20181130061428")
	# # enableR(pStateToReturnBack) #(pStateToReturnBack,[],[],"Finished_DragonModeOnly. |20181130061428")
	# Set_Exclusiveness_ForRules(pStateToReturnBack)