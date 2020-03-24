
class UniqModeLayer():
    def __init__(self):
        self.name = ""
        self.RtoActivate = [] #ex.: ["Alphabet", "VSCodeCcrRule"]
        self.ending_cmd = {} #ex.: {"(done | finished)": R(Key(ToSendWhenFinished) +  Function(EndCurrUML_BckToPrviousState))},
        self.uniqRule = []#ex.: 
        self.RbeenExclusive_stored = []#ex.: 
