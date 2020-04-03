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


def triggerQueuing():
    pass



class StoreCommands_ToExcute_OnConditionMet(AsynchronousAction):
    Queue = None  # type: Queue_cls

    def __init__(self, conditionToCheckRepeatly, t=1):

        # prepareStorage_forCommandsHistory(StoreCommands_ToExcute_OnConditionMet.Queue)
        StoreCommands_ToExcute_OnConditionMet.Queue = StoreCommands_ToExcute_OnConditionMet.prepareStorage_forQueuingCommandsHistory()  # type: Queue_cls
        # AsynchronousAction.__init__(self, [L(S(["cancel"], conditionToCheckRepeatly))], t, 100, "UC", False,
        AsynchronousAction.__init__(self,
            [L(S(["cancel"], conditionToCheckRepeatly))],
            t,
            100,
            "some description |20200402140843",
            True,
            StoreCommands_ToExcute_OnConditionMet.on_QueuingConditionMet(StoreCommands_ToExcute_OnConditionMet.Queue)
            ) #End AsynchronousAction.__init__()
        self.show = True #??

    # def prepareStorage_forCommandsHistory(self, Queue):
    # @staticmethod
    # def prepareStorage_forQueuingCommandsHistory():
    #     # type: () -> Queue_cls
    #     Queue = Queue_cls()
    #     Queue.get_and_register_history()
    #
    #     return Queue

    @staticmethod
    def  on_QueuingConditionMet(Queue):
        # type: (Queue_cls) -> None
        """

        :type Queue:Queue_cls
        :rtype: None
        """
        print "\n|-- in 'on_QueuingConditionMet()':", Queue,  "--| 20200402021207 |"

my_value = 0
spoken_queue = []
triggerMet_StartQueuingSequences = False
def storeSpoken_inQueue(params):
    #__ ToRemeber: it is not depend on App. in otw, event is the app change, it keep storing spokens. (but it relate to the app that start the queue storing ??)

    #__ Create new Queue in to Queues list
    #__ by telling on_recognition_fromDragonfly() to do it
    # on_recognition_DataShare.Queue = Queue_cls()
    # on_recognition_DataShare.enable_recording_spoken = True


    # global  been_CheckingforWindowExist

    global spoken_queue, triggerMet_StartQueuingSequences
    spoken_queue.append(params)
    print "\n|-- spoken_queue:", spoken_queue,  "--| 20200331061848 |"

    # an if : inside call only one: if triguer is not met ...
    if not checkFowWindowExist.been_CheckingforWindowExist:
        # StoreCommands_ToExcute_OnConditionMet( checkFowWindowExist(*filter(lambda s: s != "then", params)), 1 ).execute()
        StoreCommands_ToExcute_OnConditionMet(checkFowWindowExist(None, None), 1).execute() #old, may not compatible...
        checkFowWindowExist.been_CheckingforWindowExist = True
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
        checkFowWindowExist.been_CheckingforWindowExist = False
        triggerMet_StartQueuingSequences = False
        spoken_queue = []

        my_value = 0


AsynchronousAction_Stoping_spec = "cancel"


# _history = get_and_register_history(10)
# been_CheckingforWindowExist = False

class checkFowWindowExist(ActionBase):
    been_CheckingforWindowExist = False
    _history = None

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
        print "\n|-- _history:", checkFowWindowExist._history,  "--| 20200402084547 |"

        # region__ run only once
        # global been_CheckingforWindowExist
        # if not on_recognition_DataShare.enable_recording_spoken:
        if not checkFowWindowExist.been_CheckingforWindowExist:
            print "\n|-- enable_recording_spoken",   "--| 20200401104625 |"

            checkFowWindowExist._history = get_and_register_history(10)

            # __ Create new Queue in to Queues list
            # __ by telling on_recognition_fromDragonfly() to do it
            on_recognition_DataShare.Queue = Queue_cls()
            on_recognition_DataShare.enable_recording_spoken = True

            #__
            # StoreCommands_ToExcute_OnConditionMet( checkFowWindowExist(*filter(lambda s: s != "then", params)), 1 ).execute()
            # StoreCommands_ToExcute_OnConditionMet(checkFowWindowExist(None, None), 1).execute()

            checkFowWindowExist.been_CheckingforWindowExist = True
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
            print "\n|-- [i.utterances for i in queues]:", [i.utterances for i in queues],  "--| 20200401110510 |"
            on_recognition_DataShare.Queue = None

            my_value = 0
            # return True
            checkFowWindowExist.been_CheckingforWindowExist = False

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
#__ ____________________________________________



Queue = None  # type:Queue_cls
# def prepareStorage_forQueuingCommandsHistory():
# def prepareStorage_forQueuingCommandsHistory(params):
# def prepareStorage_forQueuingCommandsHistory(text):
def prepareStorage_forQueuingCommandsHistory(params=None):
    # type: () -> Queue_cls
    
    print "\n|-- in 'prepareStorage_forQueuingCommandsHistory()'|params:",params,   "--| 20200402105707 |"
    # print "\n|-- in 'prepareStorage_forQueuingCommandsHistory()'|text:",text,   "--| 20200402105707 |"

    global Queue
    Queue = Queue_cls()
    Queue.get_and_register_history()

    # return Queue


# region__ (Simulate waiting for window to exist)
# my_value = 0
# def RepeatlyCheck_ifWindowExist():
#     global my_value
#     my_value = my_value + 5
#     print(my_value)
#     if my_value == 40:
#         my_value = 0
#         return True #When return True: it stop the Asyncho. reapeter.
#     return False
# endregion }__ (Simulate waiting for window to exist)

# def  on_QueuingConditionMet(Queue = None):
# def  on_QueuingConditionMet(Queue):

# def RepeatlyCheck_ifWindowExist(winTitle, winClass):
# def RepeatlyCheck_ifWindowExist(windowname=None, executable=None):

def RepeatlyCheck_ifWindowExist(p):
    # Window.get_foreground().handle

    # targetWind = BaseWindow
    # targetWind.executable = p[0]
    # targetWind.title = p[1]

    # targetWind.get_matching_windows()
    # Save As ahk_class #32770
    # if window_exists(windowname=None, executable=None):
    windowname = p[0]
    executable = p[1]
    # print "\n|--p:", p,  "--| 20200402081642 |"
    print "\n|--windowname,executable :", windowname,executable,  "--| 20200402081642 |"
    if window_exists(windowname=windowname, executable=executable):
        #__ focus on that window
        FocusWindow(title=windowname, executable=executable)
        time.sleep(0.3) # give a chance to window appear.
        # Window.set_focus()
        # targetWind.set_focus()
        # set_focus()

        return   True
    else:
        return  False



#__ get window title.
    #__ get window class.


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
        # R(F(prepareStorage_forQueuingCommandsHistory, extra={"modifier"}),rspec="then_rspec")
        # R(F(prepareStorage_forQueuingCommandsHistory, params="%(text)s")
            R(F(prepareStorage_forQueuingCommandsHistory)
              + AsynchronousAction(
                  [L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
                  # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
                  time_in_seconds=1,
                  # repetitions=0,
                  repetitions=1000,
                  rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
                  # rdescript="",
                  blocking=True,
                  finisher=F(on_QueuingConditionMet)
                )  # End AsynchronousAction()
              , rspec="then_rspec"
              )  # End R()
        
              #   + ContextSeeker(forward=[
            #     L(
            #         # S(["cancel"], lambda: None),
            #         S([AsynchronousAction_Stoping_spec], lambda: None),  # we need this??
            #         S(["*"],
            #           # lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
            #           #     checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(),
            #           # R(K("t") + F(repeat_me), rdescript=""), #ok
            #           # R(K("t") + AsynchronousAction([L(S(["!"], repeat_me))]), rdescript=""), #ok
            #           # R(F(prepareStorage_forQueuingCommandsHistory, params="%(text)s")
            #           # R(F(prepareStorage_forQueuingCommandsHistory)
            #           R(
            #               # + AsynchronousAction(
            #               AsynchronousAction(
            #                   [L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
            #                   # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
            #                   time_in_seconds=1,
            #                   # repetitions=0,
            #                   repetitions=1000,
            #                   rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
            #                   # rdescript="",
            #                   blocking=True,
            #                   finisher=F(on_QueuingConditionMet)
            #               )  # End AsynchronousAction()
            #               , rdescript=""),  # End R()
            #           use_spoken=True,
            #           consume=True
            #           )  # End S()
            #     )  # End L()
            #     # ]),
            # ])  # End ContextSeeker()
            #   , rspec="then_rspec"
            #   )  # End R()

        # region__ (almost)
        # "then [<text>]":
        # "then":
        # # R(F(prepareStorage_forQueuingCommandsHistory, extra={"modifier"}),rspec="then_rspec")
        # # R(F(prepareStorage_forQueuingCommandsHistory, params="%(text)s")
        #     R(F(prepareStorage_forQueuingCommandsHistory)
        #       + ContextSeeker(forward=[
        #         L(
        #             # S(["cancel"], lambda: None),
        #             S([AsynchronousAction_Stoping_spec], lambda: None),  # we need this??
        #             S(["*"],
        #               # lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
        #               #     checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(),
        #               # R(K("t") + F(repeat_me), rdescript=""), #ok
        #               # R(K("t") + AsynchronousAction([L(S(["!"], repeat_me))]), rdescript=""), #ok
        #               # R(F(prepareStorage_forQueuingCommandsHistory, params="%(text)s")
        #               # R(F(prepareStorage_forQueuingCommandsHistory)
        #               R(
        #                 # + AsynchronousAction(
        #                 AsynchronousAction(
        #                   [L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
        #                   # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
        #                   time_in_seconds=1,
        #                   # repetitions=0,
        #                   repetitions=1000,
        #                   rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
        #                   # rdescript="",
        #                   blocking=True,
        #                   finisher=F(on_QueuingConditionMet)
        #                   )  # End AsynchronousAction()
        #                 , rdescript=""),  # End R()
        #               use_spoken=True,
        #               consume=True
        #               )  # End S()
        #         )  # End L()
        #         # ]),
        #         ])  # End ContextSeeker()
        #       , rspec="then_rspec"
        #       )  # End R()
        # endregion }__ (almost)

        # region__ (not working)
        # "then [<text>]":
        #     # R(F(prepareStorage_forQueuingCommandsHistory, extra={"modifier"}),rspec="then_rspec")
        #     # R(F(prepareStorage_forQueuingCommandsHistory, params="%(text)s")
        #     R(F(prepareStorage_forQueuingCommandsHistory)
        #         + ContextSeeker(forward=[
        #           L(
        #             # S(["cancel"], lambda: None),
        #             S([AsynchronousAction_Stoping_spec], lambda: None), #we need this??
        #             S(["*"],
        #                   # lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
        #                   #     checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(),
        #                   # R(K("t") + F(repeat_me), rdescript=""), #ok
        #                   # R(K("t") + AsynchronousAction([L(S(["!"], repeat_me))]), rdescript=""), #ok
        #                   # R(F(prepareStorage_forQueuingCommandsHistory, params="%(text)s")
        #                   R(F(prepareStorage_forQueuingCommandsHistory)
        #                     + AsynchronousAction(
        #                       [L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
        #                       # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
        #                       time_in_seconds=1,
        #                       # repetitions=0,
        #                       repetitions=1000,
        #                       rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
        #                       # rdescript="",
        #                       blocking=True,
        #                       finisher=F(on_QueuingConditionMet)
        #                   )  # End AsynchronousAction()
        #                   , rdescript=""),  # End R()
        #                   # use_spoken=True
        #                   )  # End S()
        #           )  # End L()
        #         # ]),
        #         ]) #End ContextSeeker()
        #     , rspec = "then_rspec"
        #     ) #End R()
        # endregion }__ (not working)

        # region__  go err: TypeError: dragonfly_data <{'textnv': '', 'nnavi50': 1, 'big': False, '_grammar': Grammar(ccr-1), 'spacing': 0, 'mtn_dir': 'right', 'nnavi10': 1, 'npunc': 1, 'extreme': None, 'modifier': '', 'nnavi3': 1, 'capitalization': 0, 'npunc100': 1, '_rule': PreparedRule(PreparedRule), '_node': Node: Alternative(...), [u'then'], 'long': '', 'mtn_mode': None, 's': '', 'n': 1, 'app': None, 'nnavi500': 1, 'splatdir': 'backspace'}>
        # "then":
        #     # R(F(prepareStorage_forQueuingCommandsHistory, extra={"modifier"}),rspec="then_rspec")
        #     R(F(prepareStorage_forQueuingCommandsHistory),rspec="then_rspec")
        #     + ContextSeeker(forward=[
        #         L(
        #             # S(["cancel"], lambda: None),
        #             S([AsynchronousAction_Stoping_spec], lambda: None),
        #             S(["*"],
        #               # lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
        #               #     checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(),
        #               # R(K("t") + F(repeat_me), rdescript=""), #ok
        #               # R(K("t") + AsynchronousAction([L(S(["!"], repeat_me))]), rdescript=""), #ok
        #               R(F(prepareStorage_forQueuingCommandsHistory)
        #                 + AsynchronousAction(
        #                   [L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
        #                   # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
        #                   time_in_seconds=1,
        #                   # repetitions=0,
        #                   repetitions=1000,
        #                   rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
        #                   # rdescript="",
        #                   blocking=True,
        #                   finisher=F(on_QueuingConditionMet)
        #                   )  # End AsynchronousAction()
        #                 , rdescript=""),  # End R()
        #               # use_spoken=True
        #               )  # End S()
        #         )  # End L()
        #     ]),
        # endregion }__  go err:

        # region__ Version with 'then' only not working
        # "then":
        #     ContextSeeker(forward=[
        #         L(
        #             # S(["cancel"], lambda: None),
        #             S([AsynchronousAction_Stoping_spec], lambda: None),
        #             S(["*"],
        #               # lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
        #               #     checkFowWindowExist(*filter(lambda s: s != "then", fnparams)), 1).execute(),
        #               # R(K("t") + F(repeat_me), rdescript=""), #ok
        #               # R(K("t") + AsynchronousAction([L(S(["!"], repeat_me))]), rdescript=""), #ok
        #               R(  F(prepareStorage_forQueuingCommandsHistory)
        #                 + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist, parameters=['Save As', 'notepad']))],
        #                 # + AsynchronousAction([L(S(["!"], RepeatlyCheck_ifWindowExist,windowname="Save As", executable="notepad"))],
        #                                      time_in_seconds=1,
        #                                      # repetitions=0,
        #                                      repetitions=1000,
        #                                      rdescript="wait for window to exist: windowname='Save As', executable='notepad'",
        #                                      # rdescript="",
        #                                      blocking=True,
        #                                      finisher=F(on_QueuingConditionMet)
        #                                     ) #End AsynchronousAction()
        #                 , rdescript=""), #End R()
        #               # use_spoken=True
        #              ) #End S()
        #          ) #End L()
        #     ]),
        # endregion }__ Version with 'then' only not working

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
        #               # lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
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
        #               lambda fnparams: StoreCommands_ToExcute_OnConditionMet(
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