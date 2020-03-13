from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data

def isInUniqModeForCurrApp():
	# if len(gl.UniqModeLayer_Hist):
	if data.count_UML_ofApp(data.currWindHndl) > 0:
		# print "\n|~ici20191218235925| data.count_UML_ofApp(data.currWindHndl):", data.count_UML_ofApp(data.currWindHndl), " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		print "\n|~ici20191218235925| data.currWindHndl:", data.currWindHndl, " || In:",stack()[0][3],"%s|%d " % (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno),"| Caller:",stack()[1][3],"%s:%d" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno)
		return True
	else:
		return False
