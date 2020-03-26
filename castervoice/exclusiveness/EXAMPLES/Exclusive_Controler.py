from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import (Grammar, Playback, Key, Dictation, Function)
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
#__ __
from castervoice.exclusiveness.enableDNS_byTurnOff_exclusiveness import enableDNS_byTurnOff_exclusiveness

# ---Constant------------------------------------------------------------
K = Key
F = Function

class Exclusive_Controler(MappingRule):

	mapping = {
		'turn off exclusive': 
			R(Function(enableDNS_byTurnOff_exclusiveness)),
		'turn on exclusive': 
			R(Function(enableDNS_byTurnOff_exclusiveness)),			
	}

# ---------------------------------------------------------------------------
def get_rule():
	return Exclusive_Controler, RuleDetails(name="Dragon Controler rule")