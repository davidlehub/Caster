from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data
from castervoice.exclusiveness.do_backOneLevelOfUML import do_backOneLevelOfUML

#region--- (This is how you annotate a function definitio)
# def f(num1, ListOfString, my_float=3.5):
#     # type: (int,List[str], float) -> float
#     """Your function docstring goes here after the type definition."""
#     return num1 + my_float 
#endregion (This is how you annotate a function definitio)

def backOneLevelOfUML(): #20191123223225
	'''Ending of an uniq mode layer go back to previous one...
	'''
	# dbg = True
	# if dbg: print "\n\n---20181119222315| backOneLevelOfUML:"

	Why = 'back to previous state, bcz an uniq mode layer is finished. |20181216063321)'
	#--== foolproof.
	# if not len(gl.UniqModeLayer_Hist):
	if not data.count_UML_ofApp(data.currWindHndl):
		print "\n", "dbg20200324212026| return, bcz 'not data.count_UML_ofApp(data.currWindHndl)':",  " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return

	#--== remove from history, and at same time put removed item in our target varibale.:
	# CurrUniqModeLayer =  gl.UniqModeLayer_Hist.pop(len(gl.UniqModeLayer_Hist) - 1)
	# CurrUniqModeLayer =  gl.UniqModeLayer_Hist.pop() #trying vers 20191128204732	
	CurrUniqModeLayer =  data.pop_UML_ofCurrApp() #trying vers 20191128204732	
	# print "\n|~ici 20191218141156| CurrUniqModeLayer:",CurrUniqModeLayer , " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
	do_backOneLevelOfUML(CurrUniqModeLayer)
