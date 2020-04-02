#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.lib.util.recognition_history import get_and_register_history

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

# from castervoice.queuing.cls.Queue_cls import Queue_cls

class Queue_cls():
    def __init__(self):
        # self.spokens = {}
        # self.words = None
        self.utterances = []
        self.history = None

    def get_and_register_history(self, lookBack=1000):
        self.history = get_and_register_history(lookBack)

def Add_Queue_forApp(Queue, appData):
    # type: (Queue_cls, AppData_cls) -> None
    pass
    