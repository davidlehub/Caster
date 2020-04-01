#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from dragonfly.grammar.grammar_base import Grammar
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.exclusiveness.Notify_on_begin_fromDragonFly import Notify_on_begin_fromDragonFly

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

class SpeedEngineExclusion(MappingRule):

    mapping = {

        "!!!": "",

    }
    extras = [
        # Dictation("text"),
        # Dictation("mim"),
        # IntegerRefST("n", 1, 1000),
    ]
    defaults = {"n": 1, "mim": ""}

    # def _process_begin(self, executable, title, handle):
    def _process_begin(self):
        # print "\n|- ici process begin.",   "-| {20200329095845| In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno), "}|"
        Notify_on_begin_fromDragonFly()




# ---------------------------------------------------------------------------
def get_rule():
    return SpeedEngineExclusion, RuleDetails(name="Speed Engine exclusion")