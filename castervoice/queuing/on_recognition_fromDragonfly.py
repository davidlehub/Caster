# TODO: to delete: no need cz: using History function already there in Caster
#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
from castervoice.queuing.cls.Queue_cls import Queue_cls
from castervoice.queuing.globalVariables.queues import queues

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

class on_recognition_DataShare(): #Static for sharing data
    enable_recording_spoken = False
    Queue = None  # type: Queue_cls

def on_recognition_fromDragonfly(words):
    print "\n|-- (Don't use this any more)|" ,  "--| 20200401055206 |"
    # print "\n|-- on_recognition_fromDragonfly()| words:", words,  "--| 20200401055206 |"

    if on_recognition_DataShare.enable_recording_spoken:
        # Queue = Queue_cls()
        Queue = on_recognition_DataShare.Queue  # type: Queue_cls
        # Queue.spokens
        Queue.utterances.append(words)
        print "\n|-- Queue.utterances:", Queue.utterances,  "--| 20200401104818 |"

        # queues.append(Queue)
    else:
        pass
