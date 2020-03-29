#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict
# from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from dragonfly.engines import (_default_engine)
# from castervoice.exclusiveness.makeDragonHeard import makeDragonHeard

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

class DragonVocabulary_cls(object):
    """
     """
    _enabled = None  # type: bool
    def __init__(self):
        self.temporary_Disabled = False
        self.temporary_Enabled = False
        self.enabled = None  # type: bool

    # region__(decided: not really necessary to make property: just just attribute/field)
    # @property
    # def temporary_Disabled(self):
    #     return self._temporaryDisabled
    # @temporary_Disabled.setter
    # def temporary_Disabled(self, value):
    #     self._temporaryDisabled = value
    #
    # @property
    # def temporary_Enabled(self):
    #     return self._temporaryEnabled
    # @temporary_Enabled.setter
    # def temporary_Enabled(self, value):
    #     """
    #
    #     :type value: bool
    #     """
    #     self._temporaryEnabled = value
    #
    # @property
    # def enabled(self):
    #     return self._enabled
    # @enabled.setter
    # def enabled(self, value):
    #     # type: (bool) -> bool
    #     """
    #
    #     :param value: bool
    #     :rtype: bool
    #     """
    #     self._enabled = value
    #

    # endregion (decided: not really necessary to make property:)

    # region__(Methode)
    # def enable(self):
    def disable(self):

        """

        :rtype: None
        """
        # DragonVocabulary.enable()
        # ExclusivMode.set_enabled(True) #TODO: to remove
        # self.enabled = True
        self.enabled = False

        # Set_Exclusiveness_ForRules(gl.RbeenActive)

        for grammar in _default_engine.grammars:
            # if grammar.loaded:
            #     grammar.set_exclusiveness(0)
            #     print "\n", "20200323162038| grammar exclusive = 0:",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

            grammar.set_exclusiveness(1)
            # print "\n", "20200323162037| grammar exclusive = 1:",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

            if grammar not in gl.GbeenExclusive:
                gl.GbeenExclusive.append(grammar)

        # print "\n", "(exclusiveness) is OFF."
        print "\n", "(exclusiveness) is ON."

    # def disable(self):
    def enable(self):

        # type: () -> None

        # DragonVocabulary.disable()
        # __
        # ExclusivMode.set_enabled(False) #TODO: to remove
        # self.enabled = False
        self.enabled = True

        # print "\n", "20200323162131a| Before gl.GbeenExclusive:",_NEXUS._grammar_manager._grammars_container._ccr_grammars, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        # print "\n", "20200323162131b| Before gl.GbeenExclusive:",_NEXUS._grammar_manager._grammars_container._non_ccr_grammars, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        # print "\n", "20200323162131| Before gl.GbeenExclusive:",[i.name for i in gl.GbeenExclusive], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

        # __ turn OFF exclusiveness for grammars
        # for grammar in gl.GbeenExclusive:
        for grammar in _default_engine.grammars:

            grammar.set_exclusiveness(0)
            # print "\n", "20200323162038| grammar exclusive = 0:",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

            try:
                gl.GbeenExclusive.remove(grammar)
            except:
                pass

        # print "\n", "(exclusiveness) is ON."
        print "\n", "(exclusiveness) is OFF."


    # endregion (Methode)

_DragonVocabulary = DragonVocabulary_cls()

# __all__ = ['enable_dragonVocabulary', 'disable_dragonVocabulary']

def enable_dragonVocabulary():
    _DragonVocabulary.enable()

def disable_dragonVocabulary():
    _DragonVocabulary.disable()


    # self.temporary_Disabled = False
    # self.temporary_Enabled = False
    # self.enabled = None  # type: bool
def enable_temporary_dragonVocabulary():
    _DragonVocabulary.enable()
    _DragonVocabulary.temporary_Enabled = True

def  dragonVocabulary_wasTemporary_enabled():
    if _DragonVocabulary.temporary_Enabled:
        return True
    else:
        return False

def disable_temporary_dragonVocabulary():
    _DragonVocabulary.disable()
    _DragonVocabulary.temporary_Disabled = True

def  dragonVocabulary_wasTemporary_disable():
    if _DragonVocabulary.temporary_Enabled:
        return True
    else:
        return False


def dragonVocabulary_is_Enabled():
    if _DragonVocabulary.enabled:
        return True
    else:
        return False

def dragonVocabulary_is_Disabled():
    if _DragonVocabulary.enabled:
        return False
    else:
        return True

def indicate_DragonVocabulary_is_Disabled():
    _DragonVocabulary.enabled = False

def indicate_DragonVocabulary_is_Enabled():
    _DragonVocabulary.enabled = True