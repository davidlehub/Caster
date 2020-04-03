#region--- (Import)
import time
from inspect import getframeinfo, stack, getframeinfo, currentframe

from dragonfly.windows.base_window import BaseWindow
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.lib.merge.mergerule import MergeRule
from dragonfly import MappingRule, FocusWindow
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
from dragonfly import (Grammar, Playback, Key, Dictation, Function, Text, ActionBase)
from castervoice.lib.const import CCRType
from castervoice.lib.merge.state.actions import AsynchronousAction, ContextSeeker
from castervoice.lib.merge.state.actions2 import NullAction
from castervoice.lib.merge.state.short import R, S, L
from dragonfly.actions.action_mimic import Mimic

from castervoice.lib.utilities import window_exists
from castervoice.queuing.cls.Queue_cls import Queue_cls
from castervoice.queuing.globalVariables.queues import queues
from castervoice.queuing.on_recognition_fromDragonfly import on_recognition_fromDragonfly, on_recognition_DataShare
from castervoice.lib.util.recognition_history import get_and_register_history
from dragonfly import Window

#endregion (Import)

K = Key
F = Function

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

''' template:
   "vis": R( #
       # F(insertComment_simple)
       K(N_Mode)
       + K("v")
       , rdescript="|>-00- Vim start select. |" + stack()[0][3] + "|%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
       ) #end 'R('
       ,
'''
#__ ____________________________________________

Queue = None  # type:Queue_cls
def prepareStorage_forQueuingCommandsHistory(params=None):
    # type: () -> Queue_cls
    
    # print "\n|-- in 'prepareStorage_forQueuingCommandsHistory()'|params:",params,   "--| 20200402105707 |"

    global Queue
    Queue = Queue_cls()
    Queue.get_and_register_history()

    # return Queue



def RepeatlyCheck_ifWindowExist(p):

    windowname = p[0]
    executable = p[1]

    print "\n|-- Queuing is activated: checking, at every second, if The window named '%s' of the app '%s' is appeared, then will execute the commands in the queue." % (windowname, executable) , "--| 20200402081642 |"


    if window_exists(windowname=windowname, executable=executable):
        #__ focus on that window

        FocusWindow(title=windowname, executable=executable)
        time.sleep(0.3) # give a chance to window appear.

        return   True #this make the Asynch. loop to stop. then execute commands been blocked.

    else:
        return  False

def  on_QueuingConditionMet():
    """
    :rtype: None
    """
    print "\n|-- in 'on_QueuingConditionMet()'| Queue.history:", Queue.history,  "--| 20200402021207 |"


# class queuingTrigger(MergeRule):
class queuingTrigger(MappingRule):
    mapping = {
        # "<modifier>": R(F(modifier_handle, extra={"modifier"}),
        #                 rspec="modifier_rspec") + ContextSeeker(forward=[L(  # works
        #     # S(["no time"], makeDragonHeard_contextSeek, parameters=[["big"], 0.0]),
        #     # - vid20191229154126
        #     # S(["!!!"], makeDragonHeard_contextSeek, parameters=[[gl.modofierPressedDown[0]], 0.0]), #error: list index out of range
        #     S(["!!!"], makeDragonHeard_existingModifier),
        #     S(["cancel"], TamFc.releaseModifierKey),
        #     # S(["letter_rspec"], sendKey_Letter, use_rspec=True), #the parameters (a) is = 'letter_rspec'
        #     # S(["letter_rspec"], sendKey_Letter, parameters=["%(letter)s"]), #the parameters (a) is = ["%(letter)s"]
        #     S(["modifier_rspec"], NullAction(), consume=False),  # ok
        #     # --- (i dont puted 'Delete_rspec', bcz is dangerous...)
        #     # S(["letter_rspec","enterKey_rspec","backspace_rspec","escape_rspec","direction_rspec_notCCR"
        #     # 	,"leftCLick_rspec_notCCR","middleCLick_rspec_notCCR","rightCLick_rspec_notCCR","wheelScroll_rspec_notCCR"
        #     # 	, "pontuation_rspec"
        #     # S(["letter_rspec","pontuation_rspec"
        #     S(["allKeyboard_ccrSpec", "allFunctionKey_NonCcrSpec"
        #        ], TamFc.releaseModifierKey, consume=False
        #       ),  # ok
        #     # S(["letter_rspec"], print_params_to_console, use_spoken=True),
        #     # R(Function(alphanumeric.letters2, extra={"letter"}),
        #
        #     # S(["evening"], print_params_to_console, use_spoken=True),
        #     # S(["noon"], print_params_to_console, parameters=["some parameters"]),
        #     # S(["noon"], print_params_to_console, parameters=["some parameters"]),
        #     # S(["midnight"], print_params_to_console, use_rspec=True),
        # )
        # ]
        # ),

        "then":
            R(
                F(prepareStorage_forQueuingCommandsHistory)
              + AsynchronousAction(
                  [L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
                  # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
                  time_in_seconds=1,
                  # repetitions=0,
                  repetitions=1000,
                  rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
                  # rdescript="",
                  blocking=True,
                  finisher=F(on_QueuingConditionMet) #what to do when all the queues commands has been execute.
                  )  # End AsynchronousAction()

              , rdescript=""
              )  # End R()

    } #End mapping

    extras = [
        # --
        Dictation("text"),

    ]
    defaults = {"text":""}

def get_rule():
    # print "\n", "20200324004713| Callers::",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # for i in range(1, 16):
    # 	try:
    # 		print "\t","",stack()[i][3],"%s:%d" % (getframeinfo(stack()[i][0]).filename, getframeinfo(stack()[i][0]).lineno)
    # 	except:
    # 		print ""
    # 		break
    # return queuingTrigger, RuleDetails(ccrtype=CCRType.GLOBAL)

    details = RuleDetails(name="queuing Trigger")
    return queuingTrigger, details