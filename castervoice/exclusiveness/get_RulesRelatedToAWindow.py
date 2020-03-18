from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable import GlobalV as gl

def get_RulesRelatedToAWindow(CurrWindowData):
    RulesRelatedToCurrWindow_className = []
    for R in gl.allRegisteredRule_HavingAppContext: #R is type of: C:\Users\HP\Documents\Caster\castervoice\exclusiveness\globalVariable\registeredRule_data.py
        Rdetail = R.detail #Rdetail is type of: #of type: C:\Users\HP\Documents\Caster\castervoice\lib\ctrl\mgr\rule_details.py
        # print "\n", "20200316111905| Rdetail:", Rdetail, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        # print "", "20200316111906| Rdetail.executable:", Rdetail.executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        # print "", "20200316111907| executable:", executable, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
        
        #--- TODO: Filter/validate also using: title
        #--- (Rdetail.executable= ,exemple, 'code')
        # if Rdetail.executable in executable:
        # if Rdetail.executable in executable:
        # 	RulesRelatedToCurrWindow_className.add(R.get_rule_class_name())		
        if Rdetail.executable == CurrWindowData.ForegroundAppProcessName:
            RulesRelatedToCurrWindow_className.append(R.className)
    
    return RulesRelatedToCurrWindow_className