from castervoice.lib.merge.ccrmerging2.hooks.events.base_event import BaseHookEvent
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType


class registerRule_ExclEvent(BaseHookEvent):
    def __init__(self, active_mrs=None, managed_rule=None, mappingRule_anabled=None):
        super(registerRule_ExclEvent, self).__init__(EventType.RULES_LOADED_EXCL)
        self.active_mrs = active_mrs #(mrs: 'Managed RuleS'?)
        self.managed_rule = managed_rule

        self.mappingRule_anabled = mappingRule_anabled
