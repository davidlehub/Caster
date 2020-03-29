from castervoice.lib import settings, textformat
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType
from castervoice.lib import printer
from castervoice.exclusiveness.cls.DragonVocabulary_cls import DragonVocabulary

#region--- (david)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
# from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode

#endregion (david)



def _apply_exclusiveness(grammar):
    #region--- (david)
    if  DragonVocabulary.enabled: return
    # if not DragonVocabulary.enabled: return
    # if not ExclusivMode.enabled: return
    #endregion (david)
    
    try:
        grammar.set_exclusiveness(1)
        
        #region--- (david)
        if grammar not in gl.GbeenExclusive:
            gl.GbeenExclusive.append(grammar)
        #endregion (david)


        # print "\n", "dbg20200322172337| grammar set_exclusiveness(1):",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    except Exception as e:
        printer.out(e)


class ExclusiveHook(BaseHook):
    def __init__(self):
        super(ExclusiveHook, self).__init__(EventType.GRAMMERS_LOADED)

    def get_pronunciation(self):
        return "exclusive"

    def run(self, event_data):
        grammar = event_data.grammar
        _apply_exclusiveness(grammar)


def get_hook():
    return ExclusiveHook
