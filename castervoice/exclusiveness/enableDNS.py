from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.ExclusivMode_class import ExclusivMode
from castervoice.exclusiveness.globalVariable import GlobalV as gl
from castervoice.lib.control import _NEXUS
from dragonfly.engines import (_default_engine)

from dragonfly.grammar.grammar_base import Grammar

def enableDNS(CompanionRules_clasName=None):
    """ if CompanionRules_clasName=None: Only exclusiveness is deactiavated: DNS vocabularies are available. (All rules (Caster's) currently been activate are idem) """

    print "\n", "(exclusiveness) is OFF."

    #__  
    ExclusivMode.set_enabled(False)
    
    # print "\n", "20200323162131a| Before gl.GbeenExclusive:",_NEXUS._grammar_manager._grammars_container._ccr_grammars, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # print "\n", "20200323162131b| Before gl.GbeenExclusive:",_NEXUS._grammar_manager._grammars_container._non_ccr_grammars, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
    # print "\n", "20200323162131| Before gl.GbeenExclusive:",[i.name for i in gl.GbeenExclusive], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

    #__ turn OFF exclusiveness for grammars
    # for grammar in gl.GbeenExclusive:
    for grammar in _default_engine.grammars:
        # if grammar.loaded:
        #     grammar.set_exclusiveness(0)
        #     print "\n", "20200323162038| grammar exclusive = 0:",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        
        grammar.set_exclusiveness(0)
        # print "\n", "20200323162038| grammar exclusive = 0:",grammar.name , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

        try:
            gl.GbeenExclusive.remove(grammar)
        except:
            pass
    # print "\n", "20200323162131b| After gl.GbeenExclusive:",[i.name for i in gl.GbeenExclusive], " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)

    # _NEXUS._grammar_manager._change_rule_enabled('Alphabet', True) #ok
    # _NEXUS._grammar_manager._change_rule_enabled('GrammarActivatorRule', True) 


    