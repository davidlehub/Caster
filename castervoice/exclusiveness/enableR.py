from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.lib.control import _NEXUS
from collections import OrderedDict

# import inspect

#--- TODO: For more optimisation: look like this methode running 2 times, but it suppose to do it 1 time... || And same for 'disableR'?
def enableR(targetRules_className):
	""" Enables Rules so they gonna be part of exclusiveness """
	 
	for targetRule_className in targetRules_className:
		if targetRule_className in gl.RbeenExclusive:
			# print "\n", "20200316170549| skeep targetRule_className:", targetRule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
			continue

		#region--- Optimizing by not enable rule already loaded
		#--- (Concatonate/add 2 list without duplicate element)
		# all_loadedRule_class_Name =  list(OrderedDict.fromkeys([i.get_rule_class_name() for i in gl.all_loadedRule_mergeRule] + [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]))
		all_loadedRule_class_Name =  list(OrderedDict.fromkeys(gl.all_Merge_result.all_rule_class_names + [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]))
		if targetRule_className in all_loadedRule_class_Name:
			# print "\n", "20200319185240| skeep to enable rule:", targetRule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

			#--- (Add to the list, bcz that rule gonna be exclusive)
			gl.RbeenExclusive.append(targetRule_className)

			continue
		#endregion Optimizing by not enable rule already loaded

		_NEXUS._grammar_manager._change_rule_enabled(targetRule_className, True)

		gl.RbeenExclusive.append(targetRule_className)