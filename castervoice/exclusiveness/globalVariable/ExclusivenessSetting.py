
#region--- (Import)
from inspect import getframeinfo, stack, getframeinfo, currentframe
from typing import Callable, Iterator, Union, Optional, List, Dict

#endregion (Import)

#__ Here set enable or not the: exclusive system (that enable or not the: Dragon vocabulary)
use_ExclusiveFeature = True

#__ 
MyRules = ["SpeechEngineVocabulary","Exclusive_Controller","Dragon_Controller","Dragon_Controller", "Exclusive_UniqMode_test"]
# MyRules = []

#__ Fundation Rules (caster alway needs)
Rules_internal = ["GrammarActivatorRule", "HooksActivationRule", "TransformersActivationRule"]

#--- (Copy of '_enabled_ordered' in rules.toml)
# DefaultRulesTobeExclsuive_className = ["Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation", "CasterRule", "HardwareRule", "MouseAlternativesRule", "WindowManagementRule", "DouglasGridRule", "RainbowGridRule", "SudokuGridRule", "HMCRule", "HMCConfirmRule", "HMCDirectoryRule", "HMCHistoryRule", "HMCLaunchRule", "HMCSettingsRule", "HistoryRule", "ChainAlias", "Alias", "BringRule", "Again", "LegionGridRule", "DragonRule"] + Rules_internal


#--- set of Rules that are alway needed, most of time.
#--- ex.: Let say, Visual studio Code is the forground window, then the rules 'VSCodeCcrRule' and 'VSCodeNonCcrRule' are added to this list (RulesToBeExclusive_everyWhere)
#--- TODO: maybe: let user the option to specify when he create the grammar? Especially for: "Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation".

#__ Universale Rules: alway available, in any apps (except when in Uniq Mode)
RulesToBeExclusive_everyWhere = ["Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation", "CasterRule", "HardwareRule", "MouseAlternativesRule", "WindowManagementRule", "DouglasGridRule", "RainbowGridRule", "SudokuGridRule", "HMCRule", "HMCConfirmRule", "HMCDirectoryRule", "HMCHistoryRule", "HMCLaunchRule", "HMCSettingsRule", "HistoryRule", "ChainAlias", "Alias", "BringRule", "Again", "LegionGridRule", "DragonRule"] + MyRules + Rules_internal

# RulesToBeExclusive_everyWhere = ["Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation", "CasterRule", "HardwareRule", "MouseAlternativesRule", "WindowManagementRule", "DouglasGridRule", "RainbowGridRule", "SudokuGridRule", "HMCRule", "HMCConfirmRule", "HMCDirectoryRule", "HMCHistoryRule", "HMCLaunchRule", "HMCSettingsRule", "HistoryRule", "ChainAlias", "Alias", "BringRule", "Again", "LegionGridRule", "DragonRule", "GrammarActivatorRule", "HooksActivationRule", "TransformersActivationRule"] #+ [ct.UniqMode_NonCCR_className]
# RulesToBeExclusive_everyWhere = ['GrammarActivatorRule','HooksActivationRule','TransformersActivationRule']


#region--- (old caster)
# #-- make is = False if we wannt use normal caster, as if we use caster normaly, without my modification adding exclusivity to grammars.
# exClusiveMode = True #- System Exclusiveness mode activated or not. Gonna be = False in 'grammExclusivenessCtrler.py' >> 'normal_caster_mode()'.

#  ##\ True: if we dont wanna use dragon vocabulary, only caster/natlink grammar.
# # StartGrammarInExclusiveMode = False
# StartGrammarInExclusiveMode = True

# ##\ True: in case we want to disable all grammar, bcz we want to test only one grammar.
# ##\ expl20170221102005
# DisableAllGrammar = False # True: in case we want to disable all grammar, bcz we want to test only one grammar.
# # DisableAllGrammar = True
#endregion (old caster)
