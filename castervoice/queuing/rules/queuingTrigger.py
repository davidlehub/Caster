#region--- (Import)
import time
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.lib.merge.mergerule import MergeRule
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
from dragonfly import (Grammar, Playback, Key, Dictation, Function, Text, ActionBase)
from castervoice.lib.const import CCRType
from castervoice.lib.merge.state.actions import AsynchronousAction, ContextSeeker
from castervoice.lib.merge.state.actions2 import NullAction
from castervoice.lib.merge.state.short import R, S, L
from dragonfly.actions.action_mimic import Mimic
from castervoice.queuing.cls.Queue_cls import Queue_cls
from castervoice.queuing.globalVariables.queues import queues
from castervoice.queuing.on_recognition_fromDragonfly import on_recognition_fromDragonfly, on_recognition_DataShare
from castervoice.lib.util.recognition_history import get_and_register_history

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


def triggerQueuing():
    pass

class UntilCancelled(AsynchronousAction):
    def __init__(self, action, t=3):
        # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 100, "UC", False,
        AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 100, "UC", True,
                                    None)
        self.show = True


my_value = 0
spoken_queue = []
been_CheckingforWindowExist = False
triggerMet_StartQueuingSequences = False
def storeSpoken_inQueue(params):
    #__ ToRemeber: it is not depend on App. in otw, event is the app change, it keep storing spokens. (but it relate to the app that start the queue storing ??)

    #__ Create new Queue in to Queues list
    #__ by telling on_recognition_fromDragonfly() to do it
    on_recognition_DataShare.Queue = Queue_cls()
    on_recognition_DataShare.enable_recording_spoken = True


    global  been_CheckingforWindowExist

    global spoken_queue, triggerMet_StartQueuingSequences
    spoken_queue.append(params)
    print "\n|-- spoken_queue:", spoken_queue,  "--| 20200331061848 |"

    # an if : inside call only one: if triguer is not met ...
    if not been_CheckingforWindowExist:
        # UntilCancelled( checkFowWindowExist(*filter(lambda s: s != "then", params)), 1 ).execute()
        UntilCancelled( checkFowWindowExist(None, None ), 1).execute()
        been_CheckingforWindowExist = True
    else:
        print "\n|-- (skip calling Asynchornous (that check if window exit).",   "--| 20200401082031 |"

    #__ to keep catching spoken
    if not triggerMet_StartQueuingSequences:
        # makeDragonHeard(["then"])
        Mimic("then").execute()
    else:
        print "\n|-- stop getting spoken, bcz: triggerMet_StartQueuingSequences:", triggerMet_StartQueuingSequences,  "--| 20200401114138 |"
        # print "\n|-- stop getting spoken, bcz: triggerMet_StartQueuingSequences.",   "--| 20200401114138 |"
        Mimic(AsynchronousAction_Stoping_spec).execute()
        # makeDragonHeard([AsynchronousAction_Stoping_spec])

        #__ reset vars
        been_CheckingforWindowExist = False
        triggerMet_StartQueuingSequences = False
        spoken_queue = []

        my_value = 0


AsynchronousAction_Stoping_spec = "cancel"
# class UntilCancelled(AsynchronousAction):
#     # def __init__(self, action, t=3):
#     # def __init__(self, action, t=0.1):
#     # def __init__(self, action, t=float("0.1")):
#     def __init__(self, action, t=1):
#         print "\n|-- action,t:", action, t, "--| 20200331103436 |"
#         # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 10, "UC", True, # blocking ...
#         # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 10, "UC", False, #no blocking...
#         # # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], float(t), 10, "UC", False,
#         AsynchronousAction.__init__(self, [L(S([AsynchronousAction_Stoping_spec], action))], t, 10, "UC", False, #no blocking...
#         # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], float(t), 10, "UC", False,
#                                     Text("fnished 20200331164105"))
#         #                             None)
#         self.show = True


# region__ for simulate: trigger's condition me
my_value = 0
# endregion }__ for simulate: trigger's condition me
_history = get_and_register_history(10)
class checkFowWindowExist(ActionBase):
    def __init__(self, *words, **kwargs):
        ActionBase.__init__(self)
        self._words = tuple(words)
        if "extra" in kwargs:
            self._extra = kwargs.pop("extra")
        else:
            self._extra = None

        # Set pretty printing string used by __str__ and __unicode__.
        self._str = u", ".join(repr(w) for w in self._words)

        # # Make sure that all keyword arguments have been consumed.
        # if kwargs:
        #     raise ActionError("Invalid arguments: %r"
        #                       % ", ".join(list(kwargs.keys())))

    def _execute(self, data=None):
        # print_params_to_console("checking for window xx |20200401081906") #to remove: not usefull.

        # print "\n|-- (End of _excecute())",   "--| 20200401112219 |"

        # print "\n|-- get_and_register_history():", get_and_register_history(),  "--| 20200402083809 |"
        print "\n|-- _history:", _history,  "--| 20200402084547 |"

        # region__ run only once
        # global been_CheckingforWindowExist
        # if not been_CheckingforWindowExist:
        if not on_recognition_DataShare.enable_recording_spoken:
            print "\n|-- enable_recording_spoken",   "--| 20200401104625 |"
            # __ Create new Queue in to Queues list
            # __ by telling on_recognition_fromDragonfly() to do it
            on_recognition_DataShare.Queue = Queue_cls()
            on_recognition_DataShare.enable_recording_spoken = True

            #__
            # UntilCancelled( checkFowWindowExist(*filter(lambda s: s != "then", params)), 1 ).execute()
            # UntilCancelled(checkFowWindowExist(None, None), 1).execute()

            been_CheckingforWindowExist = True #?? still need?
        else:
            pass
            # print "\n|-- (skip calling Asynchornous (that check if window exit).", "--| 20200401224108 |"

        # endregion }__ ..

        # region__ for simulate: trigger's condition me
        global my_value, triggerMet_StartQueuingSequences
        my_value = my_value + 5
        print(my_value)
        if my_value == 45:
            print "\n|-- Indicate that Queuing trigger condition met.",   "--| 20200401113904 |"

            #__ Stop recoding/storing of recognised words
            on_recognition_DataShare.enable_recording_spoken = False

            #__ Add to list of queues before reinitialise to NOne
            queues.append(on_recognition_DataShare.Queue)
            print "\n|-- [i for i in queues]:", [i for i in queues],  "--| 20200401110510 |"
            on_recognition_DataShare.Queue = None

            my_value = 0
            # return True
            been_CheckingforWindowExist = False

            #__ So, Queuing trigger condition met:
            #__ stop the stop loping of checking if condition met, by stoping Asychronos ...
            triggerMet_StartQueuingSequences = True
            Mimic(AsynchronousAction_Stoping_spec).execute()
            # makeDragonHeard([AsynchronousAction_Stoping_spec])

        # endregion }__ for simulate: trigger's condition me




''' template:
   "vis": R( #
       # F(insertComment_simple)
       K(N_Mode)
       + K("v")
       , rdescript="|>-00- Vim start select. |" + stack()[0][3] + "|%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno)
       ) #end 'R('
       ,
'''
class queuingTrigger(MergeRule):
    mapping = {

        #__
        # "periodic":
        "then":
            ContextSeeker(forward=[
                L(
                    # S(["cancel"], lambda: None),
                    S([AsynchronousAction_Stoping_spec], lambda: None),
                    S(["*"],
                      lambda fnparams: UntilCancelled(
                          # Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(
                          checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(
                      ),
                      use_spoken=True))
            ]),

        # region__  ok, catching spoken |20200401110749
        # "then": ContextSeeker(forward=[L(  # works
        #     # S(["no time"], storeSpoken_inQueue, use_spoken=True),
        #     # S(["!!!"], storeSpoken_inQueue, use_spoken=True),
        #     S(["!!!"], storeSpoken_inQueue),
        # )
        # ]
        # ),

        # endregion }__

        # region__ great! Also, catching spoken. But lets use the 20200401110749
        # "then":
        #     ContextSeeker(forward=[
        #         L(
        #             # S(["!!"],  print_params_to_console, parameters=["some parameters"]),
        #
        #             S(["cancel"], lambda: None),
        #             S(["*"],
        #               # lambda fnparams: UntilCancelled(
        #               # lambda fnparams: UntilCancelled2( #modify this UntilCancelled2 to: catch spoken and store them in array.
        #               lambda fnparams: UntilCancelled3( #modify this UntilCancelled2 to: catch spoken and store them in array.
        #                   # Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(
        #                   #__ Instead of Mimic...: create my own DragonFly action that: store spoken
        #                   # storeSpoken_DragonflyAction(*filter(lambda s: s != "then", fnparams)), 1).execute(
        #                   # *filter(lambda s: s != "then", fnparams)).execute(
        #                   filter(lambda s: s != "then", fnparams)).execute(
        #               ),
        #               use_spoken=True))
        #     ]),

        # endregion }__ trying 20200401082616

        # region__ ok, but not for this use case
        # "then": #ok
        #     ContextSeeker(forward=[
        #         L(
        #             S(["cancel"], lambda: None),
        #             S(["*"],
        #               lambda fnparams: UntilCancelled(
        #                   # Mimic(*filter(lambda s: s != "then", fnparams)), 1).execute(
        #                   checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(
        #                   # print_params_to_console(*filter(lambda s: s != "then", fnparams)), 1).execute(
        #                   # print_params_to_console(*filter(lambda s: s != "then")), 1).execute( #TypeError: filter expected 2 arguments, got 1
        #               ),
        #               use_spoken=True))
        #     ]),
        # endregion }__ ok, but not for this use case

        # region__ ok
        # "then": AsynchronousAction([L(S(["!"], storeSpoken_inQueue, parameters=["some parameters"]))]),
        # endregion__} ok
    }


def get_rule():
    # print "\n", "20200324004713| Callers::",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # for i in range(1, 16):
    # 	try:
    # 		print "\t","",stack()[i][3],"%s:%d" % (getframeinfo(stack()[i][0]).filename, getframeinfo(stack()[i][0]).lineno)
    # 	except:
    # 		print ""
    # 		break
    return queuingTrigger, RuleDetails(ccrtype=CCRType.GLOBAL)
