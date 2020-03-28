from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import (Grammar, Playback, Key, Dictation, Function)
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

#__ __
from castervoice.exclusiveness.exclusiveness_OnOff import exclusiveness_OnOff

# ---Constant------------------------------------------------------------
K = Key
F = Function

class Exclusive_Controller(MappingRule):

	mapping = {
		'turn off exclusive': 
			R(Function(exclusiveness_OnOff, On=False)),
		'turn on exclusive': 
			R(Function(exclusiveness_OnOff, On=True)),			
	}

# ---------------------------------------------------------------------------
def get_rule():
	return Exclusive_Controller, RuleDetails(name="Exclusive Controller")