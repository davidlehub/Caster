from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import (Grammar, Playback, Key, Dictation, Function)
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
#__ __
from castervoice.exclusiveness.makeDragonHeard import makeDragonHeard

# ---Constant------------------------------------------------------------
K = Key
F = Function

# class Dragon_Controller(MergeRule):
class Dragon_Controller(MappingRule):

	mapping = {
		'micof': #turn off microphone (DNS).
			R(Function(makeDragonHeard, pWords=[
			  "microphone", "off"], pTime=0.0)),
	}

# ---------------------------------------------------------------------------
def get_rule():
	return Dragon_Controller, RuleDetails(name="Dragon Controller rule")