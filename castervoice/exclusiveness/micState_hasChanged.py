#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
import natlink

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

previous_micState = "" # Type: str

def micState_hasChanged():
    global previous_micState
    curr_micState = natlink.getMicState()
    if curr_micState == previous_micState:
        previous_micState = curr_micState
        return  True
    else:
        return  False