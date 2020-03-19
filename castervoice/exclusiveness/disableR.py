from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.lib.control import _NEXUS
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from collections import OrderedDict


def disableR(RulesToDisable_className,aExceptR=[]):
	for RuleToDisable_className in RulesToDisable_className:
		if RuleToDisable_className in aExceptR:
			# gl.RbeenExclusive.add(RuleToDisable_className)
			continue

		#--- Optimization do it only if: the rule is loaded	
		# print "\n", "ici 20200319091514|  RuleToDisable_className:", RuleToDisable_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# print "\t", "ici 20200319091515|  [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]:", [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]

		#--- (Concatonate/add 2 list without duplicate element)
		all_loadedRule_class_Name =  list(OrderedDict.fromkeys([i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule] + [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]))
		# print "\n", "ici 20200319183135|  all_loadedRule_class_Name:", all_loadedRule_class_Name
		# print "\t", "ici 20200319091515|  [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]:", [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]
		# print "\t", "ici 20200319091516|  [i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule]:", [i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule]


		if RuleToDisable_className not in all_loadedRule_class_Name:
			print "\n", "ici20200319091146| skeep to disable rule:", RuleToDisable_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			# print "\t", "ici 20200319091515|  [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]:", [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]
			continue
		# if RuleToDisable_className not in [i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule]:
		# 	print "\n", "ici20200319091147| skeep to disable rule :", RuleToDisable_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	# print "\t", "ici 20200319091516|  [i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule]:", [i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule]


			continue

		#--- 	
		# try:
		_NEXUS._grammar_manager._change_rule_enabled(RuleToDisable_className, False)
		try:
			gl.RbeenExclusive.remove(RuleToDisable_className)
		except :
			pass
		# except:
		# 	winsound.PlaySound("C:\\- To Burn\\- Project My\\Sound My\\Alarm09.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		# 	print "\n", "20200112213924| got exception with '_NEXUS._grammar_manager._change_rule_enabled'| RuleToDisable_className: ", RuleToDisable_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		# 	raise ValueError("(see Print above)")
