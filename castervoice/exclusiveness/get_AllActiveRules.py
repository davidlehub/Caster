from castervoice.exclusiveness.globalVariable import GlobalV as gl
from collections import OrderedDict

def get_AllActiveRules():
		
	return list(OrderedDict.fromkeys(gl.all_Merge_result.all_rule_class_names + [i.get_rule_class_name() for i in gl.all_loadedRule_mappingRule]))