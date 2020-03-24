#--- (David)
from inspect import getframeinfo, stack, getframeinfo, currentframe

from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

# from castervoice.lib._tests.GlabalStorage.allGrammars import all_loadedRule_mappingRule, all_Merge_result
from castervoice.exclusiveness.globalVariable import GlobalV as gl
# from castervoice.lib.ctrl.mgr.rule_details.RuleDetails

def storeAll_mergedCcr(all_Merge_result):

	#__ TODO: (not important) do it only if the list is different?
	gl.all_Merge_result = all_Merge_result
	# gl.all_Merge_result = list(all_Merge_result)
	print "\n", "20200321231424| gl.all_Merge_result.all_rule_class_names:", gl.all_Merge_result.all_rule_class_names, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

			
class storeAll_mergedCcr_Hook(BaseHook):
	def __init__(self):
		super(storeAll_mergedCcr_Hook, self).__init__(EventType.REMERGE_CCR_RULES_EXCL)

	def get_pronunciation(self):
		return "ccr rule storage"

	def run(self, event_data):
		all_Merge_result = event_data.all_Merge_result
		
		storeAll_mergedCcr(all_Merge_result)

def get_hook():
	return storeAll_mergedCcr_Hook