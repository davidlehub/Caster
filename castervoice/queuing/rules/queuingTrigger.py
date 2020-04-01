#region--- (Import)
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

from castervoice.exclusiveness.makeDragonHeard import makeDragonHeard
def makeDragonHeard_contextSeek(p):
	makeDragonHeard(pWords = p[0], pTime=p[1])

def print_params_to_console(params):
    print ("params:", params)

def triggerQueuing():
    pass

my_value = 0
# def queuing_spoken2(params):
def queuing_spoken2():
    global my_value

    global spoken_queue
    # spoken_queue.append(params)
    print "\n|-- spoken_queue:", spoken_queue,  "--| 20200331075617 |"

    my_value = my_value + 5
    print(my_value)
    if my_value == 10:
        my_value = 0
        return True
    return False
    # global spoken_queue
    # spoken_queue.append(params)
    # print "\n|-- spoken_queue:", spoken_queue,  "--| 20200331061848 |"
    #
    # makeDragonHeard_contextSeek([["then"], 0.0])

class UntilCancelled2(AsynchronousAction):
    def __init__(self, action, t=3):
        # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 100, "UC", False,
        AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 10, "UC", False,
                                    Text("fnished 20200331164105")) #ok it print out
                                    # None)
        self.show = True
        print "\n|-- ici",   "--| 20200331043832 |"
        AsynchronousAction.hmc_complete(None)

spoken_queue = []
# def queuing_spoken(params):
# def queuing_spoken(params=None):
# def makeDragonHeard_contextSeek(p):
	# makeDragonHeard(pWords = p[0], pTime=p[1])

def queuing_spoken(params=None):
    print "\n|-- params:", params,  "--| 20200331085920 |"
    global spoken_queue
    spoken_queue.append(params)
    print "\n|-- spoken_queue:", spoken_queue,  "--| 20200331061848 |"
    # return True

    # # an if : inside call only one: is triguer is not met.
    # UntilCancelled(
    #     checkFowWindowExist(*filter(lambda s: s != "then", params)), 1).execute()

    # makeDragonHeard(["len"])

    # region__{
    # # checkFowWindowExist()
    # # lambda fnparams: checkFowWindowExist(
    # f = lambda params: checkFowWindowExist(
    # # x = checkFowWindowExist(
    # #     Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(),  # orig
    # #     print_params_to_console(*filter(lambda s: s != "lenaaa", params)), 1).execute(), #TypeError: print_params_to_console() takes exactly 1 argument (2 given)
    #     print_params_to_console(*filter(lambda s: s != "lenaaa", params)), 3).execute()
    #     # print_params_to_console(params).execute(),
    #     # print_params_to_console(params).execute()) #err
    #     # print_params_to_console(params))
    # endregion__}


    # # checkFowWindowExist()
    # # lambda fnparams: checkFowWindowExist(
    # # lambda params: checkFowWindowExist(
    # # x = checkFowWindowExist(
    # checkFowWindowExist(
    #     # Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(),  # orig
    #     # print_params_to_console(*filter(lambda s: s != "lenaaa", params)), 1).execute(), #TypeError: print_params_to_console() takes exactly 1 argument (2 given)
    #     # print_params_to_console(params).execute(),
    #     # print_params_to_console(params).execute()) #err
    #     print_params_to_console(params)).execute()



    # makeDragonHeard_contextSeek([["then"], 0.0])


my_value = 0
# def repeat_me(param = None):
def repeat_me():
    global my_value
    my_value = my_value + 5
    print(my_value)
    if my_value == 10:
        my_value = 0
        return True
    return False


class UntilCancelled(AsynchronousAction):
    # def __init__(self, action, t=3):
    # def __init__(self, action, t=0.1):
    # def __init__(self, action, t=float("0.1")):
    def __init__(self, action, t=1):
        print "\n|-- action,t:", action, t, "--| 20200331103436 |"
        AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 10, "UC", True,
        # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], t, 10, "UC", False,
        # AsynchronousAction.__init__(self, [L(S(["cancel"], action))], float(t), 10, "UC", False,
                                    Text("fnished 20200331164105"))
        #                             None)
        self.show = True

# class check(ActionBase):
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
        print_params_to_console("blabl 20200331110042")
        return True

        # global _TEMP
        # _, orig = context.read_selected_without_altering_clipboard(False)
        # text = orig.replace(" ", self.space) if orig else ""
        # _TEMP = text.replace("\n", "") if self.remove_cr else text
        # return True

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

        # "then": R(  #
        #     F(triggerQueuing)
        #     # K(N_Mode)
        #     # K("c-s")
        #     , rdescript=""
        # )  # end 'R('
        # ,
        "noon time": R(Text("noon"), rspec="noon"),
        "cancel": R(Text(""), rspec="cancel"),
        "evening": R(Text("5 PM"), rspec="evening"),
        "midnight": R(Text("midnight"), rspec="midnight"),
        # "wait for": ContextSeeker(forward=[L(  # works

        # "then": ContextSeeker(forward=[L(  # works
        #     # S(["no time"], makeDragonHeard_contextSeek, parameters=[["then"], 0.0]), #ok
        #     # S(["!!!"], queuing_spoken, use_spoken=True), #err
        #     S(["no time"], queuing_spoken, use_spoken=True),
        #     S(["cancel"], NullAction()),
        #     # S(["noon"], print_params_to_console, parameters=["some parameters"]),
        #     S(["evening"], print_params_to_console, use_spoken=True),
        #     S(["midnight"], print_params_to_console, use_rspec=True),
        # )
        # ]
        # ),

        # "then": AsynchronousAction([L(S(["!"], repeat_me))]), #orig ok
        # "then": AsynchronousAction([L(S(["!"], repeat_me, use_spoken=True))]), #KeyError: 0
        # "then": AsynchronousAction([L(S(["!"], queuing_spoken ))]), #ok
        # "then": AsynchronousAction([L(S(["!"], queuing_spoken, parameters=["some parameters"] ))]), #ok
        # "then": AsynchronousAction([L(S(["!"], queuing_spoken, use_rspec=True ))]),
        # "then": AsynchronousAction([L(S(["!"], queuing_spoken, params=["sdf"]))]), #KeyError: 0

        "then": AsynchronousAction([L(S(["!"], queuing_spoken, use_spoken=True))]),
        # "then": AsynchronousAction([L(S(["evening"], print_params_to_console, use_spoken=True))]),
        #     S(["evening"], print_params_to_console, use_spoken=True),

        # "then": AsynchronousAction([L(S(["!"], queuing_spoken(), parameters=["some parameters"] ))]), #??
        # "then": AsynchronousAction([L(S(["!"], queuing_spoken(["sdfsdf"]) ))]),
        # "then": AsynchronousAction([L(S(["no time"], queuing_spoken, use_spoken=True))]), #no

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


        # "then":
        #     ContextSeeker(forward=[
        #         L(
        #             S(["cancel"], lambda: None),
        #             S(["*"],
        #               lambda fnparams: checkFowWindowExist(
        #                   # Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(), #orig
        #                   # Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(),
        #                   # print_params_to_console(*filter(lambda s: s != "periodic", fnparams)), 1).execute(), #TypeError: print_params_to_console() takes exactly 1 argument (2 given)
        #                   # print_params_to_console(filter(lambda s: s != "periodic", fnparams)), 1).execute(), #ok
        #                   # print_params_to_console(filter(lambda s: s != "periodic", fnparams)), 1).execute(), #
        #                   print_params_to_console(filter(lambda s: s != "then", fnparams)), 1).execute(), #
        #               use_spoken=True))
        #     ]),



        # "then": AsynchronousAction([L(S(["!"], queuing_spoken2,use_spoken=True))]), #no
        # "then": AsynchronousAction([L(S(["!"], queuing_spoken2))]), #ok



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
