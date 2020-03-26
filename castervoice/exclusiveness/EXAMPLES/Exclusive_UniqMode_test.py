from inspect import getframeinfo, stack, getframeinfo, currentframe
from dragonfly import (Grammar, Playback, Key, Dictation, Function)
from dragonfly import MappingRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
#__ __
from castervoice.exclusiveness.backOneLevelOfUML import backOneLevelOfUML
from castervoice.exclusiveness.set_UniqModeLayer import set_UniqModeLay
from castervoice.exclusiveness.UniqModeLayer import UniqModeLayer
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.const import CCRType

# ---Constant------------------------------------------------------------
K = Key
F = Function

#__ 
# def test_ExclusiveUniqMode(text):
def test_ExclusiveUniqMode():
	''' 
	'''

	ThisUniqModeLayer = UniqModeLayer() #instantiate a layer, of uniq mode.

	#region--- customizing
	ThisUniqModeLayer.name = "" #optional, not necessary.
	ThisUniqModeLayer.RtoActivate.extend(['Alphabet','Numbers']) # Rule(s) we want to be active LONELY.
	ThisUniqModeLayer.ending_cmd = {"(done | finished)": R(Function(backOneLevelOfUML), rdescript="")} #spec/command to say to exit/end this uniq mode. (In this case: "(done | finished)")
	#endregion customizing 
	
	set_UniqModeLay(ThisUniqModeLayer)


# class Exclusive_UniqMode_test(MappingRule):
class Exclusive_UniqMode_test(MergeRule):
	pronunciation = "Uniq Mode test"

	mapping = {
		"test uniq mode":
			R(Function(test_ExclusiveUniqMode)), #
	}

# ---------------------------------------------------------------------------
def get_rule():
	return Exclusive_UniqMode_test, RuleDetails(ccrtype=CCRType.GLOBAL)