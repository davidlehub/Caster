from inspect import getframeinfo, stack, getframeinfo, currentframe
from castervoice.exclusiveness.globalVariable.Data_Manager import data

def get_currUniqModeLayer_ofApp(aWindHndl):
	return data.getTop_UML_ofApp(aWindHndl)
