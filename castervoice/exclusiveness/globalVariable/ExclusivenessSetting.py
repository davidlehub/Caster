
from castervoice.exclusiveness import Constant as ct


#--- (Copy of '_enabled_ordered' in rules.toml)
DefaultRulesTobeExclsuive_className = ["Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation", "CasterRule", "HardwareRule", "MouseAlternativesRule", "WindowManagementRule", "DouglasGridRule", "RainbowGridRule", "SudokuGridRule", "HMCRule", "HMCConfirmRule", "HMCDirectoryRule", "HMCHistoryRule", "HMCLaunchRule", "HMCSettingsRule", "HistoryRule", "ChainAlias", "Alias", "BringRule", "Again", "LegionGridRule", "DragonRule", "GrammarActivatorRule", "HooksActivationRule", "TransformersActivationRule"] #+ [ct.UniqMode_NonCCR_className]

#--- set of Rules that are alway needed, most of time.
#--- ex.: Let say, Visual studio Code is the forground window, then the rules 'VSCodeCcrRule' and 'VSCodeNonCcrRule' are added to this list (RulesToBeAlwayExclusive_className)
#--- TODO: maybe: let user the option to specify when he create the grammar? Especially for: "Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation".
RulesToBeAlwayExclusive_className = ["Alphabet", "Navigation", "NavigationNon", "Numbers", "Punctuation", "CasterRule", "HardwareRule", "MouseAlternativesRule", "WindowManagementRule", "DouglasGridRule", "RainbowGridRule", "SudokuGridRule", "HMCRule", "HMCConfirmRule", "HMCDirectoryRule", "HMCHistoryRule", "HMCLaunchRule", "HMCSettingsRule", "HistoryRule", "ChainAlias", "Alias", "BringRule", "Again", "LegionGridRule", "DragonRule", "GrammarActivatorRule", "HooksActivationRule", "TransformersActivationRule"] #+ [ct.UniqMode_NonCCR_className]
# RulesToBeAlwayExclusive_className = ['GrammarActivatorRule','HooksActivationRule','TransformersActivationRule']


#region--- (old caster)
#-- make is = False if we wannt use normal caster, as if we use caster normaly, without my modification adding exclusivity to grammars.
exClusiveMode = True #- System Exclusiveness mode activated or not. Gonna be = False in 'grammExclusivenessCtrler.py' >> 'normal_caster_mode()'.

 ##\ True: if we dont wanna use dragon vocabulary, only caster/natlink grammar.
# StartGrammarInExclusiveMode = False
StartGrammarInExclusiveMode = True

##\ True: in case we want to disable all grammar, bcz we want to test only one grammar.
##\ expl20170221102005
DisableAllGrammar = False # True: in case we want to disable all grammar, bcz we want to test only one grammar.
# DisableAllGrammar = True
#endregion (old caster)
