from castervoice.lib.merge.ccrmerging2.hooks.events.base_event import BaseHookEvent
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType
from inspect import getframeinfo, stack, getframeinfo, currentframe


class registerRule_ExclEvent(BaseHookEvent):
    def __init__(self, class_name=None, details=None):
        # print "\n", "20200316121143| class_name:", class_name, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        super(registerRule_ExclEvent, self).__init__(EventType.REGISTER_Rule_EXCL)
        self.class_name = class_name
        self.details = details