from castervoice.lib.merge.ccrmerging2.hooks.events.base_event import BaseHookEvent
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType


class registerRule_ExclEvent(BaseHookEvent):
    def __init__(self, class_name, details):
        super(registerRule_ExclEvent, self).__init__(EventType.REGISTER_Rule_EXCL)
        self.class_name = class_name
        self.details = details