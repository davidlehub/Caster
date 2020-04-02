class EventType(object):
    ACTIVATION = "activation"
    NODE_CHANGE = "node change"
    GRAMMERS_LOADED = "grammars loaded"
    ON_ERROR = "on error"
    RULES_LOADED = "rules loaded"

    #region--- (david) 
    RULES_LOADED_EXCL = "rules loaded exclusive"
    APPCONTEXT_Matched_EXCL = "App Context Matched EXCL"
    REGISTER_Rule_EXCL = 'Register Rule EXCL'
    REMERGE_CCR_RULES_EXCL = 'REMERGE CCR RULES EXCL'
    SPOKEN_RECOGNIZED = 'SPOKEN RECOGNIZED'
    #endregion