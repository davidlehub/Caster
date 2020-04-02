#__ TODO: delete bcz don't know how to use event-hook system other place then 'grammar_manager'

#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

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

class queuingSpoken_hook(BaseHook):

	def __init__(self):
		super(queuingSpoken_hook, self).__init__(EventType.SPOKEN_RECOGNIZED)

	def get_pronunciation(self):
		return "printer"

	def run(self, event):
		# state = "active" if event.active else "inactive"
		# printer.out("The rule {} was set to {}.".format(event.rule_class_name, state))

		#region--- (david)
		""" The reason of adding this: bcz, for example, when user say 'enable/disble python',
  			we want the 'gl.RbeenActive' to be uptodate.
		"""
		# Update_RbeenExclusive(event.rule_class_name, event.active)
		# detect_SpeechEngineVocabulary_activation(event.rule_class_name, event.active)
		#endregion (david)


def get_hook():
	return queuingSpoken_hook
