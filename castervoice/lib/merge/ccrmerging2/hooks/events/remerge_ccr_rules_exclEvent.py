from castervoice.lib.merge.ccrmerging2.hooks.events.base_event import BaseHookEvent
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType


class remerge_ccr_rules_exclEvent(BaseHookEvent):
    def __init__(self, all_Merge_result):
        super(remerge_ccr_rules_exclEvent, self).__init__(EventType.REMERGE_CCR_RULES_EXCL)
        self.all_Merge_result = all_Merge_result