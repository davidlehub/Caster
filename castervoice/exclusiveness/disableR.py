from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.lib.control import _NEXUS
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from collections import OrderedDict
from castervoice.exclusiveness.get_AllActiveRules import get_AllActiveRules


def disableR(targetRules_className,aExceptR=[]):
	for targetRule_className in targetRules_className:

		if targetRule_className in aExceptR:
			# gl.RbeenExclusive.add(targetRule_className)
			continue

		#region--- Optimizing by not disable rule not loaded
		# print "\n", "ici 20200319091514|  targetRule_className:", targetRule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

		#--- (Concatonate/add 2 list without duplicate element)
		all_loadedRule_class_Name =  list(OrderedDict.fromkeys(gl.all_Merge_result.all_rule_class_names + [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]))
		# print "\n", "ici 20200319183135|  all_loadedRule_class_Name:", all_loadedRule_class_Name
		# print "\t", "ici 20200319091515|  [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]:", [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]

		# if targetRule_className not in all_loadedRule_class_Name:
		if targetRule_className not in get_AllActiveRules():
			# print "\n", "ici20200319091146| skeep to disable rule:", targetRule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

			#--- (...)
			try:
				gl.RbeenExclusive.remove(targetRule_className) #not sure about this line. It got exception?
				# print "\n", "dbg20200323123659| rule remove from 'gl.RbeenExclusive':", targetRule_className, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

			except :
				pass			

			continue
		#endregion Optimizing by not disable rule not loaded

		#--- Do It.	
		_NEXUS._grammar_manager._change_rule_enabled(targetRule_className, False)
