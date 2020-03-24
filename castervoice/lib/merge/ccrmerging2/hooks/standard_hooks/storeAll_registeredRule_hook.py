#--- (David)
#region--- (import)
from inspect import getframeinfo, stack, getframeinfo, currentframe

from castervoice.lib import printer
from castervoice.lib.merge.ccrmerging2.hooks.base_hook import BaseHook
from castervoice.lib.merge.ccrmerging2.hooks.events.event_types import EventType

# from castervoice.lib._tests.GlabalStorage.allGrammars import all_MappingRule, all_MergeRule
from castervoice.exclusiveness.globalVariable import GlobalV as gl
# from castervoice.lib.ctrl.mgr.rule_details.RuleDetails
from castervoice.exclusiveness.globalVariable.registeredRule_data import registeredRule_data
#endregion (import)


# def storeAll_RegisteredRule(merge_rules=None, mapping_rule=None, mappingRule_anabled=None):
def storeAll_registeredRule(Rule_className, Rdetail, rule_class):
	#--- For More info: on 'RuleDetails of: each rule in merge_rules, and  mapping_rule: C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\rule_details.py

	#--- 
	registeredRuleData = registeredRule_data(Rule_className, Rdetail, rule_class)
	#--- 
	gl.allRegisteredRule.add(registeredRuleData)

	#--- store rules having AppContext:
	# print "\n", "ici 20200312212544| Rdetail.executable:", Rdetail.executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	if (Rdetail.executable != None) or (Rdetail.title != None):
		gl.allRegisteredRule_HavingAppContext.add(registeredRuleData)

	return



	# if merge_rules:
	# 	# all_MergeRule = set()

	# 	for rule in merge_rules: # list
      
	# 		Rdetail = rule.get_details()
			
	# 		#region--- (Get to know infos)
	# 		# #--- .get_details()
	# 		# Rdetail = rule.get_details()
	# 		# print "\n", "20200314175916| RuleDetails attributes:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		# print "\tRdetail.name: ",Rdetail.name 
	# 		# print "\tRdetail.function_context: ",Rdetail.function_context 
	# 		# print "\tRdetail.executable: ",Rdetail.executable 
	# 		# print "\tRdetail.title: ",Rdetail.title 
	# 		# print "\tRdetail.grammar_name: ",Rdetail.grammar_name 
	# 		# print "\tRdetail.declared_ccrtype: ",Rdetail.declared_ccrtype 
	# 		# print "\tRdetail.transformer_exclusion: ",Rdetail.transformer_exclusion 
	# 		# print "\tRdetail.watch_exclusion: ",Rdetail.watch_exclusion 
	# 		# print "\tRdetail._filepath: ",Rdetail._filepath 
	# 		#endregion (Get to know infos)
			
	# 		# print "", "20200312151237| ",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		#--- store those info globaly. Gonna needed for exclusiveness syst.
	# 		# if rule not in all_MergeRule:
	# 		# gl.all_MergeRule.add(rule.get_rule_class_name())
	# 		gl.all_MergeRule.add(rule)
	# 		print "\n", "20200319193148| a merged Rule is add to gl.all_MergeRule. Rdetail._filepath:", Rdetail._filepath, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)


	# 		# #--- store Those having AppContext:
	# 		# print "\n", "ici 20200312212544| Rdetail.executable:", Rdetail.executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# 		if (Rdetail.executable != None) or (Rdetail.title != None):
	# 			gl.all_RuleHavingAppContext_className.add(rule)
	# 			print "\n", "20200312212544| add a Mergerd Rule to set: gl.all_RuleHavingAppContext_className. Rdetail._filepath:", Rdetail._filepath, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	# print "\n", "20200312212545| gl.all_MergeRule:", gl.all_MergeRule, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# elif mapping_rule: # Not a list
     
	# 	#region--- (Get to know infos)
	# 	# Rdetail = mapping_rule.get_details()
	# 	# print "\n", "20200314175917| RuleDetails attributes:",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	# print "\tRdetail.name: ",Rdetail.name 
	# 	# print "\tRdetail.function_context: ",Rdetail.function_context 
	# 	# print "\tRdetail.executable: ",Rdetail.executable 
	# 	# print "\tRdetail.title: ",Rdetail.title 
	# 	# print "\tRdetail.grammar_name: ",Rdetail.grammar_name 
	# 	# print "\tRdetail.declared_ccrtype: ",Rdetail.declared_ccrtype 
	# 	# print "\tRdetail.transformer_exclusion: ",Rdetail.transformer_exclusion 
	# 	# print "\tRdetail.watch_exclusion: ",Rdetail.watch_exclusion 
	# 	# print "\tRdetail._filepath: ",Rdetail._filepath 

	# 	#endregion (Get to know infos)        

	# 	Rdetail = mapping_rule.get_details()
	# 	if mappingRule_anabled:
	# 		# gl.all_MappingRule.add(mapping_rule.get_rule_class_name())
	# 		gl.all_MappingRule.add(mapping_rule)
	# 		print "\n", "20200315130230| a Mapping Rule is add to gl.all_MappingRule. Rdetail._filepath:", Rdetail._filepath, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			
   
	# 		#--- store Those having AppContext:
	# 		if (Rdetail.executable != None) or (Rdetail.title != None):
	# 			gl.all_RuleHavingAppContext_className.add(mapping_rule)
	# 			print "\n", "20200315125340| add a Mapping Rule to set: gl.all_RuleHavingAppContext_className. Rdetail._filepath:", Rdetail._filepath, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 	elif not mappingRule_anabled:
	# 		try:
	# 			# gl.all_MappingRule.discard(mapping_rule.get_rule_class_name())
	# 			gl.all_MappingRule.discard(mapping_rule)
	# 			print "\n", "20200315130356| a Mapping Rule is REMOVED to gl.all_MappingRule. Rdetail._filepath:", Rdetail._filepath, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

	# 			#--- remove from the set: for Those having AppContext:
	# 			if (Rdetail.executable != None) or (Rdetail.title != None):
	# 				gl.all_RuleHavingAppContext_className.discard(mapping_rule)
	# 				print "\n", "20200315125346| remove a Mapping Rule from set: gl.all_RuleHavingAppContext_className. Rdetail._filepath:", Rdetail._filepath, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	# 		except:
	# 			pass
	# 	# print "\n", "20200312212546| gl.all_MappingRule:", gl.all_MappingRule, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			
class storeAll_registeredRule_hook(BaseHook):
	def __init__(self):
		super(storeAll_registeredRule_hook, self).__init__(EventType.REGISTER_Rule_EXCL)

	def get_pronunciation(self):
		return "registered rule storage"

	def run(self, event_data):
		# print "\n", "ici 20200316130401|in run :" , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		class_name = event_data.class_name
		details = event_data.details
		rule_class = event_data.rule_class
		
		storeAll_registeredRule(class_name, details,rule_class)

def get_hook():
	return storeAll_registeredRule_hook