from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.exclusiveness.globalVariable.Data_Manager import data,Exclusiveness,GramAndRules
from castervoice.exclusiveness import Constant as ct

def store_AllEnabledRule_ofApp(aWindHndl, aForce = False):
	if not data.prevWindHndl and not aForce:
		return

	#--- instatiate
	if not data.appGramAndRules.has_key(aWindHndl): data.appGramAndRules[ct.default] = GramAndRules()

	#--- do it
	data.makeAcopy_AllEnabledRule(aWindHndl)


	#region--- (old caster
	# data.makeAcopy_AllEnabledRule(aWindHndl)
	# data.makeAcopy_engineGrammars(aWindHndl)
	# data.makeAcopy_NexusMergerConfigs(aWindHndl)
	#endregion (old caster
