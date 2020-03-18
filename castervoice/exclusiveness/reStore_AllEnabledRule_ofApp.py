from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data


def reStore_AllEnabledRule_ofApp(aWindHndl):
	data.putBack_AllEnabledRule(aWindHndl)

	# data.putBack_NexusMergerConfigs(aWindHndl)
	# data.putBack_engineGrammars(aWindHndl)
	# # data.putBack_NexusMergerGrammars(aWindHndl)
	# data.putBack_AllEnabledRule(aWindHndl)
