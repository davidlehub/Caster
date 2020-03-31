#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.lib import printer
from castervoice.exclusiveness.cls.DragonVocabulary_cls import enable_dragonVocabulary,disable_dragonVocabulary,dragonVocabulary_is_Disabled, dragonVocabulary_is_Enabled,enable_temporary_dragonVocabulary, disable_temporary_dragonVocabulary, dragonVocabulary_wasTemporary_disable, dragonVocabulary_wasTemporary_enabled


#region--- (david)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl

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

def apply_exclusiveness(grammar):
    # region--- (david)
    if dragonVocabulary_is_Enabled(): return
    # if DragonVocabulary.enabled: return
    # if not DragonVocabulary.enabled: return
    # if not ExclusivMode.enabled: return
    # endregion (david)

    try:
        grammar.set_exclusiveness(1)

        # region--- (david)
        if grammar not in gl.GbeenExclusive:
            gl.GbeenExclusive.append(grammar)
        # endregion (david)

        # print "\n", "dbg20200322172337| grammar set_exclusiveness(1):",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    except Exception as e:
        printer.out(e)
