from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import (Grammar, Playback, Key, Dictation, Function)
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

#__ __
from castervoice.exclusiveness.cls.DragonVocabulary_cls import DragonVocabulary

# ---Constant------------------------------------------------------------
K = Key
F = Function

def DragonVocabulary_disable():
	DragonVocabulary.disable()
def DragonVocabulary_enable():
	DragonVocabulary.enable()

class Exclusive_Controller(MappingRule):

	mapping = {
		'turn off exclusive': 
			R(Function( DragonVocabulary_disable )),
			# R(Function( DragonVocabulary.disable() )),
			# R(Function(exclusiveness_OnOff, On=False)),
		'turn on exclusive':
			R(Function( DragonVocabulary_enable )),
			# R(Function( DragonVocabulary.enable() )),
			# R(Function(exclusiveness_OnOff, On=True)),
	}

# ---------------------------------------------------------------------------
def get_rule():
	return Exclusive_Controller, RuleDetails(name="Exclusive Controller")