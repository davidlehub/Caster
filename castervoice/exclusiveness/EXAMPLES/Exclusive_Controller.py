from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import (Grammar, Playback, Key, Dictation, Function)
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

#__ __
from castervoice.exclusiveness.cls.DragonVocabulary_cls import enable_dragonVocabulary,disable_dragonVocabulary,dragonVocabulary_is_Disabled, dragonVocabulary_is_Enabled,enable_temporary_dragonVocabulary, disable_temporary_dragonVocabulary, dragonVocabulary_wasTemporary_disable, dragonVocabulary_wasTemporary_enabled


# ---Constant------------------------------------------------------------
K = Key
F = Function

# def DragonVocabulary_disable():
# 	DragonVocabulary.disable()
# def DragonVocabulary_enable():
# 	DragonVocabulary.enable()

class Exclusive_Controller(MappingRule):

	mapping = {
		'turn off exclusive': 
			R(Function( enable_dragonVocabulary )),
			# R(Function( DragonVocabulary_disable )),
			# R(Function( DragonVocabulary.disable() )),
			# R(Function(exclusiveness_OnOff, On=False)),
		'turn on exclusive':
			R(Function( disable_dragonVocabulary )),
			# R(Function( DragonVocabulary_enable )),
			# R(Function( DragonVocabulary.enable() )),
			# R(Function(exclusiveness_OnOff, On=True)),
	}

# ---------------------------------------------------------------------------
def get_rule():
	return Exclusive_Controller, RuleDetails(name="Exclusive Controller")