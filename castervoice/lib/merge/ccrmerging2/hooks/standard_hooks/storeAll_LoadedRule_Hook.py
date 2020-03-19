#--- (David)
from inspect import getframeinfo, stack, getframeinfo, currentframe

from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

# from castervoice.lib._tests.GlabalStorage.allGrammars import all_loadedRule_mappingRule, all_loadedRule_mergeRule
from castervoice.exclusiveness.globalVariable import GlobalV as gl
# from castervoice.lib.ctrl.mgr.rule_details.RuleDetails

def storeAll_LoadedRule(merge_rules=None, mapping_rule=None, mappingRule_anabled=None):
	#--- For More info: on 'RuleDetails of: each rule in merge_rules, and  mapping_rule: C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\rule_details.py

	if merge_rules: # list of <castervoice.lib.ctrl.mgr.managed_rule.ManagedRule ...>
		# all_loadedRule_mergeRule = set()

		for rule in merge_rules: # list
	  
			#region--- (Get to know infos)
			# #--- .get_details()
			# Rdetail = rule.get_details()
			# print "\n", "20200314175916| RuleDetails attributes:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			# print "\tRdetail.name: ",Rdetail.name 
			# print "\tRdetail.function_context: ",Rdetail.function_context 
			# print "\tRdetail.executable: ",Rdetail.executable 
			# print "\tRdetail.title: ",Rdetail.title 
			# print "\tRdetail.grammar_name: ",Rdetail.grammar_name 
			# print "\tRdetail.declared_ccrtype: ",Rdetail.declared_ccrtype 
			# print "\tRdetail.transformer_exclusion: ",Rdetail.transformer_exclusion 
			# print "\tRdetail.watch_exclusion: ",Rdetail.watch_exclusion 
			# print "\tRdetail._filepath: ",Rdetail._filepath 
			#endregion (Get to know infos)
			
			#--- store those info globaly. Gonna needed for exclusiveness syst.
			gl.all_loadedRule_mergeRule.append(rule)

			print "\n", "20200315125726| MERGED loaded:", rule.get_rule_class_name(), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)


			# #--- store Those having AppContext:


	elif mapping_rule: # Not a list. Is a type: <<castervoice.lib.ctrl.mgr.managed_rule.ManagedRule ...>
	 
		#region--- (Get to know infos)
		# Rdetail = mapping_rule.get_details()
		# print "\n", "20200314175917| RuleDetails attributes:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# print "\tRdetail.name: ",Rdetail.name 
		# print "\tRdetail.function_context: ",Rdetail.function_context 
		# print "\tRdetail.executable: ",Rdetail.executable 
		# print "\tRdetail.title: ",Rdetail.title 
		# print "\tRdetail.grammar_name: ",Rdetail.grammar_name 
		# print "\tRdetail.declared_ccrtype: ",Rdetail.declared_ccrtype 
		# print "\tRdetail.transformer_exclusion: ",Rdetail.transformer_exclusion 
		# print "\tRdetail.watch_exclusion: ",Rdetail.watch_exclusion 
		# print "\tRdetail._filepath: ",Rdetail._filepath 

		#endregion (Get to know infos)        

		if mappingRule_anabled:
			# gl.all_loadedRule_mappingRule.add(mapping_rule.get_rule_class_name())
			gl.all_loadedRule_mappingRule.append(mapping_rule)

			print "\n", "20200319083742| MAPPING loaded and ENABLED :", mapping_rule.get_rule_class_name(), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			
		elif not mappingRule_anabled:
			try:
				# gl.all_loadedRule_mappingRule.discard(mapping_rule.get_rule_class_name())
				gl.all_loadedRule_mappingRule.remove(mapping_rule)

				print "\n", "20200319083743| MAPPING loaded and DISABLED :", mapping_rule.get_rule_class_name(), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			except:
				pass
			
class storeAll_LoadedRule_Hook(BaseHook):
	def __init__(self):
		super(storeAll_LoadedRule_Hook, self).__init__(EventType.RULES_LOADED_EXCL)

	def get_pronunciation(self):
		return "rule storage"

	def run(self, event_data):
		merge_rules = event_data.active_mrs
		mapping_rule = event_data.managed_rule
		mappingRule_anabled = event_data.mappingRule_anabled
		
		storeAll_LoadedRule(merge_rules, mapping_rule, mappingRule_anabled)

def get_hook():
	return storeAll_LoadedRule_Hook