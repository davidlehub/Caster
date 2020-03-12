
from ExclusivenessContext_trigguer import ExclusivenessContext_trigguer
class ExclusivenessContext_test01():
    
    #--- What make this context to activate.
    triggers = ExclusivenessContext_trigguer()
    triggers.whenFocusedWindowChanged = {"windowTitle_endWith" : "Notepad"}
    triggers.whenIsay = ["activate exclusive test 1"]
    
    grammarsToBeExclusive = ["NavigationNon", "Alphabet"]

# class ExclusivenessContext_trigguer():
#     whenFocusedWindowChanged = {"windowTitle_endWith" : "Notepad"}
#     whenIsay = ["activate exclusive test 1"]
